import discord as Discord
from discord.ext import commands

from ciel_settings import Settings

TOKEN = Settings.CIEL_TOKEN

BOT_PREFIX = ("c>")

Ciel = commands.Bot(command_prefix=BOT_PREFIX)



@Ciel.event
async def on_ready() :
    print("Logged in as")
    print(Ciel.user.name)
    print(Ciel.user.id)
    print("------------")
    await Ciel.change_presence(game=Discord.Game(name='with Lu'))

Ciel.run(TOKEN)