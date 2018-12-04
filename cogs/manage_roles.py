import discord
from discord.ext import commands
from bot_setup import database

class Manage_Roles:

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def init(self):
        '''
        Updates basic info for all users on server
            user.id (str): the user's id number
            user.name (str): the user's username
            channel.id (str): the id of the channel the bot uses to dm the user 
        '''
        currentServer = self.client.get_server(id="515992928246824960")
        all_users = currentServer.members
        for user in all_users:
            exisiting_ids = [i[0] for i in database.fetch("execList")]
            if user.id not in exisiting_ids:
                if not user.bot and user.id:
                    dm_channel = await self.client.start_private_message(user)
                    database.insert(user.id,user.name,str(dm_channel.id))
        await self.client.say("completed")
    
    @commands.command()
    async def print_roles(self):
        '''
        Prints out all user information
        '''
        for i in database.fetch("execList"):
            await self.client.say(i[1])

def setup(client):
    client.add_cog(Manage_Roles(client))