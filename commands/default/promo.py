import discord
import interactions
from discord.ext import commands
from discord import app_commands
import asyncio


class Promo(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.color = bot.color
    self.promocion = bot.promocion

  @app_commands.command(name="promocion",
                        description="Crea una promocion para los usuarios")
  async def promo(self, interaction: discord.Interaction, titulo: str,
                  descripcion: str, planes: str):
    embed = discord.Embed(
        title=titulo,
        description="Descripcion:\n" + descripcion + "\n\n" +
        f'Planes:\n`{planes}`\n\n' +
        f"Nota: Para mas informacion pueden comunicarse con: {interaction.user.mention}",
        color=self.color)
    if interaction.user.avatar:
      embed.set_thumbnail(url=interaction.user.avatar.url)
      embed.set_footer(text="hecha por: " + interaction.user.name,
                       icon_url=interaction.user.avatar.url)

    await interaction.response.send_message(
        f"El anuncio ya esta listo, y se publico en el canal: <#{self.promocion}>",
        ephemeral=True)

    canal = self.bot.get_channel(self.promocion)

    await canal.send(embed=embed)


async def setup(bot):

  await bot.add_cog(Promo(bot))
