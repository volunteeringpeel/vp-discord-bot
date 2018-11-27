# 
# VP Discord Bot
#

# Discord Imports
from discord.ext.commands import Bot
import os

# Load Bot
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Initialize Client
client = Bot('')

TOKEN = os.getenv('TOKEN')

# -------------------------------
# ------- Initialization --------
# -------------------------------

print("Starting up...") # Notify file was run

# Notify if Bot was setup correctly
@client.event
async def on_ready():
    print("Bot is online")

# -------------------------------
# -------- Functions ------------
# -------------------------------

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await client.send_message(message.channel, ":ping_pong: pong!")

# Run the Bot
client.run(TOKEN)