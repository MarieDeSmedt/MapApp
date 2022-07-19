
import streamlit as st
from auth.user_db_mgt import *


def init_user_db():
    """
    If the user table doesn't exist, create it. If the admin user doesn't exist, create it
    """
    db_create_usertable()
    user = db_get_user("admin","admin")
    if not user:
        db_add_user("admin","admin",1)


def login(username: str,password:str) :
    """
    It takes a username and password, checks if the user exists in the database, and if so, sets the
    user in the session state
    :param username: str - The username of the user
    :type username: str
    :param password: str
    :type password: str
    :return: a boolean.
    """
    user = db_get_user(username, password)
    if not user:
        return False
    else:
        st.session_state.user = user
        return True


def create_new_user(username: str,password: str, id_role: int = 1) -> bool:
    """
    This function creates a new user if the user doesn't already exist
    
    :param username: str = username
    :type username: str
    :param password: str = 'password'
    :type password: str
    :param id_role: 1 = admin, 2 = user, defaults to 1
    :type id_role: int (optional)
    :return: A boolean value.
    """
    user = db_get_user(username,password)
    if not user:
        db_add_user(username,password,id_role)
        return True
    else:
        return False


def view_all_users():
    """
    It returns all users from the database
    :return: A list of dictionaries.
    """
    users = db_get_all_users()
    return users


def update_old_user(new_username,new_password,new_idrole,old_username):
    """
    It updates the user with the new username, password, and idrole, where the old username is the old
    username
    
    :param new_username: the new username
    :param new_password: the new password
    :param new_idrole: 1
    :param old_username: the username of the user you want to update
    """
    db_update_user(new_username,new_password,new_idrole,old_username)



def delete_user(username,password):
    """
    If the user exists, delete them
    
    :param username: The username of the user to delete
    :param password: The password of the user to delete
    :return: The return value is a boolean.
    """
    user = db_get_user(username,password)
    if not user:
        return False
    else:
        db_delete_user(username,password)
        return True