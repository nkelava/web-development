import os
from http import cookies
from conditions import filter_data
import database


def get_or_create_sessionID():
    httpCookieStr = os.environ.get('HTTP_COOKIE', '')
    getAllCookiesObject = cookies.SimpleCookie(httpCookieStr)
    session_id = getAllCookiesObject.get("session_id").value if getAllCookiesObject.get("session_id") else None

    if session_id is None:
        session_id = database.create_session()
        cookiesObject = cookies.SimpleCookie()
        cookiesObject["session_id"] = session_id
        cookiesObject.output()  # set cookie-a in header
        print(f"Set-Cookie:session_id = {session_id};")
    return session_id


def add_to_session(params):
    session_id = get_or_create_sessionID()

    _, data = database.get_data(session_id)   # Return all data so far

    for cbox_id in params.keys():
        if (cbox_id != 'btnYear'):  # There is no need for storing current year value in data
            data[params.getvalue(cbox_id)] = data.get(cbox_id, 0) + 1

    data = filter_data(data)
    database.replace_session(session_id, data)
    return session_id


def get_session_data(session_id):
    _, data = database.get_data(session_id)
    return data


