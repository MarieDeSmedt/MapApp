
import tools.map_tools as map_t



def create_map(territory_lat_lon,df_square,score_min,score_max):
  
  # création et centrage de la map
  map = map_t.init_map( territory_lat_lon)

  # affichage des square
  map = map_t.create_square_map(map ,df_square,vmin=score_min,vmax=score_max,caption = 'Probabilité de performance' )

  
  # Set legend on map
  map = map_t.add_categorical_legend(map, ' ',
                                colors =[' ',' '],
                                labels = ['Carreau plein : non isolé','Carreau vide: isolé'])
  
  return map