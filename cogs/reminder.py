import discord
from discord.ext import commands

class Reminder:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def remind(self,*args):
        '''
        Be reminded about a certain task at a certain time
        '''
        try:
            identifier = args.index('@')
            task = ' '.join(args[:identifier])
            time = ' '.join(args[identifier+1:])
            await self.client.say("You will be reminded to {} at {}".format(task , time))
        except Exception as error:
            print(error)
            await self.client.say('Make sure the message is in the format of `^remind task @ time`')

def setup(client):
    client.add_cog(Reminder(client))