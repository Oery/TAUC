# -*- coding: utf-8 -*-
import tailer
import requests
import re
import json
import os
import time
import ctypes
from colored import fg

version = "0.6"
ctypes.windll.kernel32.SetConsoleTitleW(f"TAUC v{version} | By Oery")

os.system('cls')

server_connect = [
    " [Client thread/INFO]: Connecting to ",
    " [Render thread/INFO]: Connecting to ",
    " [Client thread/INFO]: Worker done, connecting to ",
    " [Render thread/INFO]: Worker done, connecting to "
]

rp_loading = [
    " [Client thread/INFO]: [OptiFine] Resource packs: ",
    " [Render thread/INFO]: Reloading ResourceManager: ",
]

p = fg("magenta_2a")
ntext = fg("white")
text = fg("light_yellow")
error = fg("light_red")
green = fg('light_green')

def title():
    print("")
    print(p + "MMP\"\"MM\"\"YMM   db   `7MMF'   `7MF' .g8\"\"\"bgd ")
    print("P'   MM   `7  ;MM:    MM       M .dP'     `M ")
    print("     MM      ,V^MM.   MM       M dM'       ` ")
    print("     MM     ,M  `MM   MM       M MM          ")
    print("     MM     AbmmmqMA  MM       M MM.         ")
    print("     MM    A'     VML YM.     ,M `Mb.     ,' ")
    print("   .JMML..AMA.   .AMMA.`bmmmmd\"'   `\"bmmmd'  ")
    print("\n")
    print(f"{p}Version {version} | {ntext}développé par {p}Oery#0001")
    print("")


def get_api_key(client="vanilla", logs=""):
    os.system("cls")
    title()
    
    while True:
        print(f"{p}[INFO] {ntext}Veuillez indiquer votre " + fg("orange_1") + "Clé d'authentification API [RW] (Lecture / Écriture)" + ntext + "")

        API_KEY = input(f"{p}[INFO] {ntext}Vous pouvez la générer sur " + fg("light_blue") + " https://panel.wizebot.tv/development_api_management\n" + text + "")

        res = requests.get(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/get/server_ip")

        if res.status_code != 200:
            print(error + "\n[ERREUR] " + ntext + "Clé d'authentification Invalide")
            time.sleep(2)
            os.system('cls')
            title()
            continue

        print(green + "\n[SUCCÈS] "+ fg("orange_1") + "Clé d'authentification" + ntext + " Valide")
        time.sleep(2)
        break

    data = {
        "api_key": API_KEY,
        "client": client,
        "logs": logs
    }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)

    os.system('cls')
    title()
    print(f"{p}[INFO] {ntext}Paramètres sauvegardés")
    time.sleep(2)

    os.system('cls')
    title()

    
def get_mc_window():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)

        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    for x in titles:
        print(x)
        if x.startswith("Lunar Client (") and x.endswith(")"):
            ver = x.split()[-1][1:-13] if "dev" in x else x.split()[-1][1:-16]

            if  ver == "1.7.10": ver = "1.7"
            elif ver == "1.12.2": ver = "1.12"
            elif ver == "1.16.5": ver = "1.16"
            elif ver == "1.17.1": ver = "1.17"
            elif "1.18.1" in ver: ver = "1.18.1"
            elif "1.18.2" in ver: ver = "1.18.2"
            elif "1.19" in ver: ver = "1.19"
            
            if "dev" in x:
                ver = "ichor"

            return f"lunar {ver}"

        elif x.startswith("Badlion Minecraft Client v"):
            return "badlion"

        elif x.startswith("Minecraft"):
            return "vanilla"

    return None


def get_logs_from_client(client):

    if client is None:
        print(error + "\n[ERREUR] " + ntext + "Votre " + fg("orange_1") + "Client Minecraft" + ntext + " n'a pas été détecté")
        return None

    print(f"{green}[SUCCÈS] {ntext}Client détecté : " + fg("orange_1") + client.capitalize())

    if "lunar" in client:
        return f"{os.getenv('USERPROFILE')}\.lunarclient\offline\{client.split()[-1]}\logs\latest.log"

    elif client == "badlion":
        return f"{os.getenv('APPDATA')}\.minecraft\logs\blclient\minecraft\latest.log"

    elif client == "vanilla":
        return f"{os.getenv('APPDATA')}\.minecraft\logs\latest.log"

    else:
        return None


def get_logs_from_user():

    try:
        with open("config.json", 'r') as f:
            data = json.load(f)
            client = data["client"]
            logs = data["logs"]

        print(f"{p}[INFO] {ntext}Voulez vous réutilisez vos paramètres précédents ? (" + fg("orange_1") + "Oui" + ntext + "/" + fg("orange_1") + "Non" + ntext + ")")

        if client == "custom":
            res = input(f"{p}[INFO] {ntext}Logs : " + fg("orange_1") + logs + text + "\n").lower()

        else:
            res = input(f"{p}[INFO] {ntext}Client : " + fg("orange_1") + client.capitalize() + text + "\n").lower()

    except KeyError:
        res = "non"
        logs = None

    if res == 'oui':
        return get_logs_from_client(client)

    while True:
        client = input(f"{p}[INFO] {ntext}Quel client utilisez-vous ?" + fg("orange_1") + " Lunar " + ntext + "|" + fg("orange_1") + " Badlion " + ntext + "|" + fg("orange_1") + " Vanilla " + ntext + "|" + fg("orange_1") + " Custom\n" + text + "").lower()

        if client not in ["lunar", "badlion", "vanilla", "custom"]:
            print(error + "\n[ERREUR] " + ntext + "Client Invalide")
            time.sleep(2)
            os.system('cls')
            title()

        if client == "lunar":
            ver = input(f"{p}[INFO] {ntext}Quel version de Lunar utilisez-vous ?" + fg("orange_1") + " 1.7 " + ntext + "|" + fg("orange_1") + " 1.8 " + ntext + "|" + fg("orange_1") + " 1.12 " + ntext + "|" + fg("orange_1") + " 1.16 " + ntext + "|" + fg("orange_1") + " 1.17 " + ntext + "|" + fg("orange_1") + " 1.18.1 " + ntext + "|" + fg("orange_1") + " 1.18.2\n" + text + "")

            client = f"lunar {ver}"

        elif client == "custom":
            logs = input(f"{p}[INFO] {ntext}" + "Veuillez indiquer l'emplacement du latest.log de votre Client\n" + text + "")

        print(green + "\n[SUCCÈS] " + ntext + "Client selectionné")
        time.sleep(2)
        break
        
    data = {
        "api_key": API_KEY,
        "client": client,
        "logs": logs
        }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)

    if logs is None:
        return get_logs_from_client(client)
    
    return logs


def get_command(key):

    res = requests.get(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/get/{key[0]}")

    if res.status_code != 200:
        print(f"{error}[ERREUR] {ntext}Impossible d'obtenir la commande " + fg('orange_1') + key[1])

        return None

    return res.json()['val']


def edit_command(key, value):
    res = requests.post(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/set/{key[0]}/{value}")

    if res.status_code != 200:
        print(f"{error}[ERREUR] {ntext}Impossible de mettre à jour la commande " + fg('orange_1') + key[1])
        return

    print(f"{p}[INFO] {ntext}Commande " + fg('orange_1') + key[1] + ntext + " mise à jour | " + green + value)


def update_command(key, value):

    if value == get_command(key):
        print(f"{p}[INFO] {ntext}Commande " + fg('orange_1') + key[1] + ntext + " non mise à jour car la valeur était déjà bonne")
        return

    edit_command(key, value)


def parse_server_ip(line):
    server_ip = line.split()[7][:-1] if client == "badlion" else line.split()[5][:-1]

    if server_ip.endswith('.'):
        server_ip = server_ip[:-1]

    if server_ip in alias:
        server_ip = alias[server_ip]

    return server_ip


def parse_resource_packs(line):
    pack = line[60:]

    if pack == "Default":
        return 'Aucun'

    packs = pack.split(',')
    parsed_packs = []

    for pack in packs:
        pack = re.sub("[§].", "", pack)
        pack = " ".join(pack.split())

        pack = pack.removeprefix("!")
        pack = pack.removesuffix('.zip')

        if pack not in ["textures", "Default"]:
            parsed_packs.append(pack)

    return ", ".join(parsed_packs)


title()

alias = {}

if "alias.txt" in os.listdir():
    with open("alias.txt", "r", encoding='utf-8') as f:
        for line in f.readlines():

            if not line.startswith("#") and len(line) > 1:

                if line.endswith("\n"):
                    line = line[:-1]

                words = line.split()
                alias[words[0]] = line[len(words[0])+1:]

else:
    
    with open("alias.txt", "w", encoding='utf-8') as f:
        f.write("\n\n")
        f.write("# Les Alias permettent de remplacer le texte que l'app détecte par un autre texte.\n# Ils sont utiles si vous ne voulez pas leak l'IP d'un serveur privé\n# ou si l'IP d'un serveur ne correspond pas à celle rentrée dans le menu multijoueur\n\n")
        f.write("################## DEFAULT ##################\nproduction.spectrum.moonsworth.cloud lunar.gg\ntcpshield.craftok.fr craftok.fr\n_dc-srv.5aca351ce790._minecraft._tcp.hyriode.fr hyriode.fr\n\n")
        f.write("################# EXAMPLES ##################\nmc.serveur.privé Serveur Privé\nadressebadlongue.serveur.fr serveur.fr\nmc.serveur.privé mc.serveur.privé (Whitelist ON)\n\n")
        f.write("################## CUSTOM ###################\n")

    alias = {
        "production.spectrum.moonsworth.cloud": "lunar.gg",
        "tcpshield.craftok.fr": "craftok.fr",
        "_dc-srv.5aca351ce790._minecraft._tcp.hyriode.fr": "hyriode.fr"
    }

if "config.json" not in os.listdir():
    get_api_key()

with open("config.json", 'r') as f:
    data = json.load(f)
    API_KEY = data["api_key"]
    client = data["client"]
    logs = data["logs"]

res = requests.get(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/get/server_ip")

if res.status_code != 200:
    print(error + "\n[ERREUR] " + ntext + "Votre " + fg("orange_1") + "Clé d'authentification" + ntext + " est Invalide ou votre connexion Internet a un soucis")
    time.sleep(1)
    get_api_key(client, logs)
    
print(green + "\n[SUCCÈS] " + ntext + "Clé d'authentification chargée !")

client = get_mc_window()
logs = get_logs_from_client(client)

if logs is None:
    logs = get_logs_from_user()

os.system("cls")
title()

print(f"{p}[INFO] {ntext}Le script est désormais actif")

print(p + "\n[INFO] " + ntext + "Modifiez votre commande " + fg('orange_1') + "!ip" + ntext + " et remplacez l'ip par " + fg('orange_1') + "$custom_data(get, serverip)")
print(f"{p}[INFO] {ntext}Modifiez votre commande " + fg('orange_1') + "!pack" + ntext + " et remplacez le pack par " + fg('orange_1') + "$custom_data(get, pack)\n")

server_ip = ""
pack = ""

with open(logs, 'r') as f:

    for line in f.readlines():
        if any(server_log in line for server_log in server_connect):
            server_ip = parse_server_ip(line)
        
        elif any(rp in line for rp in rp_loading):
            pack = parse_resource_packs(line)

if server_ip != "":
    update_command(("server_ip", "!ip"), server_ip)

else:
    print(f"{p}[INFO] {ntext}Commande " + fg("orange_1") + "!ip" + ntext + " non mise à jour car vous n'êtes pas connecté à un serveur")

if pack != "":
    update_command(("pack", "!pack"), pack)

for line in tailer.follow(open(logs)):

    if any(server_log in line for server_log in server_connect):
        server_ip = parse_server_ip(line)
        
        update_command(("server_ip", "!ip"), server_ip)

    elif any(rp in line for rp in rp_loading):
        pack = parse_resource_packs(line)

        update_command(("pack", "!pack"), pack)