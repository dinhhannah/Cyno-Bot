# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
DISCORD_TOKEN = "MTA5MTgyOTkzMDg4NDYxNjE5Mg.GeCk3X.9q5DNsoQ91BcsassIS8zNWo2F1LgeeLfvh2-Ro"

import asyncio
import random

from characterai import PyCAI
CAI_TOKEN = "cebc0e7ca978e159dbca0c0970e40ff2cf1454c0"
CAI_ID = "DCKUsZ-oNCKOe2nUcDIpk3hBcCNjhR1UsnoIHF-G4Nk"

load_dotenv() #load environment variables

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# intro = "I'm Cyno, General Mahamatra of the Akademiya. It's my duty to uphold the rules, and punish wrongdoing. I will protect you on your journey."
# joke = [
#     "Hmm... a joke? Ah, I've got just the one. Ahem... There once was a traveler, stranded in the desert and dying of thirst, who in desperation prayed for a Hydro Slime to come their way. But the traveler didn't realize that at that very moment, a starving Hydro Slime was praying to meet a lone, stranded traveler... What, not funny? Tsk, I think it's hysterical.",
#     "Why did the Sumpter Beast cross the road while burdened with heavy goods? To get to Sumeru's Most Sumptuous Sumpter Beast bodybuilding competition.",
#     "Which creature has the worst personal hygiene in all of Teyvat? Cryo Slimes. Why? Because they always bounce on top of the water, and never go in for a bath."
#     ]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (message.author.id != client.user.id):
        # async with message.channel.typing():
        #     await asyncio.sleep(1)
        # await message.channel.send(intro)

        botmssg = (str(message.content))
        await message.channel.send(botmssg)

    # if message.content.startswith ('$joke'):
    #     async with message.channel.typing():
    #         await asyncio.sleep(2)
    #     await message.channel.send(f"{random.choice(joke)}")
    # if message.content.startswith ('$explain'):
        #if mssg contains "i dont get it" or "why is that funny" or $explain 
            #explain

client.run(DISCORD_TOKEN)
