#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
import mysql.connector
import json
from hasher import hash_string
from alerts import alert_status
from enum import Enum


class Sex(Enum):
    Male = 'M'
    Female = 'F'
    Intersex = 'I'


db_conf = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'database': 'authentication'
}


def get_database_connection():
    mydb = mysql.connector.connect(
        host=db_conf['host'],
        user=db_conf['user'],
        passwd=db_conf['passwd'],
        database=db_conf['database']
    )
    return mydb


def create_user(user):
    hashed_password = hash_string(user['password'])
    hashed_answer = hash_string(user['answer'].lower())

    try:
        mydb = get_database_connection()
        cursor = mydb.cursor()
        cursor.execute('''INSERT INTO users (username, password, email, question, answer, sex) VALUES (%s, %s, %s, %s, %s, %s)''', (user['username'], 
                                                                                                                                    hashed_password, 
                                                                                                                                    user['email'], 
                                                                                                                                    user['question'], 
                                                                                                                                    hashed_answer,
                                                                                                                                    user['sex']))
        mydb.commit()
    except:
        return None
    return cursor.lastrowid


def get_user_by_id(user_id):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id=%s', (user_id,))
    myresult = cursor.fetchone()
    return myresult


def get_users():
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users')
    myresult = cursor.fetchall()
    return myresult


def get_user_by_username(username):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users WHERE username=%s', (username,))
    myresult = cursor.fetchone()
    return myresult


def get_user_role(user_id):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT roles.role FROM roles JOIN users ON users.role_id=roles.role_id WHERE users.user_id = %s', (user_id,))
    myresult = cursor.fetchone()
    return myresult[0]


def delete_user(user_id):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('DELETE FROM users WHERE user_id=%s', (user_id,))
    mydb.commit()


def update_user(user):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('UPDATE users SET username=%s, sex=%s, role_id=%s WHERE user_id=%s', (user['username'], user['sex'], user['role_id'], user['user_id']))
    mydb.commit()


def get_role(role_id):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM roles WHERE role_id=%s', (role_id,))
    myresult = cursor.fetchone()
    return myresult


def check_availability(username, email):
    try:
        mydb = get_database_connection()
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s', (username,))
        username_result = cursor.fetchone()
        cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
        email_result = cursor.fetchone()
        mydb.close()
    except:
        mydb.close()
        return alert_status['database_error']
    
    if (not username_result) and (not email_result):
        return alert_status['success']
    elif (username_result):
        return alert_status['username_exists']
    else:
        return alert_status['email_exists']


def change_user_password(username, password):
    hashed_password = hash_string(password)
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('UPDATE users SET password=%s WHERE username=%s', (hashed_password, username))
    mydb.commit()
    mydb.close()


def create_session():
    query = 'INSERT INTO sessions (data) VALUES (%s)'
    values = (json.dumps({}),)
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid


def get_session(session_id):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM sessions WHERE session_id=%s', (session_id,))
    myresult = cursor.fetchone()
    
    if (myresult is None):
        return None, None
    return myresult[0], json.loads(myresult[1])


def destroy_session(session_id):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute('DELETE FROM sessions WHERE session_id=%s', (session_id,))
    mydb.commit()


def replace_session(session_id, data): # Replace-delete first, then insert (delete/insert)
    query = 'REPLACE INTO sessions(session_id, data) VALUES (%s, %s)'
    values = (session_id, json.dumps(data))
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()


