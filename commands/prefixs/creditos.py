import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio

class Creditos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="credis")
    async def credis(self, ctx):
        button = Button(label="Canal de youtube", url="https://www.youtube.com/@revaydev",
                        style=discord.ButtonStyle.danger, emoji="💙")
        button2 = Button(label="Donar", url="https://www.paypal.com/donate/?hosted_button_id=BUY65JN7NWM2U",
                         style=discord.ButtonStyle.danger, emoji="🎁")
        view = View()
        view.add_item(button)
        view.add_item(button2)
        await ctx.reply("Hola, este bot lo creo ¡RevayDev! :)", view=view)

async def setup(bot):
    await bot.add_cog(Creditos(bot))
