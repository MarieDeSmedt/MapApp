import streamlit as st


def display_homepage():
    st.warning("in process")
    # un formulaire
    # return elements de connexion

def user_exist_control():
    return False

def authentication():
    # afficher page acceuil de connexion    
    #recuperer la sortie du formulaire
    user = display_homepage()
    #vérifier que cet utilisateur existe en base
    return user_exist_control()

def display_admin_page():
    st.warning("in progress")