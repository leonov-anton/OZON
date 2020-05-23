import json

filename = "username.json"
file = open(filename)
username = json.load(file)
print(f'Welcome, {username}')