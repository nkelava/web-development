#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from os import environ
from http import cookies
import database


def create_session():
    session_id = database.create_session()
    print(f'Set-Cookie: session_id = {session_id}')
    return session_id


def get_session_id():
    http_cookies_str = environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get('session_id').value if (get_all_cookies_object.get('session_id')) else None
    return session_id


def destroy_session_id():
    print('Set-Cookie: session_id = ""; expires = "Thu, 01 Jan 1970 00:00:00 GMT"')


def destroy_session():
    session_id = get_session_id()
    destroy_session_id()
    database.destroy_session(session_id)


def add_to_session(user_data, session_id=None):
    if (session_id is None):
        session_id = get_session_id()
    
    for key, value in user_data.items():
        user_data[key] = value
    database.replace_session(session_id, user_data)


def remove_from_session(dict):
    session_id = get_session_id()
    _, data = database.get_session(session_id)
    
    for key in dict:
        data.pop(key, None)
    database.replace_session(session_id, data)


def get_session_data():
    session_id = get_session_id()
    
    if (session_id):
        _, data = database.get_session(session_id)
    else:
        return None
    return data


