import urllib.parse
import discord
import random
import logging
import asyncio

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
youtube_link = 'https://www.youtube.com/watch?v=ECmpUJdgm-g'
f = open('Token.txt', 'r')
server = discord.Server.id


if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!flip'):
        await client.send_message(message.channel, 'Flipping a coin for {0.author.mention}'.format(message))
        flip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!search'):
        search = message.content[7:]
        search = urllib.parse.quote_plus(search.strip())
        query = "https://ffxiv.gamerescape.com/w/index.php?search=" + search
        await client.send_message(message.channel, query)
    elif message.content.startswith('!grape'):
        await client.send_message(message.channel, "{0.author.mention}".format(message), tts=True)
        await client.send_message(message.channel, "Got any grapes?", tts=True)
        await client.send_message(message.channel, youtube_link)
    elif message.content.startswith('!dice'):
        await client.send_message(message.channel, "Rolling a dice for {0.author.mention}".format(message))
        dice = random.randint(1, 6)
        await client.send_message(message.channel, dice)
    elif message.content.startswith('!voicemessage'):
        voice_message = message.content[13:]
        await client.send_message(message.channel, voice_message, tts=True)
    #elif message.content.startswith('!join'):
     #   channel = client.get_channel('General')
      #  if not client.is_voice_connected(channel):
       #    await client.join_voice_channel()

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, "Current commands are: \n"
                                                   "\t\t\t!flip - flips a coin \n"
                                                   "\t\t\t!search searches Gamerscape uses form of:\n"
                                                   " \t\t\t\t\t`!search [query]`\n"
                                                   "\t\t\t!grape - special\n"
                                                   "\t\t\t!dice - rolls a 6 sided die\n"
                                                   "\t\t\t!voicemessage - text to speech message\n"
                                                   "Currently working on getting bot to join voice channel.\n"
                                                   "More commands to come soon!\n"
                                                   "Soon to come are voice functions... "
                                                   "if I can ever get things to work.")

client.run(f.read())
