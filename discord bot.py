import urllib.parse
import discord
import random
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
youtube_link = 'https://www.youtube.com/watch?v=ECmpUJdgm-g'
#voice = discord.VoiceClient(client.user,)


#opus_lib = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib():
    if discord.opus.is_loaded():
        return True
    else:
        discord.opus.load_opus('libopus-0x86.dll')


load_opus_lib()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!flip'):
        await client.send_message(message.channel, 'Flipping a coin...')
        flip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!search'):
        search = message.content[7:]
        search = urllib.parse.quote_plus(search.strip())
        query = "https://ffxiv.gamerescape.com/w/index.php?search="+ search
        print(query)
        await client.send_message(message.channel, query)
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, "Current commands are: \n"
                                                   "\t\t\t!flip - flips a coin \n"
                                                   "\t\t\t!search searches Gamerscape uses form of '!search [query]`\n"
                                                   "\t\t\t!grape - special\n"
                                                   "\t\t\t!dice - rolls a 6 sided die\n"
                                                   "More commands to come soon!\n"
                                                   "Soon to come are voice functions... "
                                                   "if i can ever get things to work.")
    elif message.content.startswith('!grape'):
        await client.send_message(message.channel, youtube_link)
    elif message.content.startswith('!dice'):
        dice = random.randint(1,6)
        await client.send_message(message.channel, "Rolling a die!")
        await client.send_message(message.channel, dice)



client.run()
