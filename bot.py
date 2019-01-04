#!/bin/python3.6

import discord
import asyncio
from discord.ext import commands

token = "NTMwNDY0NjE0MTAyNTk3NjMy.Dw_xsg.ytzrrtfg_GVtKPfnESL8VSEd1DA"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot Ready !")

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(f"{author} said : {content}")
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output) 


client.run(token)