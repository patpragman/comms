import requests

# fire up the app first

url = "http://127.0.0.1:5000/"
outgoing_payload = {"username": "bobs_6969420_test_test_test",
                    "password": "will_wonka_5",
                    "payload": "broken!"}


main_json = requests.post(url, json=outgoing_payload).json()
main_data = main_json['data']

# this should say there wa an error, that username doesn't exist
assert main_json["response_type"] == "error"
# in the text of the error message there should be "Username" indicating that the username wasn't found
assert "Username" in main_data['message']

# now let's check to see if a faulty password sends back a password error
outgoing_payload = {"username": "user_0",
                    "password": "1",
                    "payload": "broken!"}
main_json = requests.post(url, json=outgoing_payload).json()
main_data = main_json['data']
assert "password" in main_data['message']

print("User login fails appropriately")