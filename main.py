
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from tools.tools import display_zoneChaudes_page,open_map
import tools.pieton_tools as p_t
from test import display_pulp





# configuration
st.set_page_config(
    page_title='MapApp',
    layout="wide",
    page_icon="icons/icon_auchan.png",
    initial_sidebar_state="auto")

#  keep off padding on page
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

#  set image
st.sidebar.image('icons/logo_auchan.png')

#  set title
st.header("[DÉVELOPPEMENT] - ZONES CHAUDES")
st.subheader(" macro des zones à fort potentiel de développement par format")

# init session_state
if 'open_map' not in st.session_state:
    st.session_state['open_map'] = False
if 'zoom_on_centroid' not in st.session_state:
    st.session_state.zoom_on_centroid = ()
if 'page' not in st.session_state:
    st.session_state.page=""
if 'distance' not in st.session_state:
    st.session_state.distance = 7
if 'to_pulp' not in st.session_state:
    st.session_state.to_pulp = False
if 'df_to_pulp' not in st.session_state:
    st.session_state['df_to_pulp']= pd.DataFrame()
if 'pulped' not in st.session_state:
    st.session_state['pulped']= pd.DataFrame()


# affichage
display_zoneChaudes_page()

#test pulp
if st.session_state['chosen_format']  == "PIETON" and len(st.session_state['zoom_on_centroid']) > 0:
    
    df_pulped = display_pulp(st.session_state['df_to_pulp'])
    
    # creation de variable pour creation de la carte
    score_min = float(df_pulped.Score.min())
    score_max = float(df_pulped.Score.max())

    pulped_map = p_t.create_map(st.session_state.zoom_on_centroid,df_pulped,score_min,score_max)
    open_map(pulped_map)


# #  set pages names
# st.session_state.page = option_menu(
#         menu_title = None,
#         options = ["Zones chaudes", "Intensité concurentielle PIETON"], 
#         # menu_icon="cast", 
#         default_index=0, 
#         orientation="horizontal")


# # display page
# if st.session_state.page == "Zones chaudes":
#     display_zoneChaudes_page()
# elif st.session_state.page == "Intensité concurentielle PIETON":
#     st.session_state['chosen_format'] = "IC_pieton"
#     display_intConc_pieton_page()
# else:
#     st.warning("modèle en cours de construction")
    