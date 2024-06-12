import os
import json
import sqlite3
from os import path
import init

#def checkfiles():

if not os.path.exists('../logs/'):
    os.makedirs('../logs/')

if not path.exists('config/config.json'):
    jsonstructure = {} # Platzhalter
    jsonstructure['discord'] = []
    wronginput = False
    print("Möchtest du das automatisierte Setup nutzen? y/n")
    input1 = input()

    if input1.lower().strip() == 'y':
        print("Bitte geben Sie den Token ein:")
        token = input()
        print("Bitte geben Sie die Pterodactyl Domain ein (Form: https://example.com/ | optional):")
        pterodactyl_domain = input()
        print("Bitte geben Sie den Pterodactyl API Key ein (optional):")
        pterodactyl_api_key = input()
        print("Bitte geben Sie die Guild ID ein:")
        guild_id = input()
        print("Bitte geben Sie die ID des Admin Channels ein:")
        guild_admin_id = input()

        jsonstructure['discord'].append({
        'token': token,
        'pterodactyl_domain': pterodactyl_domain,
        'pterodactyl_apikey': pterodactyl_api_key,
        'guild_id': guild_id,
        'guild_admin_id': guild_admin_id
        })

    elif input1.lower().strip() == 'n':

        jsonstructure['discord'].append({
        'token': 'Platzhalter',
        'pterodactyl_domain': '',
        'pterodactyl_apikey': '',
        'guild_id': '',
        'guild_admin_id': ''
        })

    else:
        wronginput = True
        print("Falsche eingabe")

    if not wronginput:
        if not os.path.exists('config'):
            os.mkdir('config')
        with open('config/config.json', 'w') as outfile:
            json.dump(jsonstructure, outfile, indent=4)
        print("Config erfolgreich erzeugt")

if not os.path.exists('whitelist/paths.txt'):
    if not os.path.exists('whitelist'):
        os.mkdir('whitelist')
    paths = open("whitelist/paths.txt", "a")
    paths.close()
    paths = open("whitelist/pterodactyl.txt", "a")
    paths.close()

if not os.path.exists('data/database.sqlite'):
    if not os.path.exists('data'):
        os.mkdir('data')
    paths = open("data/database.sqlite", "a")
    paths.close()