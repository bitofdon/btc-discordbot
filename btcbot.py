import discord
import json
from requests import Request, Session
import requests
from discord.ext import commands

#for tokens/keys
with open('config.json', 'r') as infile:
    config = dict(json.load(infile))
    bot_token = config["TOKEN"]

client = commands.Bot(command_prefix='/')

#to check that bot works - detects when the bot is ready & logged in
@client.event
async def on_ready():
    print('Bot is now online and ready')

#when user types '/btc' command, return the Price and 24% percent change
@client.command()
async def btc(ctx):
    url = "https://data.messari.io/api/v1/assets/btc/metrics"
    response = requests.get(url)
    market_data = response.json()['data']['market_data']
    price = market_data['price_usd']
    percent = market_data['percent_change_usd_last_24_hours']

    #this returns both price and percent, only taking 2 decimal places
    await ctx.send(f"Price: ${price:.2f} (changed {percent:+.2f}% in last 24 hours)")

#run the bot with Discord bot token    
client.run(bot_token)
