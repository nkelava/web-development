#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python39\python.exe

import cgitb
cgitb.enable(display=0, logdir="")


print  ("""
<!DOCTYPE html>
<html>
<head>
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
            padding-left: 38%;
        }
        table {
            height: 200px;
            width: 550px;
            font-size: 21px;
            text-align: left;
            color: #33FFD6;
            box-shadow: 5px 5px 18px 5px #707070;
            border-radius: 15px 50px;
            background-image: linear-gradient(#454545, #858585);
        }
        tr {
            height: 40px;
        }
        th {
            height: 100px;
            padding-bottom: 5%;
            font-size: 35px;
            text-align: center;
            text-decoration: underline;
        }
        td {
            text-align: right;
            padding-right: 2em;
        }
        input {
            height: 1.6rem;
            width: 100%;
            height: 100%;
            padding-left: 5%;
            font-size: 17px;
            color: #33FFD6;
            border: 1px solid black;
            background-color: #696969;
            border-radius: 5px;
        }
        td.rowLogin {
            height: 100px;
            padding: 10% 0 0 0;
            text-align: center;
        }
        input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active {
            -webkit-transition: "color 600s ease-out, background-color 600s ease-out";
            -webkit-transition-delay: 600s;
        }
        input[type=submit] {
            width: 8em;  
            height: 3em;
            margin-bottom: 5%;
            padding: 0;
            font-size: 0.8em;
            background-color: #606060;
            color: #33FFD6;
            border-radius: 5px;
        }
    </style>
</head>    
<body>
    <form action="student_info_form.py" method="POST">
        <table>
            <tr>
                <th colspan="2">Login</th>
            </tr>
            <tr>
                <td>Name:</td>
                <td><input type="text" name="username" value="" placeholder="Enter your name..." required></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><input name="password" type="password" placeholder="Enter your password..." required value=""></td>
            </tr>
            <tr>
                <td>Repeat password:</td>
                <td><input name="passwordR" type="password" placeholder="Enter password again..." required value=""></td>
            </tr>
            <tr>
                <td class="rowLogin"colspan="2"><input type="submit" value="Login"></td>
            </tr>
        </table>
    </form>
</body>
</html>
""")
