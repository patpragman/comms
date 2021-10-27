import requests

# fire up the app before running this

url = "http://127.0.0.1:5000/"

# now do the same thing and test to see that password ISN'T in the failue message
payload = {"task": "new_user",
            "username": "quargio",
            "password": "banderath"}

outgoing_payload = {"username": "user_0",
                    "password": "0",
                    "payload": payload}

response = requests.post(url, json=outgoing_payload).json()
main_data = response['data']
assert main_data['response_type'] == 'success'