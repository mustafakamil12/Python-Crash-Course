import json

username = input("What's your name? ")

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We will remember you {username} when you comeback!")
