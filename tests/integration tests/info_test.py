# test to see that the info page works
import requests
import json

# fire up the app first

url = "http://127.0.0.1:5000/"
main_json = requests.get(url).json()
main_data = main_json['data']
assert main_json['response_type'] == "error"  # there should be an error, because GET isn't supported
assert "data" in main_json # there should be a "data" sub dict
assert "request" in main_data["message"]

info_json = requests.get(url + "/info").json()
info_data = info_json['data']
assert "data" in info_json
assert "message" in info_data

# notify that the test is complete
print('Info and Main Page get request tests successful!')