from subjects import subjects


def get_status(subjectKey, data):
    for element in data:                # Go throu data and if radio button was pressed first letter will be status key
        if (element[1:] == subjectKey):
            return element[:1]
    return 'n'                          # If any subject radio button wasn't pressed set it to 'Not selected' as default 


def check_conditions(year):
    if (year == 3): # No conditions for selection in first two year
        # You can set enrolled or passed in third year only if you passed whole first year and if you passed second year subjects whose ECTS sum exceeds 10 
        return True if (check_first_year() == True) and (check_second_year_ECTS() == True) else False
    return True


def check_first_year():
    for subject in subjects:    # Update third year session data on first occurrence of not passed subject in first year
        if (subjects[subject]['year'] == 1):
            if (subjects[subject]['status'] != 'p'):
                return False
    return True


def check_second_year_ECTS():
    return False if (count_ects(2) < 10) else True    # If a student didn't get more than 10 ECTS in second year refresh session data from third year to 'Not selected'


def update_status():
    for subject in subjects:    # This is in case if conditions failed, so set every subject status to 'Not selected' because it can't be enrolled nor passed
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


