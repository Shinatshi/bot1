import discord
from discord.ext import commands
from os import listdir
from random import choice
import requests 


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

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

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run('token')
