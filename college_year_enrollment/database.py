import mysql.connector
import json


db_conf= {"host":"localhost",
           "user":"root",
           "passwd":"",
           "database":"sessiondb"}

def get_DB_connection():
    myDB = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["database"]
    )
    return myDB

def check_if_exists():
    myDB = get_DB_connection()
    cursor = myDB.cursor()
    cursor.execute("SELECT * FROM session")
    records = cursor.fetchone()

    if records is None:
        return False
    else:
        return records[0]


def create_session():
    query = "INSERT INTO session (data) VALUES (%s)"
    values = (json.dumps({}),)
    
    myDB = get_DB_connection()
    cursor = myDB.cursor()
    
    cursor.execute(query, values)
    myDB.commit()
    return cursor.lastrowid


def get_data(session_id):
    myDB = get_DB_connection()
    cursor = myDB.cursor()
    cursor.execute("SELECT * FROM session WHERE session_id=%s", (session_id,))

    myResult = cursor.fetchone()
    if myResult is None:    # Cookie points to a session that no longer exists, start with empty data
        return session_id, {}
    return myResult[0], json.loads(myResult[1])


def replace_session(session_id, data):  # Replace- delete old first, than just replace with new data
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""REPLACE INTO session (session_id, data) VALUES (%s, %s)""", (session_id, json.dumps(data)))
    mydb.commit()
    

