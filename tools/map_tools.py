import geopandas as gpd
import folium
import branca.colormap as cm
import streamlit as st
import tools.data_tools as d_t
import json
from shapely import wkt

def init_map(lat_lon = [50.6282,3.06881],width='80%',height='80%',tiles='CartoDB positron', zoom_start=6):

    # si un zoom a été choisi
    if len(st.session_state.zoom_on_centroid) >0 :
      lat_lon= st.session_state.zoom_on_centroid
      zoom_start=11

    map = folium.Map(location= lat_lon,width=width, height=height,tiles=tiles, zoom_start=zoom_start)
    return map


def add_tileLayer(map) :
  # ajoute le choix du fond de carte
  folium.TileLayer('openstreetmap',attr='&copy;MDS').add_to(map)
  folium.TileLayer('Stamen Terrain',attr='&copy;MDS').add_to(map)
  folium.TileLayer('stamentoner',attr='&copy;MDS').add_to(map)
  folium.TileLayer('cartodbpositron',attr='&copy;MDS').add_to(map)
  folium.LayerControl().add_to(map)
  return map


def add_categorical_legend(map, title, colors, labels):
  
  if len(colors) != len(labels):
      raise ValueError("colors and labels must have the same length.")

  color_by_label = dict(zip(labels, colors))
  
  legend_categories = ""     
  for label, color in color_by_label.items():
      legend_categories += f"<li><span style='background:{color}'></span>{label}</li>"
      
  legend_html = f"""
  <div id='maplegend' class='maplegend'>
    <div class='legend-title'>{title}</div>
    <div class='legend-scale'>
      <ul class='legend-labels'>
      {legend_categories}
      </ul>
    </div>
  </div>
  """
  script = f"""
      <script type="text/javascript">
      var oneTimeExecution = (function() {{
                  var executed = false;
                  return function() {{
                      if (!executed) {{
                            var checkExist = setInterval(function() {{
                                      if ((document.getElementsByClassName('leaflet-bottom leaflet-right').length) || (!executed)) {{
                                        document.getElementsByClassName('leaflet-bottom leaflet-right')[0].style.display = "flex"
                                        document.getElementsByClassName('leaflet-bottom leaflet-right')[0].style.flexDirection = "column"
                                        document.getElementsByClassName('leaflet-bottom leaflet-right')[0].innerHTML += `{legend_html}`;
                                        clearInterval(checkExist);
                                        executed = true;
                                      }}
                                  }}, 100);
                      }}
                  }};
              }})();
      oneTimeExecution()
      </script>
    """
  

  css = """

  <style type='text/css'>
    .maplegend {
      z-index:9999;
      float:right;
      background-color: rgba(255, 255, 255, 1);
      border-radius: 5px;
      border: 2px solid #bbb;
      padding: 5px;
      font-size:12px;
      positon: relative;
    }
    .maplegend .legend-title {
      text-align: left;
      margin-bottom: 5px;
      font-weight: bold;
      font-size: 90%;
      }
    .maplegend .legend-scale ul {
      margin: 0;
      margin-bottom: 5px;
      padding: 0;
      float: left;
      list-style: none;
      }
    .maplegend .legend-scale ul li {
      font-size: 80%;
      list-style: none;
      margin-left: 0;
      line-height: 18px;
      margin-bottom: 2px;
      }
    .maplegend ul.legend-labels li span {
      display: block;
      float: left;
      height: 16px;
      width: 30px;
      margin-right: 0px;
      margin-left: 0;
      border: 0px solid #ccc;
      }
    .maplegend .legend-source {
      font-size: 80%;
      color: #777;
      clear: both;
      }
    .maplegend a {
      color: #777;
      }
  </style>
  """

  map.get_root().header.add_child(folium.Element(script + css))

  return map


def create_square_map(map, df,vmin, vmax, caption=''):


    # Convert shape column to a geoseries and specify crs
    df['shape'] = gpd.GeoSeries.from_wkt(df['shape'], crs = "EPSG:4326")

    # creation de la legende
    colormap = cm.LinearColormap(colors=['lightblue', 'red'],
                             index=[vmin,vmax], vmin=vmin, vmax=vmax,
                             caption=caption)
    # fonction squi definit la forme et la couleur d'un carreau
    def style_function(feature):
        fillOpacity = 0.7
        weight = 1
        fillColor = colormap(feature['properties']['Score'])
        color = colormap(feature['properties']['Score'])

        if st.session_state['chosen_format']  == "DRIVE" or st.session_state['chosen_format']  == "PIETON" :
            if feature['properties']['Isolement'] ==  'Low':
                fillOpacity = 0
                weight = 2  
        return {'fillColor': fillColor,'fillOpacity':fillOpacity,'color': color,'weight':weight  }

    # boucle sur chaque ligne pour déssiner un carreau
    for _, r in df.iterrows():   
        # Without simplifying the representation of each borough,
        # the map might not be displayed
        sim_geo = gpd.GeoSeries(r['shape']).simplify(tolerance=0.001)
        geo_json = sim_geo.to_json()
        geo_json_dict = json.loads(geo_json)
        
        geo_json_dict["features"][0]['properties']['Score'] = r['Score']
        if st.session_state['chosen_format']  == "DRIVE":
            geo_json_dict["features"][0]['properties']['Isolement'] = r['Isolement']
        elif st.session_state['chosen_format']  == "PIETON":
            geo_json_dict["features"][0]['properties']['Isolement'] = r['Isolement']

        geo_json = json.dumps(geo_json_dict)
 
        geo_square = folium.GeoJson(data=geo_json,
                            zoom_on_click=True,
                            style_function= style_function)
                            
        folium.Popup(
          "Rang:" + str(r['Rang'])+
          '</br>'+
          "Nb ménages: " + str(r['Nb_menages'])+
          '</br>'+
          "Score: " +str(round(r['Score'],2))
          ).add_to(geo_square)

        geo_square.add_to(map)
    
    # ajout de la legende a la carte
    colormap.add_to(map)

    return map


def create_IC_pieton_map(map):
    
    # get carreuax pour carte d'intensité concurrentielle
    df = d_t.get_square_intConc_pieton()
    
   
    # Convert shape column to a geoseries and specify crs
    df['shape'] = gpd.GeoSeries.from_wkt(df['shape'], crs = "EPSG:4326")

    vmin = df['Score'].min()
    vmax = df['Score'].max()
    
    # creation de la legende
    colormap = cm.StepColormap(colors=['lightgreen','green','yellow','orange','red','darkred','black'],
                                index=[1.25,1.54,2.25,3.86,5,20,50],
                                vmin=vmin, 
                                vmax=vmax,
                                caption="Intensité concurentielle: moyenne ---------------------------------> trés forte")
    
    # fonction qui renvoi la forme et la couleur du carreau
    def style_function(feature):
        fillOpacity = 0.5
        weight = 1
        fillColor = colormap(feature['properties']['Score'])
        color = colormap(feature['properties']['Score'])           
        return {'fillColor': fillColor,'fillOpacity':fillOpacity,'color': color,'weight':weight  }

    # boucle pour dessiner les carreaux un par un
    for _, r in df.iterrows():
        sim_geo = gpd.GeoSeries(r['shape']).simplify(tolerance=0.001)
        geo_json = sim_geo.to_json()
        geo_json_dict = json.loads(geo_json)
        geo_json_dict["features"][0]['properties']['Score'] = r['Score']
        geo_json = json.dumps(geo_json_dict)
        geo_square = folium.GeoJson(data=geo_json,
                            zoom_on_click=True,
                            style_function= style_function)
        folium.Popup(
          "Score: " +str(round(r['Score'],2))
          ).add_to(geo_square)
        geo_square.add_to(map)
    
    " ajout de la legende sur la carte"
    colormap.add_to(map)

    return map