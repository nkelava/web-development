from subjects import subjects


def get_status(subjectKey, data):
    for element in data:                # Go through data and if a radio button was pressed, its first letter is the status key
        if (element[1:] == subjectKey):
            return element[:1]
    return 'n'                          # If no radio button was pressed for the subject, set it to 'Not selected' by default 


def check_conditions(year):
    if (year == 3): # No conditions for selection in the first two years
        # You can set enrolled or passed in the third year only if you passed the whole first year and passed second year subjects worth at least 10 ECTS 
        return True if (check_first_year() == True) and (check_second_year_ECTS() == True) else False
    return True


def check_first_year():
    for subject in subjects:    # Stop on the first subject in the first year that isn't passed
        if (subjects[subject]['year'] == 1):
            if (subjects[subject]['status'] != 'p'):
                return False
    return True


def check_second_year_ECTS():
    return False if (count_ects(2) < 10) else True    # If a student didn't get at least 10 ECTS in the second year, third year subjects are set to 'Not selected'


def update_status():
    for subject in subjects:    # In case the conditions failed, set every third year subject status to 'Not selected' because it can be neither enrolled nor passed
        if (subjects[subject]['year'] == 3):
            subjects[subject]['status'] = 'n'


def count_ects(year):
    ectsCnt = 0
    for subject in subjects:
        if (year == "all"):
            if (subjects[subject]['status'] == 'e'):
                ectsCnt += subjects[subject]['ects']
                continue
        elif (subjects[subject]['year'] != year):   # Count only subjects from the requested year
            continue
             
        if(subjects[subject]['status'] == 'p'):
            ectsCnt += subjects[subject]['ects']
    return ectsCnt


def filter_data(data):
    temp = data
    for dataKey in list(temp):
        for key in list(temp):
            if (dataKey[1:] == key[1:]) and (dataKey != key):
                del temp[dataKey]
    return temp


