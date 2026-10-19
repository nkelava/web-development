#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ, mkdir, path, listdir
from sys import exit
from session import get_session_data, destroy_session
from database import get_user_role


params = FieldStorage()
request_type = environ['REQUEST_METHOD'].upper()
user_data = get_session_data()

# Stop here because the rest of the page needs a logged-in user
if (user_data is None):
    print('Location: login_page.py')
    print()
    exit()

img_dir_path = '../../../../htdocs/images'

if (not path.isdir(img_dir_path)): # otherwise it returns an error with every POST
    mkdir(img_dir_path)
 
images = listdir(img_dir_path)
success = True

if (request_type == 'POST'):
    if (params.getvalue('btn_submit') == 'Log out'):
        destroy_session()
        print('Location: login_page.py')
        print()
        exit()
    else: 
        file_item = params["image"] if ("image" in params) else None

        if (file_item is not None) and (file_item.filename):
            img_dir_path = '../../../../htdocs/images/'
            img_dir_path += path.basename(file_item.filename)
            open(img_dir_path, 'wb').write(file_item.file.read(2500000))
            success = True
        else:
            message = 'No file was uploaded'
            success = False
        
        if (success):
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
                nav {
                    border-bottom: 1px solid silver;
                }
                #nav-header {
                    text-align: left;
                    margin-left: 5%;
                    font-size: 26px;
                    color: white;
                }
                #nav-edit a {
                    float: right;
                    margin: 15px 30px 0 0;
                    font-size: 20px;
                    color: white;
                    text-decoration: none;
                }
                #nav-logout input {
                    float: right;
                    margin: 10px 70px 0 0;
                    padding: 3px 15px 7px;
                    font-size: 18px;
                    font-weight: bold;
                    color: white;
                    background: #4b7dde;
                    border: 2px solid silver;
                    border-radius: 20px;
                }
                #nav-logout input:hover, #nav-edit a:hover {
                    transform: scale(1.05,1.05);
                    text-decoration: underline;
                }
                #form-upload {
                    margin-left: 36%;
                    color: white;
                }
                #form-upload form {
                    text-align: center;
                    width: 500px;
                    margin-top: 120px;
                    padding: 10px;
                    border: 2px solid white;
                    border-radius: 5px;
                }
                .txt-upload {
                    font-size: 18px;
                }
                img {
                    margin: 30px 20px;
                    border: 1px solid silver;
                    border-radius: 5px;
                }
                img:hover {
                    transform: scale(1.05,1.05);
                }
                #image-container {
                    height: 510px;
                    margin: 80px 350px 0 350px;
                    border-bottom: 1px solid silver;
                    overflow: auto;
                }
                body, input {
                    font-family: Comic Sans MS;
                }
            </style>
        </head>
        <body>
            <nav>
                <div id="nav-logout">
                    <form method="POST">
                        <input type="submit" name="btn_submit" value="Log out">
                    </form>''')

user_role = get_user_role(user_data['user_id']).upper()

if (user_role == 'ADMIN'):
    print('''       <div id="nav-edit">
                        <a href="users_page.py">Users</a>
                    </div>''')

print('''
            </div>
                <div id="nav-header">
                    <h1>UploadFiles</h1>
                </div>
            </nav>
            <div id="form-upload">
                <form enctype="multipart/form-data" method="POST">
                    <div id="upload-container">
                        <input class="txt-upload" type="file" name="image" accept="image/*">
                        <input class="txt-upload" type="submit" name="upload" value="Upload">
                    </div>
                </form>
            </div>
            <div id="image-container">''')

for image in images:
    print(f'<img src="../../../../images/{image}" width=350 height=200 alt="{image}">')
    
if (request_type == 'POST') and (not success):
    print(f'<script>alert("Image upload failed!\\n{message}");</script>')

print('''</div>
        </body>
        </html>''')


