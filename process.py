# Process Payloads here
# this is the "ore refinery"
# Alex and Pat

"""
json objects get parsed in the app.py file then if it authenticates,
the "payload" is sent as an object to methods and classes in this
file.
"""
import config
import errors
import sql

from config import Config
from sql import execute_sql


# functions to process various tasks of the app
def new_user(payload: dict) -> tuple:
    """
    This runs the script to add a new user to the database.

    :param payload: takes a payload dictionary formatting like the following example:
                    {"task": "new_user",
                     "username": "example",
                     "password": "a_pass"}

    :return: a tuple of a string with the status and a dictionary containing the data
            to go back to the user.
    """

    # as an example
    # data = {"response_type": "success - but shitty success"}
    # return "New User is not implemented", data

    password_hash = Config.pwd_context.hash  # use this as your hash function

    # Alex, you can do this with the .get() method...or you can reference it directly
    username = payload.get("username")
    password = password_hash(payload.get("password"))

    """
    You are free to do either one.  It's up to you.
    
    username = payload['username']
    password = hash(payload['password'])"""

    data = (username, password)

    # sql thing sending stuff out I think. Can i even test this?

    execute_sql(config.DatabaseConfig.add_user_sql, data)

    result = sql.check_user(username)
    if result:
        return_data = {"response_type": "success",
                       "message": f"Added the user {username} to the database."}

        exit_status = ("Success!  Created a New User", return_data)
    else:
        return_data = {"response_type": "failure",
                       "message": f"Failed to add the user {username} to the database."}

        exit_status = ("Uh-oh, we couldn't verify that the user was added", return_data)

    return exit_status


def edit_password(user: str) -> tuple:
    password_hash = Config.pwd_context.hash
    try1 = input("Enter the new password: ")
    try2 = input("Verify the new password: ")
    if try1 == try2:
        newPassword = password_hash(try1)
        sql.update_password(user, newPassword)
        return_data = {"response_type": "success",
                       "message": f"updated the password for {user}."}
        exit_status = ("Success!  Password has been updated", return_data)

    else:
        print("Those passwords don't match")
        return_data = {"response_type": "failure",
                       "message": f"Failed to update the password for {user}."}
        exit_status = ("Password update failed due to unmatched password inputs", return_data)

    return exit_status


def delete_user(user: str) -> tuple:
    ans = input("Are you SURE you want to delete this user? (y/n)")
    if ans == 'y' or ans == 'Y':
        sql.delete_user(user)
        return_data = {"response_type": "success",
                       "message": f"The user {user} was removed from the database."}
        exit_status = ("Success!  User deleted", return_data)
    else:
        print("Aborting operation")
        return_data = {"response_type": "failure",
                       "message": f"Operation was aborted by user."}
        exit_status = ("Operation was aborted by user", return_data)

    return exit_status


def send_message() -> tuple:
    pass


def get_sent_messages() -> tuple:
    pass


def receive_messages() -> tuple:
    pass


# process the payloads
def process_payload(payload: dict) -> callable:
    """
    This function takes the payload from the app.  Determines which function
    to send back, then returns that function.
    :param payload:
    :return: function one of the functions above
    """
    if "task" in payload:
        task = payload["task"]
    else:
        raise errors.AppError("Payload does not have a type.")

    """ 
    Acceptable Payload Types:
        new_user
        edit_user
        delete_user
        send_message
        get_messages
        receive_messages
    """

    # for some reason a hash table did not work.  Got the following error:
    # 'un-hashable type: 'dict', so let's just use if statements

    if task == "new_user":
        return new_user
    elif task == "edit_password":
        return edit_password
    elif task == "delete_user":
        return delete_user
    elif task == "send_message":
        return send_message
    elif task == "get_messages":
        return get_sent_messages
    elif task == "receive_messages":
        return receive_messages
    else:
        raise errors.AppError("Invalid API task.")
