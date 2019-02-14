# Imports #

import discord
import asyncio
import random
import aiohttp
import json
import os
from discord.ext.commands import Bot

# Prefixes #

BOT_PREFIX = ("~", "Z", "<")

# Variables #

# Code #

client = discord.Client()

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a stoopid and pointless question.",
                brief="Answers from Ur Mum.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no you idot',
        'It is not looking likely',
        'Thats too hard! (thats what she said)',
        'It is quite possible (By that i mean "probably not ;)")',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

# Status Message #

@client.event
async def on_ready():
    print('The bot is ready!')
    print('Logged in as')
    print(client.user.name)
    await client.change_presence(game=discord.Game(name='ZestyPepper | Prefix: Z or < '))
	
@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {messaeg.author.name}: {message.content}")
	Network = client.get_guild(532959928961466379
	
	if "ZestyPepper.member_count" == message.content.lower():
		await message.channel.send(f'''{Network.member_count}'''")

# Other important shit #
    
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
