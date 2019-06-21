import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi

client.run("NTgzMTM0MTU0MjUwNjQ5NjMw.XO39rA.WunVZQti3Hz9kjgSrVpAUvDpI7o")