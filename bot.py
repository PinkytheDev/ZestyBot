# Imports #

import discord
import youtube_dl
import asyncio
import random
import time
import aiohttp
import json
import os
from discord.ext import commands 
from discord.ext.commands import Bot

# Prefixes #

BOT_PREFIX = ("~", "Z-", "_")

# Variables #

client = discord.Client()

client = Bot(command_prefix=BOT_PREFIX)


players = {}
queues = {}

def check_queue(id):
    if queue[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()


#	#	# Fun! #	#	#

# Music #

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.say('Joined.')
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    await client.say('Disconnected.')
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnet()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Video queued')


@client.command(name='8ball',
                description="Answers a stoopid and pointless question.",
                brief="Answers from Ur Mum.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no you idot',
        'It is not looking good (like me!)',
        'That question is too hard!',
        'It is quite possible :thinking: ',
        'Definitely (Not!)',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
# Math  add #

@client.command()
async def add(left : int, right : int):
    """Adds Two Numbers."""
    await client.say(left + right)

# Math Subtraction #

@client.command()
async def subtract(left : int, right : int):
	"""Subtracts Two Numbers."""
	await client.say(left - right)

# Math Multiplication #

@client.command()
async def multiply(left : int, right : int):
	"""Multiplies Numbers."""
	await client.say(left * right)
	
# Math Division #

@client.command()
async def divide(left : int, right : int):
	"""Divides Numbers!"""
	try:
	        await client.say(left // right)
	except ZeroDivisionError:
		await client.say("You cannot divide by 0! :thinking:")

# Ping #

@client.command()
async def Ping():
	"""Pangs! :ping_pong:"""
	await client.say("Pong! :ping_pong:")
	
# Shoot Command #

@client.command(name='Shoot',
                description="Shoot an enemy!",
                brief="Shoot your enemies....",
                pass_context=True)
async def Shoot(context, target: discord.Member):
    possible_responses = [
        'You missed your shot!',
        'Uh oh! The fuzz have arrived!',
        'You hit! ' + target.mention,
        'Your enemy ' + target.mention + ' dies a bloody death!',
        'Ew, blood!',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention);
	
# Stab Command #

@client.command(name='Stab',
                description="Stab an enemy!",
                brief="Stab your enemies....",
                pass_context=True)
async def Shoot(context, target: discord.Member):
    possible_responses = [
        'You spill their guts!',
        'Oh no, the Po-Po!',
        'You stab! ' + target.mention,
        'Your enemy ' + target.mention + ' dies a bloody death! (Lots of blood and guts)',
        'Ew, blood!',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention);

	
# Status Message #

@client.event
async def on_ready():
    print('The bot is ready!')
    print('Logged in as')
    print(client.user.name)
    await client.change_presence(game=discord.Game(name='ZestyPepper | Prefix: Z-'))
	
# # # Moderation # # #

# Kick Command #

@client.command(pass_context = True)
async def Kick(ctx, userName: discord.User):
    """Kick a user""" 
    try:
       await client.kick(userName)
       await client.say("Successful!")
    except:
       await client.say("You don't have permissions :thinking:")
    

			
# Ban Command #
	
@client.command(pass_context = True)
async def Ban(ctx, userName: discord.User):
    """Ban a user""" 
    try:
       await client.ban(userName)
       await client.say("Successful!")
    except:
       await client.say("You don't have permissions :thinking:")
   

# Unban Command 3

@client.command(pass_context = True)
async def Unban(ctx, userName: discord.User):
    """Unban a user""" 
    try:
       await client.unban(userName)
       await client.say("Successful!")
    except:
        await client.say("You don't have permissions :thinking:")
	
# Other important crap #
    
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(str(os.environ.get('BOT_TOKEN')))
