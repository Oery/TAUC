# -*- coding: utf-8 -*-
import tailer
import requests
import re
import json
import os
import time
import ctypes
from colored import fg
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

version = "0.5"
ctypes.windll.kernel32.SetConsoleTitleW(f"TAUC v{version} | By Oery")

os.system('cls')

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

if "config.json" in os.listdir():
    
    with open("config.json", 'r') as f:
        data = json.load(f)
        API_KEY = data["api_key"]
        client = data["client"]
        logs = data["logs"]
        bot = data["bot"]

    if bot == "wizebot": 

        res = requests.get(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/get/server_ip")
        if res.status_code == 200:
            print(green + "\n[SUCCÈS] " + ntext + "Clé d'authentification chargée !")
        else:
            print(error + "\n[ERREUR] " + ntext + "Votre " + fg("orange_1") + "Clé d'authentification" + ntext + " est Invalide ou votre connexion Internet a un soucis")
            while True:
                print("\n")
                print(f"{p}[INFO] {ntext}Veuillez indiquer votre " + fg("orange_1") + "Clé d'authentification API [RW] (Lecture / Écriture)" + ntext + ".")

                API_KEY = input(f"{p}[INFO] {ntext}Vous pouvez la générer sur " + fg("light_blue") + " https://panel.wizebot.tv/development_api_management\n" + text + "")

                res = requests.get(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/get/server_ip")
                if res.status_code == 200:
                    print(green + "\n[SUCCÈS] "+ fg("orange_1") + "Clé d'authentification" + ntext + " Valide")
                    time.sleep(2)
                    break
                print(error + "\n[ERREUR] " + ntext + "Clé d'authentification Invalide")
                time.sleep(2)
                os.system('cls')
                title()

            data = {
                "api_key": API_KEY,
                "client": client,
                "logs": logs,
                "bot": bot,
            }

            with open("config.json", "w") as f:
                json.dump(data, f, indent=4)

            os.system('cls')
            title()
            print(f"{p}[INFO] {ntext}Paramètres sauvegardés.")
            time.sleep(2)

            os.system('cls')
            title()

    

else:
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
        bot = "wizebot"
        access_token = ""
        time.sleep(2)
        break
    
    data = {
        "api_key": API_KEY,
        "client": "vanilla",
        "logs": "",
        "bot": bot,
    }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)

    os.system('cls')
    title()
    print(f"{p}[INFO] {ntext}Paramètres sauvegardés")
    time.sleep(2)

    os.system('cls')
    title()

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

client = ""
for x in titles:
    if x.startswith("Lunar Client (") and x.endswith(")"):
        print(x)

        ver = x.split()[-1][1:-13] if "dev" in x else x.split()[-1][1:-16]

        if  ver == "1.7.10": ver = "1.7"
        elif ver == "1.12.2": ver = "1.12"
        elif ver == "1.16.5": ver = "1.16"
        elif ver == "1.17.1": ver = "1.17"
        elif "1.18.1" in ver: ver = "1.18.1"
        elif "1.18.2" in ver: ver = "1.18.2"
        elif "1.19" in ver: ver = "1.19"
        client = f"lunar {ver}"

        if "dev" in x:
            ver = "ichor"

    elif x.startswith("Badlion Minecraft Client v"): client = "badlion"
    elif x.startswith("Minecraft"): client = "vanilla"

if client == "":
    print(error + "\n[ERREUR] " + ntext + "Votre " + fg("orange_1") + "Client Minecraft" + ntext + " n'a pas été détecté")
    logs = ""

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

    if res == "oui":
        pass
    elif res == "non":
        while True:
            client = input(f"{p}[INFO] {ntext}Quel client utilisez-vous ?" + fg("orange_1") + " Lunar " + ntext + "|" + fg("orange_1") + " Badlion " + ntext + "|" + fg("orange_1") + " Vanilla " + ntext + "|" + fg("orange_1") + " Custom\n" + text + "").lower()

            if client in ["lunar", "badlion", "vanilla", "custom"]:
                if client == "lunar":
                    ver = input(f"{p}[INFO] {ntext}Quel version de Lunar utilisez-vous ?" + fg("orange_1") + " 1.7 " + ntext + "|" + fg("orange_1") + " 1.8 " + ntext + "|" + fg("orange_1") + " 1.12 " + ntext + "|" + fg("orange_1") + " 1.16 " + ntext + "|" + fg("orange_1") + " 1.17 " + ntext + "|" + fg("orange_1") + " 1.18.1 " + ntext + "|" + fg("orange_1") + " 1.18.2\n" + text + "")

                    client = f"lunar {ver}"
                elif client == "custom":
                    logs = input(f"{p}[INFO] {ntext}" + "Veuillez indiquer l'emplacement du latest.log de votre Client\n" + text + "")

                print(green + "\n[SUCCÈS] " + ntext + "Client selectionné")
                time.sleep(2)
                break
            print(error + "\n[ERREUR] " + ntext + "Client Invalide")
            time.sleep(2)
            os.system('cls')
            title()

        data = {
            "api_key": API_KEY,
            "client": client,
            "logs": logs
            }

        with open("config.json", "w") as f:
            json.dump(data, f, indent=4)


os.system("cls")
title()

print(f"{green}[SUCCÈS] {ntext}Client détecté : " + fg("orange_1") + client.capitalize())
if client == 'lunar 1.19':
    print(error + "\n[ERREUR] " + ntext + "La version " + fg("orange_1") + "1.19" + ntext + " de Lunar Client n'est pas encore supportée et peut ne pas fonctionner correctement.")

print(f"{p}[INFO] {ntext}Le script est désormais actif")
if bot == "wizebot":
    print(p + "\n[INFO] " + ntext + "Modifiez votre commande " + fg('orange_1') + "!ip" + ntext + " et remplacez l'ip par " + fg('orange_1') + "$custom_data(get, serverip)")
    print(f"{p}[INFO] {ntext}Modifiez votre commande " + fg('orange_1') + "!pack" + ntext + " et remplacez le pack par " + fg('orange_1') + "$custom_data(get, pack)\n")

else:
    print(p + "\n[INFO] " + ntext + "Pour modifier les commandes Nightbot, ouvrez le fichier " + fg('orange_1') + "config.json" + ntext + " et :")
    print(f"{p}[INFO] {ntext}Modifiez la valeur de " + fg('orange_1') + "nighbot_ip_msg" + ntext + " pour changer le début de la commande " + fg('orange_1') + "!ip")

    print(f"{p}[INFO] {ntext}Modifiez la valeur de " + fg('orange_1') + "nighbot_pack_msg" + ntext + " pour changer le début de la commande" + fg('orange_1') + "!pack\n")


if "lunar" in client:
    ver = client.split()[-1]
    logs = os.getenv('USERPROFILE') + f"\.lunarclient\offline\{ver}\logs\latest.log"
elif client == "badlion": logs = os.getenv('APPDATA') + r"\.minecraft\logs\blclient\minecraft\latest.log"
elif client == "vanilla": logs = os.getenv('APPDATA') + "\.minecraft\logs\latest.log"

def update_command(key, value):
    if key == "server_ip": command = fg("orange_1") + "!ip"
    else: command = fg("orange_1") + "!pack"

    res = requests.get(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/get/{key}")

    if res.status_code == 200:
        old_value = res.json()['val']
        if value != old_value:
            res = requests.post(f"https://wapi.wizebot.tv/api/custom-data/{API_KEY}/set/{key}/{value}")
            if res.status_code == 200:
                print(f"{p}[INFO] {ntext}" + f"Commande {command}" + ntext + " mise à jour | " + fg("light_red") + old_value + ntext + " -> " + green + value)

            else:
                print(f"{error}[ERREUR] {ntext}" + f"Impossible de mettre à jour la commande {command}")

        else:
            print(f"{p}[INFO] {ntext}" + f"Commande {command}" + ntext + " non mise à jour car la valeur était déjà bonne")


    else: 
        print(f"{error}[ERREUR] {ntext}" + f"Impossible d'obtenir la commande {command}")

server_ip = ""
pack = ""
with open(logs, 'r') as f:
    for line in f.readlines():
        if (" [Client thread/INFO]: Connecting to " in line or " [Render thread/INFO]: Connecting to " in line) and client != "badlion":
            server_ip = line.split()[5][:-1]
            if server_ip.endswith('.'): server_ip = server_ip[:-1]
            if server_ip in alias: server_ip = alias[server_ip]
        elif (" [Client thread/INFO]: Worker done, connecting to " in line or " [Render thread/INFO]: Worker done, connecting to " in line) and client == "badlion":
            server_ip = line.split()[7][:-1]
            if server_ip.endswith('.'): server_ip = server_ip[:-1]
            if server_ip in alias: server_ip = alias[server_ip]
        elif " [Client thread/INFO]: [OptiFine] Resource packs: " in line or " [Render thread/INFO]: Reloading ResourceManager: " in line:
            pack = line[60:]
            if pack != "Default":
                packs = pack.split(',')
                parsed_packs = []
                for pack in packs:
                    pack = re.sub("[§].", "", pack)
                    pack = " ".join(pack.split())

                    pack = pack.removeprefix("!")
                    pack = pack.removesuffix('.zip')

                    if pack not in ["textures", "Default"]:
                        parsed_packs.append(pack)
                pack = ", ".join(parsed_packs)

if server_ip != "": update_command("server_ip", server_ip)
else: print(p + "[INFO] " + ntext + f"Commande " + fg("orange_1") + "!ip" + ntext + " non mise à jour car vous n'êtes pas connecté à un serveur")
if pack != "": update_command("pack", pack)

for line in tailer.follow(open(logs)):
    if (" [Client thread/INFO]: Connecting to " in line or " [Render thread/INFO]: Connecting to " in line) and client != "badlion":
        server_ip = line.split()[5][:-1]
        if server_ip.endswith('.'): server_ip = server_ip[:-1]
        if server_ip in alias: server_ip = alias[server_ip]
        update_command("server_ip", server_ip)
    elif (" [Client thread/INFO]: Worker done, connecting to " in line or " [Render thread/INFO]: Worker done, connecting to " in line) and client == "badlion":
        server_ip = line.split()[7][:-1]
        if server_ip.endswith('.'): server_ip = server_ip[:-1]
        if server_ip in alias: server_ip = alias[server_ip]
        update_command("server_ip", server_ip)

    elif " [Client thread/INFO]: [OptiFine] Resource packs: " in line or " [Render thread/INFO]: Reloading ResourceManager: " in line:
        pack = line[60:]
        if pack != "Default":
            packs = pack.split(',')
            parsed_packs = []
            for pack in packs:
                pack = re.sub("[§].", "", pack)
                pack = " ".join(pack.split())

                pack = pack.removeprefix("!")
                pack = pack.removesuffix('.zip')

                if pack not in ["textures", "Default"]:
                    parsed_packs.append(pack)
            pack = ", ".join(parsed_packs)
        update_command("pack", pack)

