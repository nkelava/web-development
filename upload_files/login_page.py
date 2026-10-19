#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import authenticate
from errors import alert_message, alert_status
from session import create_session, add_to_session


params = FieldStorage()
request_method = environ['REQUEST_METHOD'].upper()


if (request_method == 'POST'):
    user = {
        'username': params.getvalue('username'),
        'password': params.getvalue('password')
    }
    
    success, user_id = authenticate(user)
    error_msg = alert_status['incorrect_username_password']
    
    if (success):
        session_id = create_session()
        add_to_session({'user_id': user_id}, session_id=session_id)
        print('Location: upload_page.py')


print('''
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
                    width: 400px;
                    position: absolute;
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
                form .txt-field {
                    position: relative;
                    margin: 30px 0;
                    border-bottom: 2px solid #adadad;
                }
                .txt-field input {
                    width: 100%;
                    height: 40px;
                    padding: 0 5px;
                    font-size: 16px;
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
                    transform: translateY(-50%);
                    font-size: 16px;
                    color: #adadad;
                    pointer-events: none;
                    transition: .5s;
                }
                .txt-field span::before {
                    content: none;
                    width: 0%;
                    height: 2px;
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
                .forgot-pass-link {
                    margin: -5px 0 20px 5px;
                    color: #a6a6a6;
                    cursor: pointer;
                }
                .forgot-pass-link a {
                    color: #2691d9;
                    text-decoration: none;
                }
                .forgot-pass-link:hover {
                    text-decoration: underline;
                }
                input[type="submit"] {
                    width: 100%;
                    height: 50px;
                    font-size: 18px;
                    color: white;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    font-weight: 700;
                    border: 1px solid white;
                    border-radius: 25px;
                    cursor: pointer;
                    outline: none;
                }
                input[type="submit"]:hover {
                    border-color: #2691d9;
                    transition: .5s;
                }
                .register-link {
                    text-align: center;
                    margin: 30px 0;
                    font-size: 16px;
                    color: #666666;
                }
                .register-link a {
                    color: #2691d9;
                    text-decoration: none;
                }
                
                .register-link a:hover {
                    text-decoration: underline;
                }
                body, .container, input, a {
                    font-family: Comic Sans MS;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Login</h1>
                <form method="POST">
                    <div class="txt-field">
                        <input type="text" name="username" required/>
                        <span></span>
                        <label>Username</label>
                    </div>
                    <div class="txt-field">
                        <input type="password" name="password" required/>
                        <span></span>
                        <label>Password</label>
                    </div>
                    <div class="forgot-pass-link">
                        <a href="change_password_page.py">Forgot password?</a>
                    </div>
                    <input type="submit" value="Login"/>
                    <div class="register-link">
                        Not registered? <a href="register_page.py">Register</a>
                    </div>
                </form>
            </div>''')

if (request_method == 'POST') and (not success):
    print(f'<script>alert("Login failed!\\n{alert_message[error_msg]}");</script>')

print('''</body>
        </html>''')


