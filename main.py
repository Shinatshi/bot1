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
        random_image = choice(listdir('images'))
        with open(f'images/{random_image}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

    @bot.command()
    async def animal(ctx):
        random_image = choice(listdir('animals'))
        with open(f'animals/{random_image}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

    bot.run('token')