#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import register
from alerts import alert_message, alert_status
from database import Sex


params = FieldStorage()
request_method = environ['REQUEST_METHOD'].upper()

if (request_method == 'POST'):
    user = {
        'username': params.getvalue('username'),
        'password': params.getvalue('password'),
        'repeated_password': params.getvalue('repeated_password'),
        'email': params.getvalue('email'),
        'question': params.getvalue('question'),
        'answer': params.getvalue('answer').lower(),
        'sex': params.getvalue('sex').upper()
    }
    
    success = register(user)
    
    if (success == alert_status['success']):
        print('Location: login_page.py')


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
                    font-size: 18px;
                }
                .txt-field input {
                    width: 100%;
                    height: 40px;
                    padding: 0 5px;
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
                    color: #adadad;
                    pointer-events: none;
                    transition: .5s;
                }
                .txt-field span::before {
                    width: 0%;
                    height: 2px;
                    position: absolute;
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
                input[type="text"], select {
                    font-size: 16px;
                }
                .select-field {
                    margin-top: 40px;
                    margin-bottom: 40px;
                    color: #adadad;
                }
                .select-field label {
                    position: absolute;
                    left: 10%;
                    transform: translateY(-100%);
                    color: #adadad;
                    transition: .5s;
                }
                select {
                    width: 100%;
                    height: 40px;
                    margin-top: 7px;
                    color: #666666;
                    border: 2px solid #adadad;
                    outline: none;
                }
                .select-field select:focus + label {
                    color: #2691d9;
                }
                input[type="submit"] {
                    width: 100%;
                    height: 50px;
                    margin-bottom: 30px;
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
        </head>''')

print('''<body>
            <div class="container">
                <h1>Register</h1>
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
                    <div class="txt-field">
                        <input type="password" name="repeated_password" required/>
                        <span></span>
                        <label>Repeat password</label>
                    </div>
                    <div class="txt-field">
                        <input type="email" name="email" required/>
                        <span></span>
                        <label>E-mail</label>
                    </div>
                    <div class="txt-field">
                        <input type="text" name="question" required/>
                        <span></span>
                        <label>Secret question?</label>
                    </div>
                    <div class="txt-field">
                        <input type="text" name="answer" required/>
                        <span></span>
                        <label>Answer</label>
                    </div>
                    <div class="select-field">
                        <select name="sex" id="sex">
                            <option value="{0}">Male</option>
                            <option value="{1}">Female</option>
                            <option value="{2}">Intersex</option>
                        </select>
                        <label>Sex</label>
                    </div>
                    <input type="submit" value="Register"/>
                </form>
            </div>'''.format(Sex.Male.value, Sex.Female.value, Sex.Intersex.value))

if (request_method == 'POST') and (success != alert_status['success']):
    print(f'<script>alert("Registration failed!\\n{alert_message[success]}");</script>')

print("""</body>
        </html>""")


