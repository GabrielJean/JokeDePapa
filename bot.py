import json
from random import *
import os
import discord
import asyncio
from itertools import cycle
from discord.ext import commands

#read the token key from the settings.json file
with open('../settings.json') as f:
    settings = json.load(f)


dic = {}

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name='Coding...'))

@bot.command()
async def say(ctx, *args):
    await ctx.message.delete()
    if not args:
        await ctx.send("La commande nécessite un argument")
    else:
        await ctx.send('{}'.format(' '.join(args)))



@bot.command()
async def joke(ctx):
    await ctx.author.voice.channel.connect()



@bot.command()
async def stop(ctx):
    for vc in bot.voice_clients:
        if vc.guild.id == ctx.guild.id:
            await vc.disconnect()


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
#Start the client
bot.run(settings['token'])
