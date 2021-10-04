import requests

# fire up the app before running this

url = "http://127.0.0.1:5000/"

# now do the same thing and test to see that password ISN'T in the failue message
outgoing_payload = {"username": "user_0",
                    "password": "0",
                    "payload": {"broken!": "yup"}}
main_json = requests.post(url, json=outgoing_payload).json()
main_data = main_json['data']
assert "Payload does not have a type" in main_data['message']  # if you don't specify a type it should send an error.

test_loads = ["new_user", "edit_user", "delete_user", "send_message","get_messages", "receive_messages"]
for test_load in test_loads:
    outgoing_payload['payload'] = {"task": test_load}
    return_json = requests.post(url, json=outgoing_payload).json()
    assert return_json['response_type'] is not 'error'