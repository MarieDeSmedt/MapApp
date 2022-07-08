# DB
import sqlite3
import streamlit as st
import traceback
import sys



conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS user(userName TEXT,password TEXT, role TEXT )')


def add_user(userName,password,role):
    try:
        c.execute('INSERT INTO user(userName,password,role) VALUES (?,?,?)',(userName,password,role))
        conn.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
	

def get_all_users():
	c.execute('SELECT * FROM user')
	data = c.fetchall()
	return data

def get_all_users_by_role(role):
	c.execute('SELECT * FROM user WHERE role="{}"'.format(role))
	data = c.fetchall()
	return data

def get_user(userName,password):
	c.execute('SELECT * FROM user WHERE userName="{}" and password="{}"'.format(userName,password))
	data = c.fetchone()
	return data

def delete_user(userName):
	c.execute('DELETE FROM user WHERE userName="{}"'.format(userName))
	conn.commit()

    # todo update