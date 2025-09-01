import discord
from discord.ext import commands

class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gpt(ctx, *, prompt: str):
        if ctx.author == self.bot.user:
            return

     
        messages =[
            {"role": "system", "content": "You are a heavily sarcastic but very knowledgeable assistant that answers questions"},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",      
            messages=messages,
            temperature=0.5,
        )

        await ctx.channel.send(response.choices[0].message.content)
        print(f'Command {ctx.command} invoked by {ctx.author}')


async def setup(bot):
 await bot.add_cog(GPT(bot))
