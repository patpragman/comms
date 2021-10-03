# Alex and Pat's secure comms flask app
# Alex and Pat
# 2/10/2021

"""
This is the server application that manages communicating parties across the network.

In the generalist sense, works like this:

1.  A user sends a post request containing a JSON object over SSL.
2.  That JSON Object contains a username, a password, and a payload.
3.  If that username and password check out, the payload is processed.
4.  The payload can be a message to send, creating a new user, or
    trying to access your messages.
    When the payload is processed, a response is generated and sent
    back to the sender.

Payload types:
    New User
    Edit User
    Delete User
    Send Message
    Get Sent Messages
    Receive Messages

We use Flask, the Flask Sessions Library,PassLib, the database is in SQLite.

-Pat 10/2

"""
import sqlite3

from flask import Flask  # flask apps are handled with this class
from flask import request # request handling with flask is processed in here
from process import *  # the processing of payloads happens in this file
from sql import *  # the SQL magic occurs here
from config import * # all the configuration stuff happens in here
from errors import AppError

import json

app = Flask(__name__)


@app.route('/info', methods=["POST", "GET"])
def info() -> str:
    """
    This function sends JSON object back as a string telling some information
    about the server.

    :return: json file as a string
    """
    data = {"message": "Contact Alex or Pat if you want to know how to interact with this API."}
    payload = {"response_type": "info",
               "data": data}
    return json.dumps(payload)


@app.route('/', methods=["POST", "GET"])
def process() -> str:
    """
    This method checks to see if the user authenticates then sends the payload to be processsed

    Eventually, get requests should send a message back to however sent the request.

    :return: json string
    """
    sender_ip = request.remote_addr  # this is the IP address of the person who sent the request

    # this is the standard thing to send back.
    data = {"message": ""}
    response_type = "error"  # the default is to expect something as broken


    try:
        if request.method == "POST":
            # validate password first
            data_received = request.json()  # this gets JSON sent from the client

        else:
            """
            The responses from the server send back a json file detailing the response type,
            and explaining that there was an error with the POST type
            """
            raise AppError("Bad request type.")

    except AppError as app_error:
        # catch app errors here
        data["message"] = str(app_error)
    except sqlite3.Error as sql_error:
        # catch SQL errors here
        data["message"] = str(sql_error)
    except Exception as general_error:
        # finally, generally catch everything else here
        data["message"] = str(general_error)

    # always return something...even if it's not that illuminating
    payload = {"response_type": response_type,
               "data": data}
    return json.dumps(payload)


if __name__ == '__main__':
    app.run()
