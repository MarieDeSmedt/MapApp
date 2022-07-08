
import streamlit as st
import pandas as pd
import pickle




#### LOAD DATA ######################################################################################################



@st.cache
def load_drives():
  data = pd.read_csv("csv/drives.csv")
  return data



@st.cache
def load_square_drives():
  with open('pickle/square_drives.pkl', 'rb') as f :
    data = pickle.load(f)
  return data



#### GET DATA ######################################################################################################


def get_territory_lat_lon(chosen_territory_name, territories_json):
  for territory in territories_json['territory']:
    if territory['territoryLabel'] == chosen_territory_name:
      latitude = territory['latitude']
      longitude = territory['longitude']
  return latitude,longitude



def get_drives(choosen_sites_list,territoryLabel):
  data = load_drives()
  data = data.loc[data['nom_enseigne'].isin(choosen_sites_list)]
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data


def get_square_drives(territoryLabel):
  data = load_square_drives()
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data

