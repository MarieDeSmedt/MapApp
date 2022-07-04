import streamlit as st
import pandas as pd
import tools.data_tools as d_t
import tools.drive_tools as dri_t
import tools.qc_tools as qc_t
import tools.lad_tools as l_t
import tools.pieton_tools as p_t
import tools.map_tools as map_t
import json
import values as val
from streamlit_lottie import st_lottie_spinner
from streamlit_folium import folium_static
from st_aggrid import AgGrid
from shapely.geometry import point,LineString
from shapely import wkt
from geopy.distance import geodesic
import geopandas as gpd

def init():
    # init du rayon de zoom en km
    st.session_state['distance'] = 7
    # init du bouton "afficher carte"
    st.session_state['open_map'] = False
    # init du zoom
    st.session_state.zoom_on_centroid = ()

def choose_territory():
    territories_json = json.loads(val.territory_list)
    territory_names = []
    for territory in territories_json['territory']:
        territory_names.append(territory['territoryLabel'])

    # sélectionner le territoire sur lequel centrer la map
    chosen_territory_name = st.sidebar.selectbox(
        'TERRITOIRE',
        territory_names,
        index=1,
        on_change=init
        )
    return chosen_territory_name,territories_json


def filter_nb_menages(df):
    nbHab_min = 20.0 
    nbHab_max = float(df.Nb_menages.max())
    chosen_nbHab_min = st.sidebar.slider(
                        "Nombre de ménages minimum au carreau",
                        min_value=nbHab_min,
                        max_value=nbHab_max,
                        value= 20.0,
                        on_change=init
                        )
    df = df[ df['Nb_menages'] >= chosen_nbHab_min ]
    return df


def filter_score(df):
    score_min = float(df.Score.min())
    score_max = float(df.Score.max())
    chosen_score_min = st.sidebar.slider(
                        "Score de performance minimum",
                        min_value=score_min,
                        max_value=score_max,
                        on_change=init
                        )
    df = df[ df['Score'] >= chosen_score_min ]
    return df


def square_zoom(df):
    if st.session_state['chosen_format'] != "QUICK COMMERCE":
        list_rang = df.Rang.sort_values().to_list()
        list_rang.insert(0,"Tous les carreaux")
        zoom_choice = st.selectbox("Zoomer sur un carreau (rang):",list_rang)

        if zoom_choice != "Tous les carreaux":
            
            # récupérer le carreau choisi
            df_chosen = df[df['Rang']==zoom_choice]
            value_shape = df_chosen.iloc[0]['shape']
        
            # récvupérer les coordonées du  centre du carreau choisi
            str_shape = wkt.loads(value_shape)
            lat_chosen = str_shape.centroid.y
            lon_chosen = str_shape.centroid.x
            st.session_state.zoom_on_centroid=(lat_chosen ,lon_chosen)
            a = st.session_state.zoom_on_centroid

            #  instancier le df to return
            _list=[]
            new_df = pd.DataFrame()


            # boucler sur tous les  autres carreaux
            for _,row in df.iterrows():
                
                row_shape = row['shape']
                # récvupérer les coorodonées du centre du carreau 
                row_str_shape = wkt.loads(row_shape)
                lat_row = row_str_shape.centroid.y
                lon_row = row_str_shape.centroid.x

                
                # calculer la distance entre les deux centres
                b = (lat_row ,lon_row)
                dist = geodesic(a,b).km
                
                # si la distance est < 7km
                
                if dist <= st.session_state['distance']:
                    r = row.to_dict() # Converting the row to dictionary
                    _list.append(r) # appending the dictionary to list

            
            # injecter ces carreau dans le nouveau df 
            new_df = pd.DataFrame(_list)
        
            return new_df
        else:
            st.session_state.zoom_on_centroid=()
            return df
    else:
        return df


def open_map(map):
        
    # save map for downloading
    map.save('full_map.html')

    #dowload button        
    with open('full_map.html', 'rb') as f:
        st.download_button('Download map', f, file_name='full_map.html') 
    
    if st.session_state['chosen_format'] in ( "PIETON" , "DRIVE"): 
            st.caption('Carreau isolé (vide): moins de 30 carreaux à potentiel dans un périmètre de 3.5km')

    #display map
    folium_static(map)


def create_form(format):     

    # choisir le territoire
    chosen_territory_name,territories_json = choose_territory()  
    if len(chosen_territory_name)>0 :
            # recuperer latitude et longitude du territoire pour centrer map
            territory_lat_lon = d_t.get_territory_lat_lon(chosen_territory_name,territories_json)
    
    # init de la liste des concurrents
    df_conc = pd.DataFrame()

    # les selecteurs diffèrent en fonction du format
    if format == 'DRIVE':
        # selectionner les sites à faire apparaitre sur la map
        chosen_drives_list = st.sidebar.multiselect(
                                'Sélectionnez les enseignes à afficher',
                                val.typeDrive_list ,
                                on_change=init
                            )
        if len(chosen_drives_list) >0:
            # download concurrents
            df_conc = d_t.get_drives(chosen_drives_list,chosen_territory_name)
        #  dowload les carreaux à dessiner
        df_square = d_t.get_square_drives(chosen_territory_name)
        
    if format == 'QUICK COMMERCE':
        #proposer le choix d'afficher les darkstores concurrents
        display_darkstore= st.sidebar.checkbox(
                                "Afficher les concurrents",
                                on_change=init
                                )
        if display_darkstore:
            # download concurrents
            df_conc=d_t.get_darkstores()

        # pour le QC on va afficher la liste des villes et non les carreaux dans le tableau
        st.session_state.villes = d_t.get_scores_villes(chosen_territory_name)
        #  dowload square to draw
        df_square = d_t.get_square_qc(chosen_territory_name)
       
    if format == "LAD":
        #  dowload square to draw
        df_square = d_t.get_square_lad(chosen_territory_name)
    
    if format == "PIETON":
        # modification du rayon à afficher en cas de zoom
        st.session_state['distance']= 4
        #  dowload square to draw
        df_square = d_t.get_square_pieton(chosen_territory_name)
     
    # sélectionner les valeurs de nb hab mini
    df_square = filter_nb_menages(df_square)
    
    # sélectionner les valeurs du Score mini
    df_square = filter_score(df_square)

    return chosen_territory_name,territory_lat_lon, df_square, df_conc


def display_intConc_pieton_page():
    # init de la map
    map = map_t.init_map(lat_lon = [50.6282,3.06881],width='100%',height='100%',tiles='CartoDB positron', zoom_start=6)
    # création des carreaux de l'intensité concurrentielle
    # map = map_t.create_IC_pieton_map(map)
    # affichage de la carte
    # open_map(map)


def display_zoneChaudes_page():

    # selectionner les formats à faire apparaitre sur la map
    st.session_state['chosen_format'] = st.sidebar.selectbox(
        'FORMATS',
        val.formats_list,
        on_change=init
        )
        
    # création de la sidebar #######################################################################

    # choix du format
    format = st.session_state['chosen_format']

    # création des éléments en fonction du format
    chosen_territory_name, territory_lat_lon, df_square, df_conc =create_form(format)
    
    # affichage message alerte si IDF
    if chosen_territory_name == "ILE-DE-FRANCE":
        if format != "DRIVE": 
            st.warning ("modèle en cours d'optimisation")
    
    # si PIETON et IDF pas de carte sinon go
    if chosen_territory_name == "ILE-DE-FRANCE" and format == "PIETON":
        # CARTE_PIETON
        # si vous voulez afficher la carte pieton mettre go = TRUE  
        go = False
    else :
        go = True

    if go :

        # création du bouton pour affichage carte
        click_btn = st.sidebar.button(label = 'ouvrir carte')
        if click_btn:
            st.session_state['open_map']=True

        # si le bouton est cliqué
        if st.session_state['open_map']:
            
            # instanciation d'un dataframe specifique au quick commerce
            if 'villes' in st.session_state:
                df_villes = st.session_state.villes
            else:
                df_villes = pd.DataFrame()
            
            # choisir le zoom
            df_zoomed = square_zoom(df_square)
            st.session_state['to_pulp'] = df_zoomed


            # creation de variable pour creation de la carte
            score_min = float(df_square.Score.min())
            score_max = float(df_square.Score.max())


            # création de la carte en fonction du format choisi
            if st.session_state['chosen_format']  == "DRIVE":
                map = dri_t.create_map(territory_lat_lon,df_conc,df_zoomed,score_min,score_max)                

            if st.session_state['chosen_format']  == "QUICK COMMERCE":
                map = qc_t.create_map(territory_lat_lon,df_conc,df_zoomed,score_min,score_max)
                
            if st.session_state['chosen_format']  == "LAD":
                map = l_t.create_map(territory_lat_lon,df_conc,df_zoomed,score_min,score_max)

            if st.session_state['chosen_format']  == "PIETON":
                map = p_t.create_map(territory_lat_lon,df_zoomed,score_min,score_max)
        
            #display map on left and  dataframe in right
            row1 = st.columns((10,2,10))

            with row1[0] : # colonne 1
                
                # afficher carte
                open_map(map)

            with row1[2]: # colonne 2

                # affichage nombre de carreaux a afficher    
                st.info('Nombre de carreaux à potentiel: '+ str(df_zoomed.shape[0]) )
                
                #filtrage des carreaux à afficher dans le tableau en fonction du format
                if st.session_state['chosen_format']  == "DRIVE":
                    df_to_display = df_zoomed.copy()
                    df_to_display = df_to_display[['Rang','InspireCode','Score','Nb_menages','Isolement']]
                    df_to_display['Score'] = df_to_display['Score'].round(2)
                    df_to_display['Isolement'] = df_to_display.Isolement.apply(lambda x: "isolé" if x=='Low' else "non isolé")
                    df_to_display.sort_values(by = ['Rang'], inplace=True)

                if st.session_state['chosen_format']  == "LAD":
                    df_to_display = df_zoomed.copy()
                    df_to_display = df_to_display[['Rang','InspireCode','Score','Nb_menages']]
                    df_to_display['Score'] = df_to_display['Score'].round(2)
                    df_to_display.sort_values(by =['Rang'], inplace=True)

                if st.session_state['chosen_format']  == "PIETON":
                    df_to_display = df_zoomed.copy()
                    df_to_display = df_to_display[['Rang','InspireCode','Score','Nb_menages','Isolement','shape']]
                    df_to_display['Score'] = df_to_display['Score'].round(2)
                    df_to_display['Isolement'] = df_to_display.Isolement.apply(lambda x: "isolé" if x=='Low' else "non isolé")
                    df_to_display.sort_values(by = ['Rang'], inplace=True)

                if st.session_state['chosen_format']  == "QUICK COMMERCE":
                    df_to_display = df_zoomed.copy()
                    df_to_display.sort_values(by =['Rang'], inplace=True)
                    
                # cas particulier du quick commerce: on affiche des villes et non les carreaux
                if st.session_state['chosen_format']  == "QUICK COMMERCE":
                    AgGrid(df_villes)
                else :
                    AgGrid(df_to_display)
            
            # si on est dans le pieton on affiche dessous la carte de l'intensité concurrentielle
            if st.session_state['chosen_format']  == "PIETON":
                st.header("Intensité concurentielle")
                display_intConc_pieton_page()

            # si on veut rajouter des cartes: démo ou CA/UC ca sera ici

            st.session_state['df_to_pulp'] = df_to_display
            




