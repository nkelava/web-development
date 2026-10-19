#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import get_user_question
from errors import alert_message, alert_status
from hasher import verify_input
from database import change_user_password


params = FieldStorage()
request_method = environ['REQUEST_METHOD'].upper()
stage = params.getvalue('submit')
error_msg = None

if (request_method == 'POST'):
    user = {
        'username': params.getvalue('username'),
        'answer': params.getvalue('answer'),
        'password': params.getvalue('password'),
        'repeated_password': params.getvalue('repeated_password')
    }
    
    if(stage != None):
        stored_question, stored_answer = get_user_question(user)
        # Nested if-else statements primarily for specifying what went wrong and secondly for controlling flow
        if(stored_question):
            if(stage == 'Reset') and (verify_input(stored_answer, user['answer'].lower())):
                if(user['password'] == user['repeated_password']):
                    change_user_password(user['username'], user['password'])
                    print('Location: login_page.py')
                else:
                    error_msg = alert_status['repeated_password_doesnt_match']
            else:
                if(user['answer']):
                    error_msg = alert_status['answer_doesnt_match']
            stage = 'Next'
        else:
            error_msg = alert_status['username_doesnt_exist']
            stage = None


print ()
print ('''
       <!DOCTYPE html>
        <html>
        <head>
            <title>UploadFiles</title>
            <style>
                body {
                    height: 100vh;
                    margin: 0;
                    padding: 0;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    overflow: hidden;
                }
                .container {
                    position: absolute;
                    width: 400px;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: white;
                    border-radius: 10px;
                }
                .container h1 {
                    text-align: center;
                    padding-bottom: 20px;
                    color: #666666;
                    border-bottom: 1px solid silver;
                }
                .container form {
                    padding: 0 40px;
                    box-sizing: border-box;
                }
                form .txt-field, form .txt-field_question {
                    position: relative;
                    margin: 30px 0;
                    border-bottom: 2px solid #adadad;
                }
                .txt-field input, .txt-field_question input {
                    width: 100%;
                    height: 40px;
                    padding: 0 5px;
                    font-size: 18px;
                    color: #666666;
                    background: none;
                    border: none;
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
                    font-size: 20px;
                    color: #adadad;
                    transform: translateY(-50%);
                    pointer-events: none;
                    transition: .5s;
                }
                .txt-field_question label {
                    color: #2691d9;
                }
                .txt-field span::before {
                    position: absolute;
                    width: 0%;
                    height: 2px;
                    top: 40px;
                    left: 0;
                    background: #2691d9;
                    content: none;
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
                input[type="submit"] {
                    width: 100%;
                    height: 50px;
                    margin-bottom: 30px;
                    font-size: 20px;
                    font-weight: 700;
                    color: white;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    border: 1px solid;
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
        </head>
        <body>
            <div class="container">
                <h1>Reset password</h1>
                <form method="POST">''')

if(stage == None):
    print('''
                    <div class="txt-field">
                        <input type="text" name="username" required/>
                        <span></span>
                        <label>Username</label>
                    </div>
                    <input type="submit" name="submit" value="Next"/>
                </form>''')

if(stage == 'Next'):
    print('''
                    <div class="txt-field_question">
                        <label>Secret question?</label>
                        <input type="text" name="question" placeholder="{0}" disabled/>
                    </div>
                    <div class="txt-field">
                        <input type="text" name="answer" required/>
                        <span></span>
                        <label>Answer</label>
                    </div>
                    <div class="txt-field">
                        <input type="password" name="password" required/>
                        <span></span>
                        <label>New password</label>
                    </div>
                    <div class="txt-field">
                        <input type="password" name="repeated_password" required/>
                        <span></span>
                        <label>Repeat password</label>
                    </div>
                    <input type="submit" name="submit" value="Reset"/>
                    <input type="hidden" name="username" value="{1}"/>
                </form>'''.format(stored_question, user['username']))

if (request_method == 'POST') and (error_msg):
    print(f'<script>alert("Reset failed!\\n{alert_message[error_msg]}");</script>')

print('''
        </body>
        </html>''')


