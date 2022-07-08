
import streamlit as st
from auth.db_mgt import *


def login(userName: str,password: str) -> bool:
    user = get_user(userName,password)
    st.session_state.role = "admin"
    return user

def create_new_user(userName: str,password: str) -> bool:
    user = get_user(userName,password)
    if not user:
        add_user(userName,password,"user")
        return True
    else:
        return False

def delete_user():
    return True

def view_user_by_userName():
    return True

def view_all_users():
    return True

def init_user_db():
    create_usertable()
    user = get_user("admin","admin")
    if not user:
        add_user("admin","admin",'admin')
