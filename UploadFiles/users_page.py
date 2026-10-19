#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from session import get_session_data
from database import delete_user, get_users


params = FieldStorage()
user_data = get_session_data()

# If user doesn't have session he isn't logged in so go back to login
if (user_data is None):
    print('Location: login_page.py')
    
delete_id = params.getvalue('delete_id')

if (delete_id):
    try:
        delete_user(delete_id)
    except:
        pass

print()
print('''
      <!DOCTYPE html>
      <html>
      <head>
        <title>UploadFiles</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                background: linear-gradient(120deg, #2980b9, #8e44ad);
                overflow: hidden;
            }
            .header {
                width: 100%;
                text-align: left;
                padding: 6px 0 7px 96px;
                font-size: 19.5px;
                color: white;
                border-bottom: 1px solid silver;
            }
            .conatainer {
                padding: 50%;
            }
            table {
                margin: 200px 0 0 650px;
                width: 700px;
                color: white;
                border: 3px solid white;
                border-radius: 10px;
                border-spacing: 0;
                box-shadow: 5px 8px silver;
                font-size: 18px;
            }
            table a {
                color: white;
            }
            #username {
                font-size: 20px;
                font-weight: bold;
                color: #6285d9;
                border: 2px solid #6285d9;
                background-color: white;
            }
            th {
                height: 50px;
                font-size: 32px;
            }
            tr, th, td {
                border: 1px solid white;
            }
            th, td {
                text-align: center;
                padding: 5px;
            }
            .last-row td {
                height: 30px;
                font-size: 20px;
                font-weight: bold;
            }
            a:hover {
                color: #92b5f7;
            }
            body, .container {
                font-family: Comic Sans MS;
            }
        </style>
      </head>
      <body>
        <div class="container">
            <div class="header">
                <h1>UploadFiles</h1>
            </div>
            <table border=1>
                <tr>
                    <th colspan="3">Users</th>
                </tr>
                <tr>
                    <td id="username">USERNAME</td>
                    <td></td>
                    <td></td>
                </tr>''')

users = get_users()

for user in users:
    if (user[1] != "admin"):
        print('''
                    <tr>
                        <td>{0}</td>
                        <td><a href="edit_user_page.py?edit_id={1}">Edit</a></td>
                        <td><a href="users_page.py?delete_id={2}">Delete</a></td>
                    </tr>'''.format(user[1], user[0], user[0]))
 
print('''       <tr class="last-row">
                    <td ><a href="register_page.py">Add user</a></td>
                    <td colspan="2"><a href="upload_page.py">Go back</td>
                </tr>
            </table>
        </body>
        </html>''')


