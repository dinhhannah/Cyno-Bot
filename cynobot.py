# bot.py
import os

import discord
from dotenv import load_dotenv

import asyncio

load_dotenv()

intents = discord.Intents.default()

client = discord.Client(intents=intents)

intro = "I'm Cyno, General Mahamatra of the Akademiya. It's my duty to uphold the rules, and punish wrongdoing. I will protect you on your journey."
joke = "Hmm... a joke? Ah, I've got just the one. Ahem... There once was a traveler, stranded in the desert and dying of thirst, who in desperation prayed for a Hydro Slime to come their way. But the traveler didn't realize that at that very moment, a starving Hydro Slime was praying to meet a lone, stranded traveler... What, not funny? Tsk, I think it's hysterical."

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(intro)
    if message.content.startswith('$joke'):
        await message.channel.send(joke)
    
client.run('MTA5MTgyOTkzMDg4NDYxNjE5Mg.GeCk3X.9q5DNsoQ91BcsassIS8zNWo2F1LgeeLfvh2-Ro')