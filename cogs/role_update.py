import discord
from discord.ext import commands
from bot_setup import users

class Role_Update:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def updates(self):
        mes = "What's your role update?"
        for user in users:
            await self.client.send_message(discord.Object(id=user[2]),mes)


def setup(client):
    client.add_cog(Role_Update(client))