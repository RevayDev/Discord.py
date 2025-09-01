"""
  Si quieres usar este comando necesitas instalar openai


import discord
import interactions
from discord.ext import commands
from discord import app_commands
import asyncio
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GPT_KEY = os.getenv("GPT")

client = OpenAI(api_key=GPT_KEY, )

class GPT(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.color = bot.color

  @app_commands.command(name="gpt", description="Habla con una ia")
  async def gpt(self, interaction: discord.Interaction, consulta: str):
    await interaction.response.send_message(
        f'estoy pensado tu pregunta... "{consulta}" ')
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": consulta,
        }],
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content

    await interaction.channel.send(response)


async def setup(bot):
  await bot.add_cog(GPT(bot))

  

  
"""