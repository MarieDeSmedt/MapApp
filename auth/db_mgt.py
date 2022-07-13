# DB
import sqlite3
import streamlit as st
import traceback
import sys



conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# Functions
def db_create_usertable():
	try:
		c.execute('CREATE TABLE IF NOT EXISTS user(userName TEXT,password TEXT, role TEXT )')
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))



def db_add_user(userName,password,role):
    try:
        c.execute('INSERT INTO user(userName,password,role) VALUES (?,?,?)',(userName,password,role))
        conn.commit()
    except sqlite3.Error as er:
        st.write('SQLite error: %s' % (' '.join(er.args)))
        st.write("Exception class is: ", er.__class__)
        st.write('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        st.write(traceback.format_exception(exc_type, exc_value, exc_tb))	



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



def db_get_user(userName,password):
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
	


def db_delete_user(userName,password):
	try:
		c.execute('DELETE FROM user WHERE userName="{}" AND password="{}"'.format(userName,password))
		conn.commit()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))
	


def db_update_user(new_userName,new_password,new_role,old_userName):
	try:
		c.execute('UPDATE user SET userName="{}", password="{}", role="{}" WHERE userName="{}" '.format(new_userName,new_password,new_role,old_userName))
		conn.commit()
	except sqlite3.Error as er:
		st.write('SQLite error: %s' % (' '.join(er.args)))
		st.write("Exception class is: ", er.__class__)
		st.write('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		st.write(traceback.format_exception(exc_type, exc_value, exc_tb))