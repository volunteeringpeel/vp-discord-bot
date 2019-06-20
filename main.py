import discord, sys, traceback, os
from discord.ext import commands

# Get Token
from dotenv import load_dotenv
load_dotenv(verbose=True)
TOKEN  = os.environ['TOKEN']

# Initialize Bot
bot = commands.Bot(command_prefix='!')
initial_extensions = ['cogs.serverManagement']

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

# Load extensions (cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN, bot=True, reconnect=True)