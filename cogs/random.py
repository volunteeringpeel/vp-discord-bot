import discord
from discord.ext import commands

class Random:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self):
        await self.client.say(":ping_pong: pong!")
    
    @commands.command()
    async def say(self,arg):
        await self.client.say(arg)

def setup(client):
    client.add_cog(Random(client))