import discord
from discord.ext import commands

from bitcoin import BitcoinPrice
from coronavirus import CoronaVirus

import youtube_dl
import random
import os

client = commands.Bot(command_prefix='.')


@client.command()
async def exit(ctx):
    print('exiting')
    await ctx.send('ok me voy ps... mal amigo')
    await client.close()

@client.command()
async def play(ctx, url):
    songthere = os.path.isfile('./song.mp3')
    try:
        if songthere:
            os.remove('./song.mp3')
            print('borrando mp3')
            await ctx.send('limpiando el cache de audio')
    except PermissionError:
        await ctx.send('La musica esta sonando. ESPER...')
    server = ctx.message.guild
    vc = ctx.message.author.voice.channel
    if type(vc) is None:
        ctx.send('tienes que estar en un canal de vos')
    global voiceclient
    voiceclient = await vc.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('bajando audio..')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'song.mp3')

    voiceclient.play(discord.FFmpegPCMAudio('song.mp3'))
    voiceclient.source = discord.PCMVolumeTransformer(voiceclient.source)
    voiceclient.source.volume = 5

@client.command()
async def leave(ctx):
    if voiceclient.is_playing():
        await voiceclient.stop():
        await voiceclient.disconnect()
    else:
        await ctx.send('no toy reproduciendo nad')

@client.command()
async def pause(ctx):
    if voiceclient.is_playing():
        await voiceclient.pause()
    else:
        await ctx.send('no toy reproduciendo nad')

@client.command()
async def resume(ctx):
    if voiceclient.is_playing():
        await voiceclient.resume()
    else:
        await ctx.send('no toy reproduciendo nad')

@client.command()
async def btc(ctx):
    btcprice = BitcoinPrice.coinbase()
    await ctx.send('bitcoin esta a {} dolares..'.format(btcprice))

@client.group()
async def luisp(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('comando invalido... a lo mejor quisiste decir .luisp img?')

@luisp.command()
async def img(ctx):
    image_to_send = str(random.randrange(1,9))
    print(image_to_send)
    await ctx.send(file=discord.File("C:\\Users\\misu1\\OneDrive\\Documents\\luispiresbot\\image_database\\{}.jpeg".format(image_to_send)))

@client.group()
async def virus(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('comando invalido... a lo mejor quisiste decir \'.coronavirus deaths\' o \'.coronavirus cases?\'')

@virus.command()
async def casestotal(ctx):
    total = CoronaVirus.totalCases()
    await ctx.send('hay actualmente {} casos TOTALES de COVID19'.format(total))

@virus.command()
async def actcases(ctx):
    activecases = CoronaVirus.activeCases()
    await ctx.send('hay actualmente {} casos ACTIVOS de COVID19'.format(activecases))

@virus.command()
async def perished(ctx):
    deathsvar = CoronaVirus.deaths()
    await ctx.send('hay actualmente {} muertos gracias al COVID19'.format(deathsvar))

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status('dnd'))
    print('We have logged in as {0.user}'.format(client))


# Error identification system ----
@client.event
async def on_error(event, args):
    print('{} caused an exception'.format(event))
    await client.close()

@client.event
async def on_message_delete(message):
    culprit = message.author.name
    content = message.content
    print(str(culprit))
    await message.channel.send('epa..... {0.author.mention} q ases borrando esto?'.format(message))
    await message.channel.send('*'+ content +'*')
    try:
        await message.channel.send(message.attachments[0].proxy_url)
    except IndexError:
        pass

@client.event
async def on_message(message):
    culprit = message.author.name
    praises = [ 'HA HABLADO EL DIOS {0.author.mention} pires... el demonio'.format(message),
                    'alabado sea {0.author.mention} pires... el monsenor robesto sipols'.format(message),
                    'las cartas de {0.author.mention} segun san jose... verisuclo 9 cap 1'.format(message),
                    'silaba tonica',
                    '*trompetas* cabron!!!! respeta!!! luis p esta abland....',
                    '{0.author.mention} elohim essaim eleison kyrie'.format(message),
                    'hecho x andres',
                    '{0.author.mention} pires the creator... igor'.format(message),
                    'jajaajj q dies este idiota {0.author.mention}????'.format(message),
                    'agh... coronavirus coronavirus... lavese las manos',
                    'IGNIS SANCTUS Fuego eterno',
                    'ok toy ladiyao'
    ]
    if culprit == 'FlamingMilhouse':
        await message.channel.send(random.choice(praises))
    else:
        pass
    await client.process_commands(message)



client.run('NjkxMjQ5Mjc1MDIzMjYxNzM2.XnqXVg.y7La0UsI084ygI1rrZBqhH3cSEk')
