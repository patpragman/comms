import requests

# fire up the app first

url = "http://127.0.0.1:5000/"
outgoing_payload = {"username": "bobs",
                    "password": "will_wonka_5",
                    "payload": "broken!"}


main_json = requests.post(url, json=outgoing_payload).json()
main_data = main_json['data']
print(main_json)
print(main_data)
