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


client = discord.Client()

#Confirm when the bot is ready
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

#Allow the user to stop the bot before it end by itself
@bot.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@bot.command(pass_context=True)
async def joke(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.voice_channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        if voice_client == None:
            # grab user's voice channel
            channel=voice_channel.name
            await client.say('Connection au canal de voix: '+ channel)

            #Choose a random file to play
            audio = os.listdir("Audio")
            nb_len = len(audio)
            audiofile = randint(0, nb_len - 1)

            embed = discord.Embed()
            embed.set_author(name='Joke de Papa')
            embed.set_footer(text='Tout droits réservés à Gaboom Films')
            embed.set_thumbnail(url='https://sauterellesetcoccinelles.com/wp-content/uploads/2017/10/JOKE-DE-PAPA.jpg')
            embed.add_field(name='Titre', value=audio[audiofile].replace('.flac', ''))
            await client.say(embed=embed)

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
            await client.say("Veuillez attendre que la blague se termine")
    else:
        await client.say('L\'utilisateur n\'est pas dans un channel vocal')


#Log all messages for testings purposes
#@bot.event
#async def on_message(message):
#    author = message.author
#    content = message.content
#    print(f"{author} said : {content}")
#    await client.process_commands(message)

#Respond Ping to the !ping command (for testing)
@bot.command()
async def ping():
    await client.say('Pong!')

@bot.command()
async def help():
    await client.say("""
**Comment utiliser le bot : **
!help : Affiche cette aide.
!joke : Lance une joke dans le canal vocal de l'auteur.
!stop : Arrête la joke en cours.
!say : Fait dire quelque chose au bot.
!ping : Teste la connection du bot.
""")

#Make the bot say wathever is written after the command !say
@bot.command(pass_context=True)
async def say(ctx, *args):
    await client.delete_message(ctx.message)
    output = ''
    if not args:
        await client.say("La commande nécessite un argument")
    else:
        for word in args:
            output += word
            output += ' '
        await client.say(output) 


#Start the client
client.run(settings['token'])
