# DB
import sqlite3
import streamlit as st
import traceback
import sys



conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()


# CRUD functions

# ####################################  CREATE TABLE
def db_create_roletable():
	try:
		c.execute('CREATE TABLE IF NOT EXISTS role(id INTEGER PRIMARY KEY,name TEXT)')
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))

# ####################################  CREATE 

def db_add_role(name:str):
    try:
        c.execute('INSERT INTO role(name) VALUES (?)',(name,))
        conn.commit()
    except sqlite3.Error as er:
        st.write('SQLite error: %s' % (' '.join(er.args)))
        st.write("Exception class is: ", er.__class__)
        st.write('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        st.write(traceback.format_exception(exc_type, exc_value, exc_tb))

# ####################################  READ

def db_get_role_by_id(id_role:int):
	try:
		c.execute('SELECT * FROM role WHERE id="{}"'.format(id_role))
		data = c.fetchone()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
	return data


def db_get_role_by_name(name):
	try:
		c.execute('SELECT * FROM role WHERE name="{}"'.format(name))
		data = c.fetchone()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
	return data


def db_get_all_roles():
	try:
		c.execute('SELECT * FROM role')
		data = c.fetchall()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
	return data


# ####################################  UPDATE

# no need

# ####################################  DELETE

def db_delete_role(name :str):
	try:
		c.execute('DELETE FROM role WHERE name="{}" '.format(name))
		conn.commit()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
