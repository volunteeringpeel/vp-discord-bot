# pylint: disable=W0614

from bot_setup import *

@client.command()
async def updates():
    mes = "What's your role update?"
    for user in users:
        await client.send_message(discord.Object(id=user[2]),mes)