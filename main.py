# VP Discord Bot
# pylint: disable=W0614

from bot_setup import *
from commands.random import *
from commands.role_update import *

print("Starting up...")
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):
    '''
    The following code updates basic info for all users on server
        user.id (str): the user's id number
        user.name (str): the user's username
        channel.id (str): the id of the channel the bot uses to dm the user 
    '''
    if message.content == "update user info":
        all_users = message.server.members
        for user in all_users:
            if not user.bot:
                dm_channel = await client.start_private_message(user)
                database.insert(user.id,user.name,str(dm_channel.id))

        await client.send_message(message.channel, "completed")

    '''
    Processes all commands. Commands are found in the commands/ folder.
    '''
    await client.process_commands(message)

# Run the Bot
client.run(TOKEN)