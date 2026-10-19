#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python39\python.exe

import cgi

form_data = cgi.FieldStorage()

print ('''
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
            color: #33FFD6;
        }
        form {
            padding-top: 10%;
            padding-left: 38%;
        }
        table {
            height: 600px;
            width: 600px;
            font-size: 21px;
            padding-bottom: 5%;
            color: #33FFD6;
            box-shadow: 5px 5px 18px 5px #707070;
            border-radius: 15px 50px;
            background-image: linear-gradient(#454545, #858585);
        }

        th {
            height: 100px;
            font-size: 35px;
            text-align: center;
            text-decoration: underline;
        }
        tr {
            height: 40px;
        }
        td {
            padding-left: 140px;
            text-align: right;
        }
        .rowData {
            width: 400px;
            padding: 0 20px 0 95px;
            text-align: left;
        }
        .linkContainer {
            padding-top: 20px;
            font-size: 21px;
        }
        a {
            font-weight: bold;
            color: #454545;
        }
  </style>
</head>    
<body>
    <form>
        <table>
            <tr>
                <th colspan="2" style="text-align: center">Entered data</th>
            </tr>
            <tr>
                <td>Name:</td>
                <td class="rowData">''')
print(form_data.getvalue('username'))
print('''</td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td class="rowData">''')
print(form_data.getvalue('email'))
print('''</td>
            </tr>   
            <tr>
                <td>Status:</td>
                <td class="rowData">''')
print(form_data.getvalue('status'))
print('''</td>
            </tr>
            <tr>
                <td>Spec.:</td>
                <td class="rowData">''')
print(form_data.getvalue('specialisation'))
print('''</td>
            </tr>
            <tr>
                <td>Master thesis: </td>
                <td class="rowData">''')

print('Yes' if form_data.getvalue('masters') == "Yes" else 'No')

print('''</td>
            </tr>
            <tr>
                <td>Remarks:</td>
                <td class="rowData">''')

print(form_data.getvalue('remark') if form_data.getvalue('remark') else 'No remarks')

print('''</td>
            </tr>
        </table>
        <div class="linkContainer">
         <a href="http://localhost/cgi-bin/continuation_forms/login.py">Back to start...</a>
        </div>
    </form> 
</body>
</html>''')

