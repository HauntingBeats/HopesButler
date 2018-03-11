import asyncio
import datetime
import os
import random
import sys
import time
import urbandict

import discord
from discord.ext import commands



class GeneralCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True, aliases = ['ud', 'dict'])
    async def urban(self, ctx, *, message: str, member : discord.Member = None):
        member = member or ctx.message.author
        avatar = member.avatar_url
        defi = urbandict.define(message)
        definition = defi[0]['def']
        example = defi[0]['example']
        embed = discord.Embed(title=message,description=definition, color=0x00FFFF)
        embed.set_author(name=ctx.message.author, icon_url=avatar)
        embed.add_field(name="__Example__", value=example, inline=False)
        embed.set_footer(text=f"This message was triggered by {ctx.message.author}", icon_url='https://vignette.wikia.nocookie.net/logopedia/images/a/a7/UDAppIcon.jpg/revision/latest?cb=20170422211150')
        await ctx.send(embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        coinflip = ['Heads', 'Tails']
        answer = random.choice(coinflip)
        flip = await ctx.send("You toss the coin in the air...")
        asyncio.sleep(2.5)
        await flip.edit(content='The coin falls and appears to be... {}!'.format(answer))

    @commands.command(pass_context=True, no_pm=True, aliases = ['roll'])
    async def dice(self, ctx):
        dice = await ctx.send("Rolling the dice....")
        answer = random.randint(2, 12)
        time.sleep(2.5)
        await dice.edit(content='You rolled a {}!'.format(answer))

    @commands.command(pass_context=True, no_pm=True, aliases = ['today'])
    async def date(self, ctx):
        date = datetime.datetime.now().strftime('**Date: **%A, %B %d, %Y\n**Time: **%I:%M %p')
        embed = discord.Embed(color=0x00FFFF)
        embed.add_field(name="Bot's System Date & Time", value=date, inline=False)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def dance(self, ctx):
        'Pastes random dance gif'
        choice = ['https://media.giphy.com/media/3o72F2gPNTHli4yFzO/giphy.gif', 'https://media.giphy.com/media/26xBIbh7wgIMAZKsE/giphy.gif', 'https://media.giphy.com/media/xT0xexgbLQAi3yCqas/giphy.gif', 'https://media.giphy.com/media/3rgXBumyEL9086dy48/giphy.gif', 'https://media.giphy.com/media/XyAGm96eUIPsc/giphy.gif', 'https://media.giphy.com/media/KPgOYtIRnFOOk/giphy.gif', 'https://media.giphy.com/media/3rgXBvnbXtxwaWmhr2/giphy.gif', 'https://media.giphy.com/media/TfKfqjt2i4GIM/giphy.gif', 'https://media.giphy.com/media/iuuwqzPEDAZqM/giphy.gif', 'https://media.giphy.com/media/ALCI3eTii7qOk/giphy.gif', 'https://media.giphy.com/media/K9MPm9A3CaSkw/giphy.gif', 'https://media.giphy.com/media/6fScAIQR0P0xW/giphy.gif', 'https://media.giphy.com/media/XotulrpeCFzXi/giphy.gif']
        Dance = random.choice(choice)
        em = discord.Embed(color = 0xFF0000)
        em.set_author(name='Dance Gif: ')
        em.set_image(url=Dance)
        await ctx.send(embed=em)

    @commands.command(pass_context=True, no_pm=True)
    @commands.is_nsfw()
    async def nsfw(self, ctx):
        'NSFW command'
        nsfw = ['https://images-ext-1.discordapp.net/external/EdfKUPKJyFnpwIS1XsEg5Dxqs9YUj5HjejPD_1zbFN8/https/cdn.boobbot.us/Gifs/gif291.gif', 'https://images-ext-2.discordapp.net/external/Kki29Ze4XZyN7qUzdEMUsy48AII2Z1l7OhvLV4sIboM/https/cdn.boobbot.us/Gifs/gif643.gif', 'https://images-ext-1.discordapp.net/external/98Og-y3AwaqOHBbse9R--70kxr2PVERtbJ163VtMI98/https/cdn.boobbot.us/Gifs/gif459.gif', 'https://images-ext-1.discordapp.net/external/n35L5QA62j_RDOG7oek6VqNc0VjYRz4iC5nrd4eJaR0/https/cdn.boobbot.us/Gifs/gif473.gif', 'https://images-ext-1.discordapp.net/external/SbbAakQHuoz_FVQ1oiwjYT3BIPUGruCPNlzqGZm4ynM/https/cdn.boobbot.us/Gifs/gif835.gif', 'https://images-ext-2.discordapp.net/external/TAQ25XBvQuzh8UU85erfOzBfjR6aJgxUkJ6RNeWN_bo/https/cdn.boobbot.us/Gifs/gif610.gif', 'https://images-ext-2.discordapp.net/external/s9Xfo-tqLs1GxDS9VYelA6rCQ_cVYG5ew2d4o7oF-yg/https/cdn.boobbot.us/Gifs/gif638.gif', 'https://images-ext-2.discordapp.net/external/kBs4WaRA_56bqovUdrXIIPEWtuFb4z18mdyth2ySUXA/https/cdn.boobbot.us/Gifs/gif632.gif', 'https://images-ext-1.discordapp.net/external/mYXGOovRdUevu9pbxZzqHoe3du1Adr5gnp9z1wNmEZM/https/cdn.boobbot.us/Gifs/gif345.gif', 'https://images-ext-1.discordapp.net/external/YlP3ejdO60FvZZzu8j7gKVUY8Xxx4xhRE5Ivfvj8TxU/https/cdn.boobbot.us/Gifs/gif192.gif', 'https://images-ext-2.discordapp.net/external/4MWt5pt_UkpCSVuocXWvJnkrB2cCQNxdEH2eozBEGEA/https/cdn.boobbot.us/Gifs/gif982.gif']
        Choice = random.choice(nsfw)
        em = discord.Embed(color= 0xFF0000)
        em.set_author(name='NSFW Gif: ')
        em.set_image(url=Choice)
        await ctx.send(embed=em)

    @commands.command(pass_context=True, no_pm=True, aliases = ['picture'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        "shows profile picture"
        member = member or ctx.message.author
        avatar = member.avatar_url
        if ".gif" in avatar:
            avatar += "&f=.gif"
        em = discord.Embed(url=avatar, color= 0xFF0000)
        em.set_author(name=str(member), icon_url=avatar)
        em.set_image(url=avatar)
        await ctx.send(embed=em)

    @commands.command(no_pm=True, aliases = ['add', 'multiply', 'divide', 'subtract'])
    async def math(self, ctx, *args):
        await ctx.send(eval(" ".join(args)))

def setup(bot):
    bot.add_cog(GeneralCommands(bot))
    print('Commands Online')
