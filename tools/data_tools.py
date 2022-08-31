
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
  """
  It loops through the territories_json object and returns the latitude and longitude of the territory
  that matches the chosen_territory_name
  
  :param chosen_territory_name: The name of the territory you want to get the latitude and longitude
  for
  :param territories_json: The JSON file that contains the territories and their lat/lon coordinates
  :return: A tuple of latitude and longitude
  """
  for territory in territories_json['territory']:
    if territory['territoryLabel'] == chosen_territory_name:
      latitude = territory['latitude']
      longitude = territory['longitude']
  return latitude,longitude



def get_drives(choosen_sites_list,territoryLabel):
  """
  It takes a list of sites and a territorylabel, and returns a dataframe of all the drives that match
  those criteria
  
  :param choosen_sites_list: a list of sites that you want to get the data for
  :param territoryLabel: the territory you want to get the data for
  :return: A dataframe with the choosen sites and the choosen territory
  """
  data = load_drives()
  data = data.loc[data['nom_enseigne'].isin(choosen_sites_list)]
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data


def get_square_drives(territoryLabel):
  """
  > This function loads the data , filters it by the territoryLabel, and returns
  the filtered data
  :param territoryLabel: The territory label you want to get the data for
  :return: A dataframe with the territoryLabel column filtered to only include the territoryLabel
  passed in.
  """
  data = load_square_drives()
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data

