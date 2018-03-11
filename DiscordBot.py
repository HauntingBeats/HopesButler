import discord
from discord.ext import commands

from musicutils import config

startup_extensions = ["Commands", "utility", "errorhandler", "music"]
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'))
bot.remove_command('help')

@bot.event
async def on_ready():
    memberCount = len(list(bot.get_all_members()))
    guildCount = len(bot.guilds)
    print('Bot Online')
    print('Bot Username: {}'.format(bot.user))
    print('Server Count:', str(len(bot.guilds)))
    await bot.change_presence(activity=discord.Game(name='Say ?help | In {} servers'.format(guildCount)))

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(description='I have joined this server!', title='Information', color = 0x00ff00)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name='__Server __', value=str(guild))
    embed.add_field(name='__Server ID__', value=str(guild.id))
    embed.add_field(name='__Owner__', value=str(guild.owner))
    embed.add_field(name='__Owner ID__', value=guild.owner.id)
    embed.add_field(name='__Members__', value=guild.member_count)
    embed.add_field(name='__Server Region__', value='%s' % str(guild.region))
    embed.set_footer(icon_url=guild.icon_url, text='Guild created on {}'.__format__('Date - %d %B %Y'))
    channel = bot.get_channel(394586766562164737)
    await channel.send(embed=embed)
    
@bot.event    
async def on_guild_remove(guild):
    embed = discord.Embed(description='I have left this server!', title='Information', color = 0xFF0000)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name='__Server __', value=str(guild))
    embed.add_field(name='__Server ID__', value=str(guild.id))
    embed.add_field(name='__Owner__', value=str(guild.owner))
    embed.add_field(name='__Owner ID__', value=guild.owner.id)
    embed.add_field(name='__Members__', value=guild.member_count)
    embed.add_field(name='__Server Region__', value='%s' % str(guild.region))
    embed.set_footer(icon_url=guild.icon_url, text='Guild created on {}'.__format__('Date - %d %B %Y'))
    channel = bot.get_channel(394586766562164737)
    await channel.send(embed=embed)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.bot_token)
