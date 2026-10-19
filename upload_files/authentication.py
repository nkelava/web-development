from database import create_user, get_user_by_username, check_availability
from hasher import verify_input
from errors import alert_status


def register(user):
    # Continue if password and repeated password are same AND username and email are available
    availability = check_availability(user['username'], user['email'])
    password_check = True if (user['password'] == user['repeated_password']) else False

    if (password_check) and (availability == alert_status['success']):
        user_id = create_user(user)
        return availability if (user_id) else alert_status['database_error']
    return alert_status['repeated_password_doesnt_match'] if (not password_check) else availability


def authenticate(user):
    user_record = get_user_by_username(user['username'])
    # Continue if there is a user record in database AND passwords are matching
    if (user_record) and (verify_input(user_record[2], user['password'])):
        return True, user_record[0]
    else:
        return False, None


def get_user_question(user):
    user_record = get_user_by_username(user['username'])
    return (user_record[4], user_record[5]) if (user_record) else (None, None)


