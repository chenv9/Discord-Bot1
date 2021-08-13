import discord
from discord.ext import commands
import random
import giphy_client
from discord.ext.commands import Bot
from giphy_client.rest import ApiException


# Create an instance of the API class
api_instance = giphy_client.DefaultApi()
giphy_token = 'ox3jdJyHR0uHjuDiZm6wa1hJXphLmus3'

api_instance = giphy_client.DefaultApi()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('bot is ready')

@bot.event
async def on_member_join(member):
    print(f'{member} is here.')

@bot.event
async def on_member_remove(member):
    print(member +" is gone")

@bot.command(aliases =['8ball', '8BALL'])
async def _8Ball(ctx, *, question):
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")

@bot.command()
async def ping(ctx): 
    await ctx.send(f'Heres my Ping : {bot.latency * 1000}')



@bot.command(aliases =['send'])
async def send_anonymous_dm(ctx, member: discord.Member, *, content):
    for i in range(25):
        channel = await member.create_dm() 
        await channel.send(content) 



async def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, query, limit=3, rating='g')
        lst = list(response.data)
        gif = random.choices(lst)

        return gif[0].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e


@bot.command(name='gif')
async def gif(ctx,foo):

    gif = await search_gifs(foo)
    await ctx.send(gif)

@bot.command(name='commands')
async def commands(ctx):
    await ctx.send("gif (input), max, max2, send, funk, hunty, scary, ace, 8ball")

@bot.command(name='max2')
async def black(ctx):
    gif = 'https://media.giphy.com/media/h8NhYvKUJNdkwcpjCZ/giphy.gif'
    await ctx.send(gif)


@bot.command(name='max3')
async def blacktwo(ctx):
    gif = 'https://media.giphy.com/media/ghCgpF3k34kbehVrrj/giphy.gif'
    await ctx.send(gif)

@bot.command(name='kevin')
async def kevin(ctx):
    gif = 'https://media.giphy.com/media/LmkjxjtkHR2iN7USVD/giphy.gif'
    await ctx.send(gif)

@bot.command(name='chris')
async def chris(ctx):
    gif = 'https://media.giphy.com/media/iFCE09YXyN0xgQyHKr/giphy.gif'
    await ctx.send(gif)

@bot.command(name='chris2')
async def chris2(ctx):
    gif = 'https://media.giphy.com/media/SpoBFBJEuVlD1xbq6w/giphy.gif'
    await ctx.send(gif)

@bot.command(name='max4')
async def max4(ctx):
    gif = 'https://media.giphy.com/media/ZXAdo2QyayVpEFJxDg/giphy.gif'
    await ctx.send(gif)




bot.run("NzQ2NTM5OTQ0NTM2OTY1MTQx.X0BzgA.xht-nF9XZEeHyVLGsUOcggldngQ")

