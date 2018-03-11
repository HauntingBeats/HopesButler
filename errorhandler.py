import discord
from discord.ext import commands
import traceback
import sys

class ErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
            if isinstance (error, commands.CommandNotFound):
                embed = discord.Embed(title = "Error - Command not found!",
                                      description = "**" + ctx.author.name + "**, to view all my commands use: ?help", color = 0xFF0000)
                embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
                embed.add_field(name="Command Used: ", value = ctx.message.content)
                await ctx.send(embed = embed, delete_after=8.0)

            elif isinstance(error, commands.BadArgument):
                embed = discord.Embed(title = "Error - Spell Check!",description = "**"+ ctx.author.name +"**, make sure to carefully add the correct input", color = 0xFF0000)
                embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
                embed.add_field(name="Command Used: ", value = ctx.message.content)
                await ctx.send(embed = embed, delete_after=10.0)
                
            elif isinstance(error, commands.CommandOnCooldown):
                embed = discord.Embed(title = "Warning - Command Spam Detected :rage:!",description = "**"+ ctx.author.name +"**, Please wait before using command again!", color = 0xFF0000)
                embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
                embed.add_field(name="Command Used: ", value = ctx.message.content)
                await ctx.send(embed = embed, delete_after=10.0)

            elif isinstance (error, commands.MissingPermissions):
                embed = discord.Embed(title = "Error - Missing Permissions!",description = "**"+ ctx.author.name +"**, Who do you think you're tricking?", color =  0xFF0000)
                embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
                embed.add_field(name="Command Used: ",value = ctx.message.content)
                await ctx.send(embed = embed, delete_after=10.0)

            elif isinstance(error, commands.NotOwner):
                embed = discord.Embed(title = "Error - Not my daddy! :smirk:",description = "**"+ ctx.author.name +"**, I'm not dumb you troll! :smirk:", color = 0xFF0000)
                embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed = embed)
            try:
                await ctx.message.delete()
            except:
                pass
                if isinstance (error, commands.BotMissingPermissions):
                    pass
            else:
                #  All other Errors not returned come here... And we can just print the default TraceBack.
                print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
                traceback.print_exception(type(error),error,error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
    print('ErrorHandler Active')