import os
from discord.ext import commands
import asyncio
from discord import Intents
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

#Variables
class MyBot(commands.Bot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.color = 0xTU_COLOR
    self.bienvenidas = ID_CHANNEL
    self.chat = ID_CHANNEL
    self.despedidas = ID_CHANNEL


bot = MyBot(command_prefix="+",
            intents=discord.Intents.all(),
            help_command=None)


# cargar comandos
async def load():
  for root, dirs, files in os.walk('./commands'):
    for filename in files:
      if filename.endswith('.py'):
        path = os.path.join(root, filename)
        module_name = path.replace('/', '.').replace('\\', '.')[2:-3]

        if not bot.get_cog(module_name.split('.')[-1]):
          try:
            await bot.load_extension(module_name)
          except:
            pass

  for filename in os.listdir('./events'):
    if filename.endswith('.py'):
      if not bot.get_cog(filename[:-3]):
        await bot.load_extension(f'events.{filename[:-3]}')


async def main():
  await load()
  await bot.start(TOKEN)


asyncio.run(main())
