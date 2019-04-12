import discord
import json
from requests import Request, Session
import requests
from discord.ext import commands
import random

#for tokens/keys
with open('config.json', 'r') as infile:
    config = dict(json.load(infile))
    bot_token = config["TOKEN"]

client = commands.Bot(command_prefix='$')

#to check that bot works - detects when the bot is ready & logged in
@client.event
async def on_ready():
    print('Bot is now online and ready')


#COMMANDS HERE
#on $when_moon - generate one of the possible responses - must import random
@client.command()
async def when_moon(ctx):
    possible_responses = [
        'Hopefully soon',
        'Never',
        'Bottom is in',
        'just HODL'
    ]
    #await client.say(random.choice(possible_responses)) - this method is outdated
    await ctx.send(random.choice(possible_responses))

client.run(bot_token)
