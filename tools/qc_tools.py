

import folium
from folium.features import CustomIcon

import values as val
import json

import tools.map_tools as map_t


def qc_icon():

  icons_json = json.loads(val.icon_list)

  for icon in icons_json['darkstore']:
    if icon['nom_enseigne'] == 'darkstore':
      icon_url = icon['icon_url']
      icon_size=icon['icon_size']

      url = "./icons/{}".format
      icon_image = url(icon_url)

      icon_todisplay = CustomIcon(
        icon_image,
        icon_size=icon_size,
      )
      return icon_todisplay


def pin_sites(map,df_sites):
 
  for latitude, longitude, nom_enseigne in zip(df_sites.latitude, df_sites.longitude, df_sites.nom_enseigne):
            folium.Marker(
                location=(latitude,longitude),
                popup=nom_enseigne,
                icon=qc_icon()                
                ).add_to(map)
  return map


def create_map(territory_lat_lon,df_conc,df_square,score_min,score_max):
  
  
  # création et centrage de la map
  map = map_t.init_map( territory_lat_lon)

  # affichage des square
  map = map_t.create_square_map(map ,df_square,vmin=score_min,vmax=score_max,caption = 'Probabilité de performance' )

  #creation des markers
  if not df_conc.empty :
    map = pin_sites(map, df_conc)
  
  # Set legend on map
  map = map_t.add_categorical_legend(map, ' ',
                                colors =[' ',' '],
                                labels = ['Carreau plein : non isolé','Carreau vide: isolé'])
  
  return map


