# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import asyncio
import random

DISCORD_TOKEN = "MTA5MTgyOTkzMDg4NDYxNjE5Mg.GeCk3X.9q5DNsoQ91BcsassIS8zNWo2F1LgeeLfvh2-Ro"
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

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

    # command, usermsg = None 
    # for text in ['@Cyno']:
    #     if message.content.startswith(text):
    #         command = message.content.split(' ')[0]
    #         usermsg = message.content.replace(text, '')
    #         print(command, usermsg)

    # if message.content.startswith('$hello'):
    #     async with message.channel.typing():
    #         await asyncio.sleep(1)
    #     await message.channel.send(intro)

    # if message.content.startswith ('$joke'):
    #     async with message.channel.typing():
    #         await asyncio.sleep(2)
    #     await message.channel.send(f"{random.choice(joke)}")
    # if message.content.startswith ('$explain'):
        #if mssg contains "i dont get it" or "why is that funny" or $explain 
            #explain


from characterai import PyCAI
client_ = PyCAI(CAI_TOKEN)

while True:
    mssg = input('You: ')
    data = client_.chat.send_message(CAI_ID, message)
    
    mssg = data['replies'][0]['text']
    name = data['src_char']['participant']['name']
    
    print(f"{name}:{message}")


# from characterai import PyAsyncCAI

# async def main():
#     client_ = PyAsyncCAI(CAI_TOKEN)
#     await client_.start()

#     # Save tgt and history_external_id to avoid making a lot of requests
#     chat = await client_.chat.get_chat(CAI_ID)

#     history_id = chat['external_id']
#     participants = chat['participants']

#     # In the list of "participants", a character can be at zero or in the first place
#     if not participants[0]['is_human']:
#         tgt = participants[0]['user']['username']
#     else:
#         tgt = participants[1]['user']['username']

#     while True:
#         message = input('You: ')

#         data = await client_.chat.send_message(
#             CAI_ID, message, history_external_id = history_id, tgt=tgt
#         )

#         name = data['src_char']['participant']['name']
#         text = data['replies'][0]['text']

#         print(f"{name}: {text}")

# asyncio.run(main())


client.run(DISCORD_TOKEN)

#contains/starts with hey cyno? 
