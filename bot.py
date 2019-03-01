# Imports #

import discord
import asyncio
import random
import time
import aiohttp
import json
import os
from discord.ext.commands import Bot

# Prefixes #

BOT_PREFIX = ("~", "Z-", "_")

# Variables #

client = discord.Client()

client = Bot(command_prefix=BOT_PREFIX)

#	#	# Fun! #	#	#

# 8ball #

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

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def Kick(ctx, UID: int):
    """Kick your haters"""
    try:
        UID = await client.get_user_info(UID)
        await client.kick(ctx.message.server, UID)
    except discord.Forbidden:
        await client.say("You don't have permissions :thinking:")
    excpet discord.HTTPException:
        await client.say("try again")

			
# Ban Command #
	
@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def Ban(ctx, UID: int):
    """Ban your haters"""
    try:
        UID = await client.get_user_info(UID)
        await client.ban(ctx.message.server, UID)
    except discord.Forbidden:
        await client.say("You don't have permissions :thinking:")
    excpet discord.HTTPException:
        await client.say("try again")

# Unban Command 3

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def Unban(ctx, UID: int):
    """Unban your haters"""
    try:
        UID = await client.get_user_info(UID)
        await client.unban(ctx.message.server, UID)
    except discord.Forbidden:
        await client.say("You don't have permissions :thinking:")
    excpet discord.HTTPException:
        await client.say("try again")

# Mute Command #		

@client.command(pass_context=True)
@commands.has_permissions(mute_members=True)
async def Mute(ctx, UID: int):
    """Mute your haters"""
    try:
        UID = await client.get_user_info(UID)
        await client.mute(ctx.message.server, UID)
    except discord.Forbidden:
        await client.say("You don't have permissions :thinking:")
    excpet discord.HTTPException:
        await client.say("try again")

			
# Unmute Commane #


@client.command(pass_context=True)
@commands.has_permissions(mute_members=True)
async def Unmute(ctx, UID: int):
    """Unmute your haters"""
    try:
        UID = await client.get_user_info(UID)
        await client.unmute(ctx.message.server, UID)
    except discord.Forbidden:
        await client.say("You don't have permissions :thinking:")
    excpet discord.HTTPException:
        await client.say("try again")

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


