import discord
import asyncio 
import time 
import sys
import datetime
from discord.ext import commands
from paginator import Pages

class UtilityCommands():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(no_pm = True, aliases = ['ping'])
    async def latency(self, ctx):
        pingms = "{}".format(int(self.bot.latency * 1000))
        message = await ctx.send("Pinging the server....")
        await asyncio.sleep(2)
        await message.edit(content = f"Pong! - My latency is `{pingms}`ms")

    @commands.command(pass_context=True, no_pm=True)
    async def invite(self, ctx, *, member : discord.Member = None):
        guild = ctx.guild
        member = member or ctx.message.author
        channel = ctx.message.author
        avatar = member.avatar_url
        invite = discord.Embed(title='Invite me to your server!', url='https://discordapp.com/oauth2/authorize?client_id=372603198860427264&scope=bot&permissions=37084224', color=0x00FFFF)
        invite.set_author(name=member, icon_url=avatar)
        await ctx.send("I just slid in your DM's ;)")
        embed = invite
        await ctx.message.delete()
        await channel.send(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def help(self, ctx):
        help = discord.Embed(title='Help Menu:', color=0x00FFFF)
        help.set_author(name='HopesButler#2165', icon_url='https://cdn.discordapp.com/attachments/387479502206533632/389188924679127040/Logo_2.png')
        help.add_field(name='__?fun__', value='Type ?fun for fun commands', inline=False)
        help.add_field(name='__?data__', value='Type ?data for utility commands', inline=False)
        help.add_field(name='__?music__', value='Type ?music for music commands', inline=False)
        help.set_footer(text='Made by Haunt#7322')
        await ctx.send(embed=help)

    @commands.command(pass_context=True, no_pm=True)
    async def fun(self, ctx):
        help = discord.Embed(title='Commands', color=0x00FFFF)
        help.set_author(name='HopesButler#2165', icon_url='https://cdn.discordapp.com/attachments/387479502206533632/389188924679127040/Logo_2.png')
        help.add_field(name="__?dice__", value='Rolls a dice, giving a random number from 2-12', inline=False)
        help.add_field(name="__?math__", value="Simple calculator", inline=False)
        help.add_field(name="__?dance__", value="Gifs of People Dancing", inline=False)
        help.add_field(name="__?coinflip__", value="Heads or Tails?", inline=False)
        help.add_field(name='__?christmas__', value='Tells you how long until christmas', inline=False)
        help.add_field(name="__?devbday__", value='Tells you how long until the developer\'s birthday (Haunt#7322)', inline=False)
        help.set_footer(text='Made by Haunt#7322')
        await ctx.send(embed=help)

    @commands.command(pass_context=True, no_pm=True)
    async def data(self, ctx):
        util = discord.Embed(title='Utility Commands: ', color = 0x00FFFF)
        util.set_author(name='HopesButler#2165', icon_url='https://cdn.discordapp.com/attachments/387479502206533632/389188924679127040/Logo_2.png') 
        util.add_field(name="__?avatar__", value='Returns somebody\'s profile picture', inline=False)
        util.add_field(name="__?serverinfo__", value='Returns information about the server', inline=False)
        util.add_field(name='__?userinfo__', value='Returns information about the member', inline=False)
        util.add_field(name='__?listservers__', value='Lists all servers the bot is in', inline=False)
        util.add_field(name="__?ping__", value='Returns the ping the bot has to the server', inline=False)
        util.add_field(name='__?invite__', value='Sends you a private message with an invite link to the server.', inline=False)
        util.set_footer(text='Made by Haunt#7322')
        await ctx.send(embed=util)

    @commands.command(pass_context=True, no_pm=True)
    async def music(self, ctx):
        music = discord.Embed(title='Music Commands: ', color=0x00FFFF)
        music.set_author(name='HopesButler#2165', icon_url='https://cdn.discordapp.com/attachments/387479502206533632/389188924679127040/Logo_2.png')
        music.add_field(name='__?play__', value='Plays the song you search, ex. ?play candy paint', inline=False)
        music.add_field(name='__?stop__', value='Stops the music being played', inline=False)
        music.add_field(name='__?quit__', value='Makes the bot disconnect from the voice channel', inline=False)
        music.add_field(name='__?volume__', value='Self explanatory', inline=False)
        music.add_field(name='__?skip__', value='Also self explanatory', inline=False)
        await ctx.send(embed=music)

    @commands.guild_only()
    @commands.command(aliases = ['ls'])
    async def listservers(self, ctx):
        for guild in self.bot.guilds:
            guilds = [f"**{guild.name}** \nServer Owner: **{guild.owner.name}#{guild.owner.discriminator}**\nOnline Members: **{sum(m.status is discord.Status.online for m in guild.members)}** - Total Members: **{guild.member_count}**\nText Channels: **{str(len(guild.text_channels))}** - Voice Channels: **{str(len(guild.voice_channels))}**\n" for guild in self.bot.guilds]
        try:
            p = Pages(ctx, entries=guilds, per_page=5)
            p.embed.color = 0x00FFFF
            await p.paginate()
        except Exception as e:
            await ctx.send(e)

    @commands.command(pass_context=True, no_pm=True, aliases = ['info'])
    async def userinfo(self, ctx, *, member : discord.Member = None):
        'Information about a user'
        guild = ctx.guild
        member = member or ctx.message.author
        avatar = member.avatar_url
        roles = [role.name.replace('@', '@\u200b') for role in member.roles]
        embed = discord.Embed(description="Info about this user", color=0x00FFFF)
        embed.set_author(name=str(member), icon_url=avatar)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="Nickname", value= member.display_name)
        embed.add_field(name="User ID", value = member.id)
        embed.add_field(name="Account Created At", value = member.created_at.__format__('Date: %d %b %Y'), inline=False)
        embed.add_field(name= "Top Role", value = member.top_role)
        embed.add_field(name = "Roles", value = ' **|** '.join(roles) if len(roles) < 15 else f'{len(roles)} roles')
        embed.set_footer(text = f"Member since: {member.joined_at.__format__('%d %b %Y')}")
        await ctx.send(embed = embed)

    @commands.command(pass_context=True, no_pm=True)
    async def serverinfo(self, ctx):
        guild = ctx.guild
        roles = [x.name for x in guild.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at)
        time = time.split(' ')
        time = time[0]
        embed = discord.Embed(description='Info about this server', title='Information', colour=0x00FFFF)
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
        embed.add_field(name='__Created on__', value=guild.created_at.__format__('Date - %d %B %Y'), inline=True)
        return await ctx.send(embed=embed)

    @commands.command(aliases = ['xmas'])
    async def christmas(self, ctx):
        now=datetime.datetime.now()
        xmas=datetime.datetime(now.year, 12, 25)
        if xmas<now:
            xmas=xmas.replace(year=now.year+1)
        delta=xmas-now
        weeks, remainder=divmod(int(delta.total_seconds()), 604800)
        days, remainder2=divmod(remainder, 86400)
        hours, remainder3=divmod(remainder2, 3600)
        minutes, seconds=divmod(remainder3, 60)
        embed=discord.Embed(color=0x10a542)
        embed.add_field(name=":gift::christmas_tree::santa:Time left until Christmas:santa::christmas_tree::gift:", 
            value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
        await ctx.send(embed=embed)

    @commands.command(aliases = ['hauntbday'])
    async def ownerbday(self, ctx):
        now=datetime.datetime.now()
        bday=datetime.datetime(now.year, 8, 12)
        if bday<now:
            bday=bday.replace(year=now.year+1)
        delta=bday-now
        weeks, remainder=divmod(int(delta.total_seconds()), 604800)
        days, remainder2=divmod(remainder, 86400)
        hours, remainder3=divmod(remainder2, 3600)
        minutes, seconds=divmod(remainder3, 60)
        embed = discord.Embed(color=0x00FFFF)
        embed.add_field(name=":birthday: Time left until Haunt's Birthday :birthday:",
            value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        if await ctx.bot.is_owner(ctx.author):
            await ctx.send('Okay, I will be back soon!')
            self.bot.logout()
            sys.exit(0)
        else:
            await ctx.send("**:no_entry:** You're not my dad!")

def setup(bot):
    bot.add_cog(UtilityCommands(bot))
    print('Utility Commands Up')
