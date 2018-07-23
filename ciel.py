from discord.ext.commands import Bot
import random

BOT_PREFIX = ("c>", ">>", "!")
TOKEN = "NDcwOTIzMTk4NDMxNzU2Mjg4.Djda3g.K5-v_gdsG5df6B8GlVj1U8X9_4g"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name="8ball", description="Answers a yes/no question", brief="Answers from the beyond (demo)", aliases=["eight_ball", "eightball", "8-ball"], pass_context=True)
async def eight_ball(context) :
    possible_responses = [
        "That is a no from me",
        "Not very likely",
        "It's too hard to tell"
        "It's quite possible",
        "Definitely"
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number) :
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_ready() :
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------------")

client.run(TOKEN)
