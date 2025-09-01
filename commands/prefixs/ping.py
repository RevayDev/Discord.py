import discord
from discord.ext import commands
import asyncio

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.reply("¡Hola, este es mi comando!")

async def setup(bot):
  await  bot.add_cog(Ping(bot))
