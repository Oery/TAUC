client_secret = "a755134565457aacb5dabb7846bf3990cad28b3f94f87f6494cfabc22f97976b"
client_id = "154a0edf9e03bc865e331395d655b167"
redirect_uri = "https://developerslifefor.me"

authorization_base_url = "https://api.nightbot.tv/oauth2/authorize"
token_url = "https://api.nightbot.tv/oauth2/token"

scope = ["channel", "channel_send", "commands"]

from requests_oauthlib import OAuth2Session
nighbot = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# authorization_url, state =  nighbot.authorization_url(authorization_base_url)
# print(authorization_url)

redirect_response = "https://oui"
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(client_id, client_secret)

token = nighbot.fetch_token(token_url, auth=auth, authorization_response=redirect_response)
access_token = token['access_token']
print(access_token)

import json
with open("config.json", 'r') as f:
    data = json.load(f)
    access_token = data["nightbot_token"]

import requests
from pprint import pprint

hed = {"Authorization": f"Bearer {access_token}"}


# res = requests.get("https://api.nightbot.tv/1/channel", headers=hed)
# if res.json()['channel']['joined'] == False:
#     res = requests.post("https://api.nightbot.tv/1/channel/join", headers=hed)

# pprint(res.json())

# message = "Bonjour !!!"
res = requests.get("https://api.nightbot.tv/1/commands", headers=hed)

ip_command_id = ""
pack_command_id = ""
for command in res.json()["commands"]:
    if command["name"] == "!ip": ip_command_id = command["_id"]
    if command["name"] == "!pack": pack_command_id = command["_id"]

if ip_command_id == "":
    data = {
        "coolDown": 5,
        "message": "IP du serveur : ",
        "name": "!ip",
        "userLevel": ["everyone"] }
    res = requests.post("https://api.nightbot.tv/1/commands", headers=hed, data=data)
    ip_command_id = res.json()['command']['_id']
if pack_command_id == "":
    data = {
        "coolDown": 5,
        "message": "Pack : ",
        "name": "!pack",
        "userLevel": ["everyone"] }
    res = requests.post("https://api.nightbot.tv/1/commands", headers=hed, data=data)
    pack_command_id = res.json()['command']['_id']

# print(ip_command_id)
# print(pack_command_id)

# data = {"message": "IP du serveur : mc.hypixel.net" }
# res = requests.put(f"https://api.nightbot.tv/1/commands/{ip_command_id}", headers=hed, data=data)
# pprint(res.json())