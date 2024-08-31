import discord
from discord.ext import commands
from os import listdir
from random import choice

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Бот запущен!')

@bot.command()
async def mem(ctx):
    all_images = listdir('images')
    
    even_images = [img for img in all_images if all_images.index(img) % 2 == 0]
    odd_images = [img for img in all_images if all_images.index(img) % 2 != 0]
    
    selection_pool = even_images * 3 + odd_images
    
    random_image = choice(selection_pool)
    
    with open(f'images/{random_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    if random_image in odd_images:
        await ctx.send("Редкая")

@bot.command()
async def animal(ctx):
    all_images = listdir('animals')
    
    even_images = [img for img in all_images if all_images.index(img) % 2 == 0]
    odd_images = [img for img in all_images if all_images.index(img) % 2 != 0]
    
    selection_pool = even_images * 3 + odd_images
    
    random_image = choice(selection_pool)
    with open(f'animals/{random_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    if random_image in odd_images:
        await ctx.send("Редкая")

bot.run('token')
