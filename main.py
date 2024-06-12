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
# msg_opt = slash.Option(description="Dein Minecraft Name", , required=True)

@bot.event
async def on_ready():
    print('Bot wurde gestartet')
    return

@bot.slash_cmd(aliases=["hilfe"])
async def help(ctx:slash.Context):
    "Hilfe für alle verwendbaren Befehle"
    await functions.cmdhelp(ctx)

@bot.slash_cmd(aliases=["minecraft"], guild_id=1210285934248198244)
async def mc(ctx:slash.Context, name:slash.Option(description="Dein Minecraftname", required=True)):
    "Registriere deinen Minecraft Namen"
    await functions.cmdmc(ctx, name.strip(), bot)

@bot.slash_cmd()
async def mcname(ctx:slash.Context):
    "Gibt deinen aktuellen Minecraft Namen an"
    await functions.cmdmcname(ctx)

bot.run(token)