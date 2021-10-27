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

    username = payload.get("username")
    password = payload.get("password")

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


def edit_user() -> tuple:
    pass


def delete_user() -> tuple:
    pass


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
    elif task == "edit_user":
        return edit_user
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
