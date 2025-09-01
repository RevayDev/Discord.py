import discord
import interactions
from discord.ext import commands
from discord import app_commands
import asyncio

class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color

    @app_commands.command(name="botinfo", description="te dire de mi informacion actual")
    async def botinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Mi informacio",
            description=f"> **Descripcion**\n RevayDev es mi creador, fui creada para múltiples funciones para que no tengas muchos bots que hagan varias cosas. Conmigo tendrás 5 bots en uno (yo)🤖. \n\n> **RevayDev**\neste bot es uso personal para las personas que descargaron su codigo fuente.\n\n> **otros datos**\n🎫 Nombre: {self.bot.user.name}\n 💡 ID:{self.bot.user.id}\n💻 Creado: {self.bot.user.created_at.strftime('%d/%B/%Y')}",
            color=self.color
        )
        if self.bot.user.avatar:
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Botinfo(bot))
