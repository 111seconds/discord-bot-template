import discord
from discord.ext import commands
import requests
import os # cleans console

os.system("cls") # cleans console

token = "x" # bot token here!
client_secret = "/" # leave blank if u are using token
prefix = "!" # prefix, if you dont want to use a prefix: leave it blank!

status = discord.Status.online
activity = discord.Activity

intents = discord.Intents.all()
client = commands.Bot(command_prefix= prefix, intents = intents)
client.remove_command('help') # removes help command so u can make a custom one if u want
status = status
activity = activity

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('status')) # if you want to change the status, change it here

print("hi there fella")

# commands below

# to add more commands, simply copy and paste line 35,36,37 and change "hi" to the command and "answer" to the bots answer!

# important: START ADDING COMMANDS HERE, NOT EARLIER!

@client.command()
async def hi(ctx): # command
    await ctx.send("Answer") # bots reply to command

# dont add commands after this line, commands should always be defined before running the bot!
print("for more help message me on discord (@111seconds)")

client.run(token) # starts bot

# make sure you have discord, requests and os installed! to do that simply open cmd and type "pip install os", "pip install discord.py" and "pip install requests"
