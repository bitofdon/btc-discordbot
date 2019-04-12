import discord
import json
from requests import Request, Session
import requests
from discord.ext import commands

#for tokens/keys
with open('config.json', 'r') as infile:
    config = dict(json.load(infile))
    bot_token = config["TOKEN"]

client = commands.Bot(command_prefix='$')

#to check that bot works - detects when the bot is ready & logged in
@client.event
async def on_ready():
    print('Bot is now online and ready')



client.run(bot_token)
