from conditions import get_status, check_conditions, count_ects, update_status
from subjects import subjects, year_names, status_names


def start_html(year):
    print('''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: #A1D2CE;
            }
            table {
                width: 750px;
                margin-left: 600px;
                border: 3px solid black;
                border-radius: 10px 10px 0 0;
                border-spacing: 0;
                background-color: #78CAD2;
                font-size: 18px;
            }
            tr, th, td {
                border: 1px solid black;
            }
            th, td {
                text-align: center;
                padding: 5px;
            }
            button {
                margin: 200px 5px 40px;
                height: 40px;
                width: 100px;
                border: 2px solid black;
                border-radius: 5px;
                background-color: #50858B;
                font-size: 16px;
                font-weight: bold;
            }
            button:hover {
                background-color: #62A8AC;
                transform: scale(1.1, 1.1);
            }
            #first {
                margin-left: 750px;
            }
            #yearCaption {
                height: 50px;
                font-size: 22px;
                background-color: #50858B;
            }
            #headings, #total {
                background-color: #62A8AC;
            }
            #total {
                font-size: 20px;
                font-weight: bold;
            }
            input {
                margin-left: 15px;
            }
            input[type='radio']:after, input[type='radio']:checked:after{
                width: 13px;
                height: 13px;
                border-radius: 13px;
                top: -2px;
                left: -3px;
                position: relative;
                background-color: #62A8AC;
                content: '';
                display: inline-block;
                visibility: visible;
                border: 2px solid #386369;
            }
            input[type='radio']:checked:after {
                background-color: #386369;
            }
        </style>
    </head>
    <body>
        <form action="index.py" method="POST">
            <button id="first" type="submit" name="btnYear" value="1">Year 1</button>
            <button type="submit" name="btnYear" value="2">Year 2</button>
            <button type="submit" name="btnYear" value="3">Year 3</button>
            <button type="submit" name="btnYear" value="4">Certificate</button>

            <table>
                <tr id="yearCaption">
                    <th colspan="4">%s</th>
                </tr>
                <tr id="headings">
                    <th width="300px">SUBJECTS</th>
                    <th width="100px">ECTS</th>
                    <th width="350px">STATUS</th>
                </tr>''' % year_names[year].upper())


def print_subject(subjectKey, year, data):
    name = subjects[subjectKey]['name']
    ects = str(subjects[subjectKey]['ects'])
    status = get_status(subjectKey, data)
    subjects[subjectKey]['status'] = status
    
    if (year == 4):   # When the certificate button is pressed, just list subjects and their statuses
        if (subjects[subjectKey]['year'] == 3) and (check_conditions(3) == False):
            status = 'n'    # Third year subjects can be neither enrolled nor passed if the conditions failed
            subjects[subjectKey]['status'] = status
        print_certificate(name, ects, status)
    else:
        if (year == 3) and (check_conditions(year) == False):
            update_status()   # The certificate page reads statuses from the subjects script, so they need to be updated
            status = 'n'
        
        if (subjects[subjectKey]['year'] == year):
            print_year(subjectKey, name, ects, status)


def print_year(subjectKey, name, ects, status):
    print('''<tr class="radio-toolbar">
                            <td>{0}</td>
                            <td>{1}</td>
                            <td>'''.format(name, ects))
    for statusKey in status_names:
        print_checkbox(subjectKey, statusKey, status)
    print('''                       </td>
                                </tr>''')


def print_checkbox(subjectKey, statusKey, subjectStatus):
    if (statusKey == subjectStatus):  # Compare the value with the element from session data
        print('<input type="radio" name="{0}" value="{1}" checked> {2}'.format('r'+subjectKey, subjectStatus+subjectKey, status_names[statusKey]))
    else:
        print('<input type="radio" name="{0}" value="{1}"> {2}'.format('r'+subjectKey, statusKey+subjectKey, status_names[statusKey]))


def print_ects_count():
    print('''<tr id="total">
                        <td></td>
                        <td>TOTAL</td>
                        <td>%s</td>
                    </tr>
    ''' % count_ects("all"))


def print_certificate(name, ects, status):
    print('''<tr>
                            <td>{0}</td>
                            <td>{1}</td>
                            <td>{2}</td>
                        </tr>'''.format(name, ects, status_names[status]))


def end_html():
    print('''
            </table>    
        </form>
    </body>
    </html>''')



