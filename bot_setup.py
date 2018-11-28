# pylint: disable=W0614

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

# Load Bot
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Initialize Client
client = commands.Bot(command_prefix='!')

# Initialize "database" and "users":
#     database: object which connects to mysql database
#     users: str[][] -> (user.id, user.name, user.channel)
from server import database
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')

database = database.Database(
                            "h2cwrn74535xdazj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com", # Host
                            DBUSER, # User
                            DBPASS, # Password
                            "ue1nsds7guapeehr" # Database
                            )
users = database.fetch("execList")