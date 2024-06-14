import discord

from modules import init
from modules import functions

from discord.ext import commands
from discord.ext import slash

#init.logger()

token = init.config().get_token()
domain = init.config().get_pterodactyl_domain()
apikey = init.config().get_pterodactyl_apikey()

bot = slash.SlashBot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print('Bot started succesfully')
    return

@bot.slash_cmd(aliases=["hilfe"])
async def help(ctx:slash.Context):
    "Hilfe für alle verwendbaren Befehle" #Help for all usable commands
    await functions.cmdhelp(ctx)

@bot.slash_cmd(aliases=["minecraft"])
async def mc(ctx:slash.Context, name:slash.Option(description="Dein Minecraftname", required=True)): #Your Minecraft name
    "Registriere deinen Minecraft Namen" #Register your Minecraft name
    await functions.cmdmc(ctx, name.strip(), bot)

@bot.slash_cmd()
async def mcname(ctx:slash.Context):
    "Gibt deinen aktuellen Minecraft Namen an" #Outputs your linked Minecraft name
    await functions.cmdmcname(ctx)

@bot.slash_cmd()
async def shutdown(ctx:slash.Context):
    "Will shutdown the bot if you are mighty enough."
    if await functions.isAdmin(ctx, bot):
        await functions.cmdshutdown(ctx, bot)

@bot.slash_cmd(guild_id=1210285934248198244)
async def allow(ctx:slash.Context, user:slash.Option(description="der zu whitelistene Nutzuer (@<Discordname>)", required=True)):
    "Fügt Spieler der Whitelist hinzu." #Add Players to whitelist
    if await functions.isMod(ctx, bot):
        await functions.cmdallow(ctx, user.strip(), bot)



bot.run(token)