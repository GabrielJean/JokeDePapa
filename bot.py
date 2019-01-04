#!/bin/python3.6
import json
from random import *
import os
import discord
import asyncio
from itertools import cycle
from discord.ext import commands



with open('../settings.json') as f:
    settings = json.load(f)



client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is online !")
    await client.change_presence(game=discord.Game(name='type !help'))

# @client.command(pass_context=True)
# async def join(ctx):
#     channel = ctx.message.author.voice.voice_channel
#     await client.join_voice_channel(channel)

# @client.command(pass_context=True)
# async def leave(ctx):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     await voice_client.disconnect()


@client.command(pass_context=True)
async def play(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.voice_channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await client.say('Connection au canal de voix: '+ channel)

        #Choose a random file to play
        audio = os.listdir("Audio")
        nb_len = len(audio)
        audiofile = randint(0, nb_len)

        # create StreamPlayer
        vc= await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player(f"Audio/{audio[audiofile]}", after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await client.say('L\'utilisateur n\'est pas dans un channel')



@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(f"{author} said : {content}")
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say('Pong!')
@client.command(pass_context=True)
async def say(ctx, *args):
    await client.delete_message(ctx.message)
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output) 


client.run(settings['token'])
