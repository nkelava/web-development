#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python39\python.exe

import cgi

params = cgi.FieldStorage()

print ('''
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
            padding-top: 30px;
            height: 450px;
            width: 600px;
            color: #33FFD6;
            box-shadow: 5px 5px 18px 5px #707070;
            border-radius: 15px 50px;
            background-image: linear-gradient(#454545, #858585);
        }
        tr {
            font-size: 20px;
        }
        th {
            height: 50px;
            text-align: center;
            font-size: 35px;
            text-decoration: underline;
        }
        .columnSubject {
            width: 20%;
            padding-bottom: 20%;
            font-size: 22px;
            text-align: right;
        }
        .columnTextarea {
            padding-left: 35px;
        }
        .rowNext {
            height: 50px;
            padding-top: 5%;
            text-align: center;
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
        textarea {
            width: 90%;
            height: 72%;
            margin-top: 10%;
            padding-left: 10px;
            color: #33FFD6;
            font-size: 18px;
            text-color: #33FFD;
            background-color: #606060;
            border: 1px solid black;
        }
        ::placeholder {
            font-size: 18px;
            color: #33FFD6;
        }   
    </style>
</head>    
<body>
    <form action="registration_certificate.py" method="POST">
        <table>
            <tr>
                <th colspan="2">Remark</th>
            </tr>
            <tr>
                <td class="columnSubject">Remarks:</td>
                <td class="columnTextarea">
                    <textarea name="remark" rows="6" cols="30" placeholder="e.g. Switching to a part-time study program..."></textarea>
                </td>
            </tr>
            <tr>
                <td class="rowNext" colspan="2"><input type="submit" value="Next"></td>
            </tr>
        </table>
  ''')
print ('<input type="hidden" name="username" value="' + str(params.getvalue("username")) + '">')
print ('<input type="hidden" name="email" value="' + str(params.getvalue("email")) + '">')
print ('<input type="hidden" name="status" value="' + str(params.getvalue("status")) + '">')
print ('<input type="hidden" name="specialisation" value="' + str(params.getvalue("specialisation")) + '">')
print ('<input type="hidden" name="masters" value="' + str(params.getvalue("masters")) + '">')
print ('''
    </form>
</body>
</html>''')