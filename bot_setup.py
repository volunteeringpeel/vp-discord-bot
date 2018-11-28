# pylint: disable=W0614

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

TOKEN = os.environ['TOKEN']
DBUSER = os.environ['DBUSER']
DBPASS = os.environ['DBPASS']

print(DBUSER)
print(DBPASS)

# Initialize Client
client = commands.Bot(command_prefix='$')

# Initialize "database" and "users":
#     database: object which connects to mysql database
#     users: str[][] -> (user.id, user.name, user.channel)
from server import database

database = database.Database(
                            "h2cwrn74535xdazj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com", # Host
                            DBUSER, # User
                            DBPASS, # Password
                            "ue1nsds7guapeehr" # Database
                            )
users = database.fetch("execList")