from discord.ext.commands import Bot
import random

BOT_PREFIX = ("c>", ">>", "!")
TOKEN = "NDcwOTIzMTk4NDMxNzU2Mjg4.Djda3g.K5-v_gdsG5df6B8GlVj1U8X9_4g"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name="8ball")
async def eight_ball() :
    possible_responses = [
        "That is a no from me.",
        "Not very likely.",
        "It's too hard to tell."
        "It's quite possible.",
        "Definitely."
    ]
    await client.say(random.choice(possible_responses))

client.run(TOKEN)