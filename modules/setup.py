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
    print("Do you want to use the automated setup? Y/n")
    input1 = input()

    if input1.lower().strip() == 'y':
        print("Please insert your token:")
        token = input()
        print("Please insert your pterodactyl domain here (Format: https://example.com/ | optional):")
        pterodactyl_domain = input()
        print("Please insert your pterodactyl API key (optional):")
        pterodactyl_api_key = input()
        print("Please state how many moderator roles you are using (Roles which are able to modify the whitelist or user):")
        mod_count = input()
        mod_roles = []
        print("Please insert the id of every moderating role:")
        for i in mod_count:
            mod_roles.append(input())
        print("Please state how many admin roles you are using (Roles which are able to stop the bot):")
        admin_count = input()
        admin_roles = []
        print("Please insert the id of every admin role:")
        for i in admin_count:
            admin_roles.append(input())

        jsonstructure['discord'].append({
        'token': token,
        'pterodactyl_domain': pterodactyl_domain,
        'pterodactyl_apikey': pterodactyl_api_key,
        'mod_roles': mod_roles,
        'admin_roles': admin_roles
        })

    elif input1.lower().strip() == 'n':

        jsonstructure['discord'].append({
        'token': 'Platzhalter',
        'pterodactyl_domain': '',
        'pterodactyl_apikey': '',
        'mod_roles': [],
        'admin_roles': []
        })

    else:
        wronginput = True
        print("Falsche eingabe")

    if not wronginput:
        if not os.path.exists('config'):
            os.mkdir('config')
        with open('config/config.json', 'w') as outfile:
            json.dump(jsonstructure, outfile, indent=4)
        print("Config created succesfully")

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