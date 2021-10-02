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


from flask import Flask
from process import *  # the processing of payloads happens in this file
from sql import *  # the SQL magic occurs here
from config import * # all the configuration stuff happens in here
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
    return json.dumps("Skeleton, nothing yet.")


if __name__ == '__main__':
    app.run()
