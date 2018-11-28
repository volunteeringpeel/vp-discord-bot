from bot_setup import client

@client.command()
async def say(arg):
    await client.say(arg)

@client.command()
async def ping():
    await client.say(":ping_pong: pong!")