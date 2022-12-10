from discord.ext import tasks, commands
import discord
from discord.commands import slash_command, Option
from datetime import datetime
import requests

from cogs import guild_ids

print("testの読み込み完了")

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop4.start()

    @tasks.loop(seconds=10)
    async def loop4(self):
        now = datetime.now().strftime('%H:%M')
        if now == '17:48':
            channel = self.bot.get_channel(1043379022685536256)
            await channel.send('<:gp1:1035875883493380196>')

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return 
        if message.content == "test":
            a='<:gp1:1035875883493380196>'
            await message.channel.send(a)

    @slash_command(guild_ids=guild_ids)
    async def test(self,ctx):
        await ctx.respond('<:gp1:1035875883493380196>')


def setup(bot: commands.Bot):
    bot.add_cog(test(bot=bot))