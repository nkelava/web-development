#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python39\python.exe

import cgi

params = cgi.FieldStorage()

def form():
    print('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    background-image: url(https://webgradients.com/public/webgradients_png/035%20Itmeo%20Branding.png);
                    background-repeat: no-repeat;
                    background-size: cover;
                }
                form {
                    padding-top: 10%;
                    padding-left: 35%;
                }
                table {
                    height: 550px;
                    width: 650px;
                    color: #33FFD6;
                    box-shadow: 5px 5px 18px 5px #707070;
                    border-radius: 15px 50px;
                    background-image: linear-gradient(#454545, #858585);
                }
                tr {
                    height: 40px;
                    font-size: 20px;
                }
                th {
                    height: 100px;
                    padding: 1.2rem;
                    text-align: center;
                    font-size: 35px;
                    text-decoration: underline;
                }
                input, select {
                    height: 90%;
                    color: #33FFD6;
                    border: 1px solid black;
                    background-color: #696969;
                    border-radius: 5px;
                }
                .rowSubject {
                    width: 34%;
                    font-size: 22px;
                    text-align: right;
                }
                .rowAnswer {
                    padding-left: 35px;
                    padding-right: 15px;
                }
                .rowNext {
                    padding-top: 5%;
                    height: 100px;
                    text-align: center;
                }
                .regular {
                    margin-right: 35px;
                }
                input[type=radio] {
                    height: 15px;
                    width: 20px;
                }
                input[type=email], select {
                    width: 70%;
                    padding-left: 10px;
                    font-size: 18px;
                }
                select {
                    width: 74%;
                }
                input[type=checkbox] {
                    height: auto;
                    margin-top: 8px;
                    transform: scale(1.5);
                }
                input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active {
                    -webkit-transition: "color 600s ease-out, background-color 600s ease-out";
                    -webkit-transition-delay: 600s;
                }
                input[type=submit] {
                    width: 8em;  
                    height: 3em;
                    margin-bottom: 5%;
                    font-size: 0.9em;
                    background-color: #606060;
                    color: #33FFD6;
                    border-radius: 10px;
                }
                ::placeholder {
                    font-size: 17px;
                    color: #33FFD6;
                }   
            </style>
        </head>    
        <body>
        <form action="remark.py" method="POST">
            <table>
                <tr>
                    <th colspan="2">Fill in the form</th>
                </tr>
                <tr>
                    <td class="rowSubject">Status:</td>
                    <td class="rowAnswer">
                        <input type="radio" name="status" value="Full-time" checked>
                        <label class="regular">Full-time</label>
                        <input type="radio" name="status" value="Part-time">
                        <label>Part-time</label>
                    </td>
                </tr>
                <tr>
                    <td class="rowSubject">E-mail:</td>
                    <td class="rowAnswer"><input type="email" name="email" value="" placeholder="Enter your e-mail..." required></td>
                </tr>
                <tr>
                    <td class="rowSubject">Specialisation:</td>
                    <td class="rowAnswer">
                        <select name="specialisation">
                            <option value="Baze podataka">Baze podataka</option>
                            <option value="Programiranje">Programiranje</option>
                            <option value="Informacijski sustavi">Informacijski sustavi</option>
                            <option value="Racunalne mreze">Racunalne mreze</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td class="rowSubject">Master's thesis:</td>
                    <td class="rowAnswer"><input type="checkbox" name="masters" value="Yes"></td>
                </tr>
                <tr>
                    <td class="rowNext" colspan="2"><input type="submit" value="Next"></td>
                </tr>
            </table>
          <br><br>''')
    print('<input type="hidden" name="username" value="' + str(params.getvalue("username")) + '">')
    print('<input type="hidden" name="password" value="' + str(params.getvalue("password")) + '">')
    print('<input type="hidden" name="passwordR" value="' + str(params.getvalue("passwordR")) + '">')
    print('''
        <br>
        </form>

        </body>
        </html>''')


def login():
    print("""
        <!DOCTYPE html>
        <html>
        <head>
         <meta http-equiv="refresh" content="0;url=login.py" /> 
        </head>
        <body>
        </body>
    </html>
    """)


if params.getvalue('password') and params.getvalue('password') == params.getvalue('passwordR'):
    form()
else:
    login()



