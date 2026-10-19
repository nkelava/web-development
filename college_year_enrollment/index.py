#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
import cgi
import session
import display
from subjects import subjects
from os import environ


# exec(open("create_database.py").read())    # Execute script that creates table if it doesn't exist
params = cgi.FieldStorage()

btnYear = params.getvalue('btnYear')
year = 1 if btnYear is None else int(btnYear)   # For first GET request year is None so set year to 1(1.year) as default

if environ['REQUEST_METHOD'] == 'POST':  # In case of POST add info to session if not that means it's first GET request so create session
    session_id = session.add_to_session(params)
else:
    session_id = session.get_or_create_sessionID()

display.start_html(year)
data = session.get_session_data(session_id)

for subject in subjects:
    display.print_subject(subject, year, data)
    
if (year == 4):
    display.print_ects_count()

display.end_html()


