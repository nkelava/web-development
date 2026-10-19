#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from session import get_session_data
from database import get_user_role, update_user, get_user_by_id, Sex


params = FieldStorage()
request_method = environ['REQUEST_METHOD'].upper()
loggedin_user_data = get_session_data()

# If user doesn't have session he isn't logged in so go back to login 
# (in case unlogged person tries to access page via URL) 
if (loggedin_user_data is None): 
    print ('Location: login_page.py')
else:
	loggedin_user_id = loggedin_user_data['user_id']
	loggedin_user_role = get_user_role(loggedin_user_id).upper()
 
	if (loggedin_user_role != 'ADMIN'):
		print('Location: login_page.py')
	else:
		edit_id = params.getvalue('edit_id')
        
if (request_method == 'POST'):
    user = {
        'user_id': params.getvalue('edit_id'),
        'username': params.getvalue('username'),
        'sex': params.getvalue('sex'),
        'role_id': 1 if (params.getvalue('role') == 'USER') else 0
    }
    update_user(user)
    print("Location: users_page.py")


print ()
print('''
        <!DOCTYPE html>
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
                    padding: 6px 0 7px 96px;
                    text-align: left;
                    font-size: 19.5px;
                    color: white;
                    border-bottom: 1px solid silver;
                }
                .container {
                    width: 400px;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: white;
                    border-radius: 10px;
                }
                .container h1 {
                    padding-bottom: 20px;
                    text-align: center;
                    font-size: 36px;
                    color: #666666;
                    border-bottom: 1px solid silver;
                }
                .container form {
                    padding: 0 40px;
                    box-sizing: border-box;
                }
                form .txt-field {
                    position: relative;
                    margin: 30px 0;
                    border-bottom: 2px solid #adadad;
                }
                form .txt-field, .select-field, input[type="submit"] {
                    font-size: 19px;
                }
                .txt-field input {
                    width: 100%;
                    height: 40px;
                    padding: 0 5px;
                    color: #666666;
                    border: none;
                    background: none;
                    outline: none;
                }
                input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active {
                    -webkit-transition: "color 600s ease-out, background-color 600s ease-out";
                    -webkit-transition-delay: 600s;
                }
                .txt-field label {
                    position: absolute;
                    top: 50%;
                    left: 5px;
                    color: #adadad;
                    transform: translateY(-50%);
                    pointer-events: none;
                    transition: .5s;
                }
                .txt-field span::before {
                    width: 0%;
                    height: 2px;
                    content: none;
                    position: absolute;
                    top: 40px;
                    left: 0;
                    background: #2691d9;
                    transition: .5s;
                }
                .txt-field input:focus ~ label,
                .txt-field input:valid ~ label {
                    top: -5px;
                    color: #2691d9;
                }
                .txt-field input:focus ~ span::before,
                .txt-field input:valid ~ span::before {
                    width: 100%;
                }
                input[type="text"], select {
                    font-size: 17px;
                }
                .select-field {
                    margin-top: 40px;
                    margin-bottom: 40px;
                    color: #adadad;
                }
                .select-field label {
                    position: absolute;
                    left: 10%;
                    color: #adadad;
                    transform: translateY(-100%);
                    transition: .5s;
                }
                select {
                    width: 100%;
                    height: 40px;
                    margin-top: 7px;
                    color: #666666;
                    border: 2px solid #adadad;
                    border-radius: 5px;
                }
                .select-field select:focus + label {
                    color: #2691d9;
                }
                input[type="submit"] {
                    width: 100%;
                    height: 50px;
                    margin-bottom: 30px;
                    color: white;
                    font-weight: 700;
                    border: 1px solid;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    border-radius: 25px;
                    cursor: pointer;
                    outline: none;
                }
                input[type="submit"]:hover {
                    border-color: #2691d9;
                    transition: .5s;
                }
                body, .container, input, select {
                    font-family: Comic Sans MS;
                }
            </style>
        </head>''')

edit_user_data = get_user_by_id(edit_id)
edit_user_info = {
    'username': edit_user_data[1],
    'sex': edit_user_data[6],
    'role': get_user_role(edit_id)
}
other_role = 'USER' if (edit_user_info['role'].upper() == 'ADMIN') else 'ADMIN'

print('''
        <body>
            <div class="header">
                <h1>UploadFiles</h1>
            </div>
            <div class="container">
                <h1>Edit user</h1>
                <form method="POST">
                    <div class="txt-field">
                            <input type="text" name="username" value="{0}">
                            <span></span>
                            <label>Username</label>
                        </div>
                    <div class="select-field">
                        <select name="sex" id="sex">
                            <option value="{1}">{2}</option>'''.format(edit_user_info['username'], edit_user_info['sex'], Sex(edit_user_info['sex']).name))

for sex in Sex:
    if sex.value != edit_user_info['sex']:
        print(f'<option value="{sex.value}">{sex.name}</option>')

print('''               </select>
                        <label>Sex</label>
                    </div>
                    <div class="select-field">
                        <select name="role" id="role">
                            <option value="{0}">{0}</option>
                            <option value="{1}">{1}</option>
                        </select>
                        <label>Role</label>   
                    </div>
                    <input type="submit" value="Edit">
                </form>
            </div>
        </body>
        </html>'''.format(edit_user_info['role'], other_role))


