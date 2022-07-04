
import streamlit as st
import pandas as pd
import pickle
import requests



#### LOAD DATA ######################################################################################################

@st.cache
def load_darkstores():
  data = pd.read_csv("csv/qc_conc.csv")
  return data

@st.cache
def load_drives():
  data = pd.read_csv("csv/drives.csv")
  return data

@st.cache
def load_scores_villes():
  data = pd.read_csv("csv/score_ville.csv")
  return data

@st.cache
def load_square_drives():
  with open('pickle/square_drives.pkl', 'rb') as f :
    data = pickle.load(f)
  return data

@st.cache
def load_square_qc():
  with open('pickle/square_qc.pkl', 'rb') as f :
    data = pickle.load(f)
  return data

@st.cache
def load_square_lad():
  with open('pickle/square_lad.pkl', 'rb') as f :
    data = pickle.load(f)
  return data


@st.cache
def load_square_pieton():
  with open('pickle/square_pieton.pkl', 'rb') as f :
    data = pickle.load(f)
  return data

# @st.cache(allow_output_mutation=True)
def load_square_intConc_pieton():
  with open('pickle/square_int_conc_pieton.pkl', 'rb') as f :
    data = pickle.load(f)
  return data

# ### GET LOADER ######################################################################################################

def load_lottieurl():
  url = 'https://assets10.lottiefiles.com/packages/lf20_uzn9pvbz.json'
  r = requests.get(url)
  if r.status_code != 200:
      return None
  return r.json()

#### GET DATA ######################################################################################################


def get_territory_lat_lon(chosen_territory_name, territories_json):
  for territory in territories_json['territory']:
    if territory['territoryLabel'] == chosen_territory_name:
      latitude = territory['latitude']
      longitude = territory['longitude']
  return latitude,longitude


def get_darkstores():
  data = load_darkstores()
  return data

def get_scores_villes(territoryLabel):
  data = load_scores_villes()
  data = data[ data['territoryLabel'] == territoryLabel ]
  data = data[ ['Rang','Departement','Commune','Score','Habitants']  ]
  data['Score'] = data['Score'].round(2)
  return data


def get_drives(choosen_sites_list,territoryLabel):
  data = load_drives()
  data = data.loc[data['nom_enseigne'].isin(choosen_sites_list)]
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data


def get_square_drives(territoryLabel):
  data = load_square_drives()
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data


def get_square_qc(territoryLabel):
  data = load_square_qc()
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data

def get_square_lad(territoryLabel):
  data = load_square_lad()
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data

def get_square_pieton(territoryLabel):
  data = load_square_pieton()
  data = data[ data['territoryLabel'] == territoryLabel ]
  return data


def get_square_intConc_pieton():
  data = load_square_intConc_pieton()
  return data