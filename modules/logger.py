import nextcord
from nextcord.ext import commands

class Logger(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot : commands.Bot = bot

def setup(bot : commands.Bot):
    bot.add_cog(Logger(bot))