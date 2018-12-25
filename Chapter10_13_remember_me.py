import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        answer = input("Are you " + username + "???(Enter 'yes' or 'no')")
        if answer == 'no':
            username = get_new_username()
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")


greet_user()
