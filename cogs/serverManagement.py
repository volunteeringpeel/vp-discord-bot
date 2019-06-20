import discord
from discord.ext import commands


"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.
For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class ServerManagement(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(":ping_pong: pong!")

    @commands.command()
    async def expose(self, ctx, msg_id):
        '''
        Exposes the users who didn't react to a message.
        Default channel is #announcements (can't change this yet)
        '''
        
        chan = self.bot.get_channel(id=515919559027589124) # Get announcement channel
        msg = await chan.fetch_message(msg_id) # Get intended message

        # Get list of people who reacted to message
        reactors = []
        for reaction in msg.reactions:
            async for member in reaction.users():
                reactors.append(member.mention)
        reactors = list(dict.fromkeys(reactors))

        # Get list of total executives and committee members
        suspects = []
        for guild in self.bot.guilds:
            for member in guild.members:
                for role in member.roles: 
                    # if role.name == "Dyno":
                    if role.name == "Committee Member" or role.name == "Executive":
                        suspects.append(member.mention)

        # Get list of total users who didn't react
        suspects = [user for user in suspects if user not in reactors]

        # Send them a nasty message
        await ctx.send("Please make sure to react to the latest " + chan.mention +". The following people have not done so: " + " ".join(suspects))

def setup(bot):
    bot.add_cog(ServerManagement(bot))