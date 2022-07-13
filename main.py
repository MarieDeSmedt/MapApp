
import streamlit as st
from tools.tools import display_zoneChaudes_page

import auth.user as us
import auth.admin as admin




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
if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False
if 'role' not in st.session_state:
    st.session_state.role = "no"
if 'init_db' not in st.session_state:
    us.init_user_db()
    st.session_state.init_db = True



# authentification
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logoutSection = st.container()


def LoggedOut_Clicked():
    st.session_state.loggedIn = False

def show_logout_page():
    loginSection.empty()
    with logoutSection:
        st.button("Log Out", key="logout", on_click=LoggedOut_Clicked)

def LoggedIn_Clicked(userName,password):
    user_is_login = us.login(userName, password)
    if user_is_login:
        st.session_state.userName=st.session_state.user[0]
        st.session_state.password=st.session_state.user[1]
        st.session_state.role=st.session_state.user[2]
        st.session_state.loggedIn = True
        
    else:
        st.session_state.loggedIn = False
        st.sidebar.error('Invalid user name or password')




def show_login_page():
    with loginSection:
        if st.session_state["loggedIn"] == False:
            userName = st.text_input(label="",value="",placeholder="Enter your user name")
            password = st.text_input(label="",value="",placeholder="Enter password",type="password")
            st.button("Login", key = "login", on_click=LoggedIn_Clicked, args=(userName,password))
            


with headerSection:
    st.title("Connection")
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page()
    else:
        if st.session_state['loggedIn']:
            show_logout_page()
            if st.session_state.role == "admin":
                st.sidebar.write('user is admin')
                admin.display_admin_page()
            elif st.session_state.role =="user":
                st.sidebar.write("user is user")
                # display_zoneChaudes_page()
            else:
                st.sidebar.error('user has no role')
        else:
            show_login_page()





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
    
