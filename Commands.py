import discord
import random
import time
import datetime
from discord.ext import commands
import asyncio

class GeneralCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        pingtime = time.time()
        pingms = await ctx.send('Pinging the server....')
        ping = time.time() - pingtime
        time.sleep(1.5)
        await pingms.edit(content='Pong! The ping time is `%.01f seconds`' % ping)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send('Use this link to invite me to other discord servers! https://discordapp.com/oauth2/authorize?client_id=372603198860427264&scope=bot&permissions=37084224')

    @commands.command()
    async def help(self, ctx):
        help = discord.Embed(title='Help Menu', color=16711680)
        help.set_author(name='HopesButler#2165', icon_url='https://cdn.discordapp.com/attachments/387479502206533632/389188924679127040/Logo_2.png')
        help.add_field(name='__?help__', value='Shows this menu', inline=False)
        help.add_field(name='__?ping__', value='Shows how fast the bot can send messages', inline=False)
        help.add_field(name='__?hello__', value='Greetings from bot', inline=False)
        help.add_field(name='__?dice__', value='Rolls dice, generates a number between 2-12', inline=False)
        help.add_field(name='__?add__', value='Adds two numbers together ex. "?add 9 1"', inline=False)
        help.add_field(name='__?subtract__', value='Subtracts two numbers ex. ?substract 15 9', inline=False)
        help.add_field(name='__?fortune__', value='Types a random number from 1-100', inline=False)
        help.add_field(name='__?invite__', value='Invite the bot to your discord server', inline=False)
        help.add_field(name='__?date__', value='Tells the date and time of the bot', inline=False)
        help.add_field(name='__?avatar__', value='Shows the avatar of a user', inline=False)
        help.add_field(name='__?coinflip__', value='Flips a coin', inline=False)
        help.add_field(name='__?dance__', value='Pastes a random dance gif', inline=False)
        help.add_field(name='__?serverinfo__', value='Shows information about the server', inline=False)
        help.set_footer(text='Made by Haunt#7322')
        embed = help
        channel = ctx.author
        await channel.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        roles = [x.name for x in guild.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at)
        time = time.split(' ')
        time = time[0]
        embed = discord.Embed(description='Info about this server', title='Information', colour=16711680)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name='__Server __', value=str(guild))
        embed.add_field(name='__Server ID__', value=str(guild.id))
        embed.add_field(name='__Owner__', value=str(guild.owner))
        embed.add_field(name='__Owner ID__', value=guild.owner.id)
        embed.add_field(name='__Members__', value=str(guild.member_count))
        embed.add_field(name='__Text/Voice Channels__', value=str(channels))
        embed.add_field(name='__Roles__', value='%s' % str(role_length))
        embed.add_field(name='__Server Region__', value='%s' % str(guild.region))
        embed.add_field(name='__Verification Level__', value=guild.verification_level)
        embed.add_field(name='__Created on__', value=guild.created_at.__format__('Date - %d %B %Y at time - %H:%M:%S'))
        return await ctx.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hey! :wave:')

    @commands.command()
    async def coinflip(self, ctx):
        coinflip = ['Heads', 'Tails']
        answer = random.choice(coinflip)
        flip = await ctx.send("You toss the coin in the air...")
        time.sleep(2.5)
        await flip.edit(content='The coin falls and appears to be... {}!'.format(answer))

    @commands.command()
    async def dice(self, ctx):
        dice = await ctx.send("Rolling the dice....")
        answer = random.randint(2, 12)
        time.sleep(2.5)
        await dice.edit(content='You rolled a {}!'.format(answer))

    @commands.command()
    async def date(self, ctx):
        date = datetime.datetime.now().strftime('**Date: **%A, %B %d, %Y\n**Time: **%I:%M %p')
        embed = discord.Embed(color=16711680)
        embed.add_field(name="Bot's System Date & Time", value=date, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def dance(self, ctx):
        'Pastes random dance gif'
        Dance = ['https://media.giphy.com/media/3o72F2gPNTHli4yFzO/giphy.gif', 'https://media.giphy.com/media/26xBIbh7wgIMAZKsE/giphy.gif', 'https://media.giphy.com/media/xT0xexgbLQAi3yCqas/giphy.gif', 'https://media.giphy.com/media/3rgXBumyEL9086dy48/giphy.gif', 'https://media.giphy.com/media/XyAGm96eUIPsc/giphy.gif', 'https://media.giphy.com/media/KPgOYtIRnFOOk/giphy.gif', 'https://media.giphy.com/media/3rgXBvnbXtxwaWmhr2/giphy.gif', 'https://media.giphy.com/media/TfKfqjt2i4GIM/giphy.gif', 'https://media.giphy.com/media/iuuwqzPEDAZqM/giphy.gif', 'https://media.giphy.com/media/ALCI3eTii7qOk/giphy.gif', 'https://media.giphy.com/media/K9MPm9A3CaSkw/giphy.gif', 'https://media.giphy.com/media/6fScAIQR0P0xW/giphy.gif', 'https://media.giphy.com/media/XotulrpeCFzXi/giphy.gif']
        await ctx.send(random.choice(Dance))

    @commands.command()
    @commands.is_nsfw()
    async def nsfw(self, ctx):
        'NSFW command'
        nsfw = ['https://images-ext-1.discordapp.net/external/EdfKUPKJyFnpwIS1XsEg5Dxqs9YUj5HjejPD_1zbFN8/https/cdn.boobbot.us/Gifs/gif291.gif', 'https://images-ext-2.discordapp.net/external/Kki29Ze4XZyN7qUzdEMUsy48AII2Z1l7OhvLV4sIboM/https/cdn.boobbot.us/Gifs/gif643.gif', 'https://images-ext-1.discordapp.net/external/98Og-y3AwaqOHBbse9R--70kxr2PVERtbJ163VtMI98/https/cdn.boobbot.us/Gifs/gif459.gif', 'https://images-ext-1.discordapp.net/external/n35L5QA62j_RDOG7oek6VqNc0VjYRz4iC5nrd4eJaR0/https/cdn.boobbot.us/Gifs/gif473.gif', 'https://images-ext-1.discordapp.net/external/SbbAakQHuoz_FVQ1oiwjYT3BIPUGruCPNlzqGZm4ynM/https/cdn.boobbot.us/Gifs/gif835.gif', 'https://images-ext-2.discordapp.net/external/TAQ25XBvQuzh8UU85erfOzBfjR6aJgxUkJ6RNeWN_bo/https/cdn.boobbot.us/Gifs/gif610.gif', 'https://images-ext-2.discordapp.net/external/s9Xfo-tqLs1GxDS9VYelA6rCQ_cVYG5ew2d4o7oF-yg/https/cdn.boobbot.us/Gifs/gif638.gif', 'https://images-ext-2.discordapp.net/external/kBs4WaRA_56bqovUdrXIIPEWtuFb4z18mdyth2ySUXA/https/cdn.boobbot.us/Gifs/gif632.gif', 'https://images-ext-1.discordapp.net/external/mYXGOovRdUevu9pbxZzqHoe3du1Adr5gnp9z1wNmEZM/https/cdn.boobbot.us/Gifs/gif345.gif', 'https://images-ext-1.discordapp.net/external/YlP3ejdO60FvZZzu8j7gKVUY8Xxx4xhRE5Ivfvj8TxU/https/cdn.boobbot.us/Gifs/gif192.gif', 'https://images-ext-2.discordapp.net/external/4MWt5pt_UkpCSVuocXWvJnkrB2cCQNxdEH2eozBEGEA/https/cdn.boobbot.us/Gifs/gif982.gif']
        await ctx.send(random.choice(nsfw))

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member = None):
        "shows profile picture"
        member = member or ctx.message.author
        avatar = member.avatar_url
        em = discord.Embed(url=avatar, color= 0xFF0000)
        em.set_author(name=str(member), icon_url=avatar)
        em.set_image(url=avatar)
        await ctx.send(embed=em)

    @commands.command()
    async def fortune(self, ctx):
        'Test your luck with random numbers.'
        await ctx.send(random.randint(1, 100))

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        'Adds two numbers together.'
        await ctx.send(left + right)

    @commands.command()
    async def subtract(ctx, left: int, right: int):
        'Substracts two numbers'
        await ctx.send(left - right)

def setup(bot):
    bot.add_cog(GeneralCommands(bot))
    print('Commands Online')
