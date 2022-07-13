
import streamlit as st
from auth.db_mgt import *


def login(userName: str,password:str) :
    user = db_get_user(userName, password)
    if not user:
        return False
    else:
        st.session_state.user = user
        return True

def create_new_user(userName: str,password: str, role: str = "user") -> bool:
    user = db_get_user(userName,password)
    if not user:
        db_add_user(userName,password,role)
        return True
    else:
        return False

def delete_user(userName,password):
    user = db_get_user(userName,password)
    if not user:
        return False
    else:
        db_delete_user(userName,password)
        return True

def view_user_by_userName(userName):
    user = db_get_user(userName)
    if not user:
        return "ce user n'existe pas"
    else:
        return user

def view_all_users():
    users = db_get_all_users()
    return users

def init_user_db():
    db_create_usertable()
    user = db_get_user("admin","admin")
    if not user:
        db_add_user("admin","admin",'admin')

def update_old_user(new_userName,new_password,new_role,old_userName):
    db_update_user(new_userName,new_password,new_role,old_userName)
