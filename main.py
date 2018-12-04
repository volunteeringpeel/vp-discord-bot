from bot_setup import client, TOKEN

print("Starting up...")

@client.event
async def on_ready():
    print("Bot is online")

client.load_extension("cogs.random")
client.load_extension("cogs.manage_roles")
client.load_extension("cogs.role_update")
client.load_extension("cogs.reminder")

client.run(TOKEN)