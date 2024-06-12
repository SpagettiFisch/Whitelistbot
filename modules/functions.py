import discord
import json
import requests
import urllib
import random

from os import path
from shutil import copyfile
from discord.ext import slash

from modules import init

con, cur = init.getdb()

async def cmdhelp(ctx:slash.Context):
    embed = discord.Embed(title="Hilfe",
                          color=discord.Colour(0x15f00a))
    embed.add_field(name="/mc [Name]",
                    value="Registriere deinen Minecraft-Account")
    embed.add_field(name="/mcname",
                    value="Gibt deinen aktuellen Minecraft-Account wieder")
    await ctx.respond(embed=embed, ephemeral=True)
    return

async def cmdmc(ctx:slash.Context, name:str, client):
    mcsite = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}')
    mcinfo = mcsite.json()

    if not 'error' in mcinfo:
        mcinfo = mcsite.json()
        uuid = mcinfo['id']
        uuid = f'{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:32]}'

        result = cur.execute(f"SELECT * FROM user WHERE id = '{ctx.author.id}'")
        result = cur.fetchone()
        if result:
            cur.execute(f"UPDATE user SET mcname = '{mcinfo['name']}', uuid = '{uuid}' WHERE id = {ctx.author.id}")
            await ctx.respond(f'Dein Minecraftname **{name}** wurde erfolgreich aktualisiert.')
        else:
            cur.execute(f"INSERT INTO user VALUES ({ctx.author.id}, '{ctx.author.nick}', '{ctx.author.avatar_url}', '{mcinfo['name']}', '{uuid}', {True})")
            await ctx.respond(f'Dein Minecraftname **{name}** wurde erfolgreich hinzugefügt.')
        con.commit()
        await syncWhitelist()
    else:
        await ctx.respond(f'Der Minecraftname **{name}** existiert nicht.', ephemeral=True)

async def cmdmcname(ctx:slash.Context):
    result = cur.execute(f"SELECT * FROM user WHERE id = '{ctx.author.id}'")
    result = cur.fetchone()
    if result:
        color = random.randrange(0, 2**24)
        embed = discord.Embed(title=ctx.author,
                              color=discord.Colour(color))
        embed.add_field(name="Minecraftname:",
                        value=result[3])
        embed.set_image(url=result[2])
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        await ctx.respond('Du hast deinen Minecraftnamen noch nicht hinzugefügt. Nutze `/mc [name]` um ihn hinzuzufügen.', ephemeral=True)

async def syncWhitelist():
    results = cur.execute("SELECT mcname, uuid, iswhitelisted FROM user")
    results = cur.fetchall()
    whitelist = []

    for result in results:
        if result[2]:
            whitelist.append({
                'uuid': result[1],
                'name': result[0]
            })
    with open('whitelist/whitelist.json', 'w') as outfile:
        json.dump(whitelist, outfile, indent=2)
    
    await syncWhitelistFiles()
    await syncWhitelistPterodactyl(whitelist)

async def syncWhitelistFiles():
    paths = open('whitelist/paths.txt', 'r')
    for line in paths:
        copyfile('whitelist/whitelist.json', f'{str(line.rstrip())}whitelist.json')
    paths.close()

async def syncWhitelistPterodactyl(whitelist):
    paths = open("whitelist/pterodactyl.txt", "r")
    for line in paths:
        parts = line.split(" ")
        serverid = parts[0]
        whitelistpath = parts[1]

        await pterodactylWriteFile(serverid, whitelistpath, json.dumps(whitelist), init.config().get_pterodactyl_apikey())
    paths.close()

async def pterodactylWriteFile(serverid, path, data, apikey):
    url = f'{init.config().get_pterodactyl_domain()}api/client/servers/{serverid}/files/write?file={urllib.parse.quote(path)}'
    requests.post(url, data=data, headers={"Accept": "application/json", "Authorization": f"Bearer {apikey}"})
    print('Whitelist abgeschickt')