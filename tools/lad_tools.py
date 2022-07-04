
import tools.map_tools as map_t




def create_map(territory_lat_lon,df_conc,df_square,score_min,score_max):
    
  map = map_t.init_map( territory_lat_lon)

  # affichage des square
  map = map_t.create_square_map(map ,df_square,vmin=score_min,vmax=score_max,caption = 'Score' )

   
  return map





