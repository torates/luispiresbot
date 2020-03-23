import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.command()
async def test(ctx, *arg):
    await ctx.send('{}'.format(' '.join(arg)))

@client.command()
async def ex(ctx, arg):
    if arg == 'vete':
        print('exiting')
        await ctx.send('ok me voy ps... mal amigo')
        await client.close()

@client.group()
async def luisp(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('comando invalido...')

@luisp.command()
async def img(ctx):
    image_to_send = str(random.randrange(1,9))
    print(image_to_send)
    await ctx.send(file=discord.File("C:\\Users\\misu1\\OneDrive\\Documents\\luispiresbot\\image_database\\{}.jpeg".format(image_to_send)))


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
    culprit = message.author.id
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
    if culprit == '691249275023261736':
        await message.channel.send(random.choice(praises))
    else:
        pass
    await client.process_commands(message)



client.run('NjkxMjQ5Mjc1MDIzMjYxNzM2.XniOyg.N9ut-ozzd5closr0TQf1Tfb7R7w')
