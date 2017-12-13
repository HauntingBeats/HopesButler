import discord
from discord.ext import commands
import random
import time
import datetime
import asyncio
import bot_token


startup_extensions = ["Commands"]
bot = commands.Bot('?')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Bot Online')
    print('Bot Username: {}'.format(bot.user))
    print('Server Count:', str(len(bot.guilds)))
    await bot.change_presence(game=discord.Game(name=('say ?help | In ' + str(len(bot.guilds))) + ' Servers!'))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot_token.token)
