import values as val
import folium
import json
from folium.features import CustomIcon
import tools.map_tools as map_t
import pandas as pd



def sites_icon(nom_enseigne):
  """
  It takes a string as an argument, and returns a custom icon object
  
  :param nom_enseigne: the name of the site
  :return: the icon_todisplay variable.
  """
  icon_list = json.dumps(val.icons)
  icons_json = json.loads(icon_list)

  for icon in icons_json['drive']:
    if icon['nom_enseigne'] == nom_enseigne:
      icon_url = icon['icon_url']
      icon_size=icon['icon_size']
      
      url = "./icons/{}".format
      icon_image = url(icon_url)

      icon_todisplay = CustomIcon(
        icon_image,
        icon_size=icon_size,
      )
      return icon_todisplay



def pin_sites(map: map, df_sites: pd.DataFrame) -> map:
  """
  It takes a map and a dataframe as input, and returns a map with markers on it
  
  :param map: the map object
  :param df_sites: the dataframe containing the sites' coordinates
  :return: A map with the sites pinned on it.
  """
 
  for latitude, longitude, nom_enseigne in zip(df_sites.latitude, df_sites.longitude, df_sites.nom_enseigne):
            folium.Marker(
                location=(latitude,longitude),
                popup=nom_enseigne,
                icon=sites_icon(nom_enseigne)                
                ).add_to(map)
  return map



def create_map(territory_lat_lon,df_conc,df_square,score_min,score_max):
  """
  It creates a map, adds squares to it, adds markers to it, and adds a legend to it
  
  :param territory_lat_lon: a tuple of latitude and longitude coordinates for the center of the map
  :param df_conc: a dataframe with the coordinates of the sites to pin
  :param df_square: a dataframe with of the square to draw
  :param score_min: the minimum  score
  :param score_max: the maximum score 
  :return: A map
  """
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






