# DB
import sqlite3
import streamlit as st
import traceback
import sys



conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# CRUD Functions


# ######################################### CREATE TABLE

def db_create_usertable():
	try:
		c.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,userName TEXT,password TEXT, id_role INTEGER )')
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))


# ######################################### CREATE

def db_add_user(userName: str,password: str,id_role: int):
    try:
        c.execute('INSERT INTO user(userName,password,id_role) VALUES (?,?,?)',(userName,password,id_role))
        conn.commit()
    except sqlite3.Error as er:
        st.write('SQLite error: %s' % (' '.join(er.args)))
        st.write("Exception class is: ", er.__class__)
        st.write('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        st.write(traceback.format_exception(exc_type, exc_value, exc_tb))	


# ######################################### READ

def db_get_user(userName:str,password:str):
	try:
		c.execute('SELECT * FROM user WHERE userName="{}" AND password="{}"'.format(userName,password))
		data = c.fetchone()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
	return data


def db_get_all_users():
	try:
		c.execute('SELECT * FROM user')
		data = c.fetchall()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
	return data


# ######################################### UPDATE

def db_update_user(new_userName:str,new_password:str,new_idrole:int,old_userName:str):
	try:
		c.execute('UPDATE user SET userName="{}", password="{}", id_role="{}" WHERE userName="{}" '.format(new_userName,new_password,new_idrole,old_userName))
		conn.commit()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))


# ######################################### DELETE

def db_delete_user(userName:str,password:str):
	try:
		c.execute('DELETE FROM user WHERE userName="{}" AND password="{}"'.format(userName,password))
		conn.commit()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))


















	


