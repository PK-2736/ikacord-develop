from discord.ext import tasks, commands
import discord
from discord.commands import slash_command, Option
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import requests
import json
from discord.ext import pages
from cogs import guild_ids
import io


print("spla3の読み込み完了")
dt = datetime.now()

class Splatoon3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    spla3 = discord.SlashCommandGroup("spla3", "フレンドコード関連", guild_ids = guild_ids)

    @spla3.command(name='rm武器', guild_ids = guild_ids, description='Splatoon3の武器をランダムに抽選します。')
    async def rw(self, message):
            json_open = open('data/spla3.json', 'r',encoding='utf-8')
            json_data = json.load(json_open)
            buki = random.choice(json_data)
            ja_name = buki["name"]["ja_JP"]
            path = "images/weapons/" + buki["name"]["ja_JP"] + ".png"
            file = discord.File(path, filename="image.png")
            user = message.author.display_name
            rw = discord.Embed(title = f"{user}さんにおすすめのブキは\n{ja_name}！",)
            #rw.add_field(name=f"{user}さんにおすすめのブキは",value=f"{ja_name}！")
            rw.set_image(url="attachment://image.png")
            await message.respond(file=file,embed=rw)

    @spla3.command(name='gear表', guild_ids = guild_ids, description='Splatoon3のブランド別ギア表を表示します。')
    async def gear(self, message):
            gear = discord.File("images/gear.jpg", filename="gear.png")
            brands = discord.Embed()
            brands.set_image(url="attachment://gear.png")
            await message.respond(file=gear,embed=brands)

    @spla3.command(name='dmg表', guild_ids = guild_ids, description='Splatoon3の武器別ダメージ表を表示します。')
    async def damage(self, message):
            damage = discord.File("images/damage.jpg", filename="damage.png")
            brands = discord.Embed()
            brands.set_image(url="attachment://damage.png")
            await message.respond(file=damage,embed=brands)
       
def setup(bot):
    bot.add_cog(Splatoon3(bot))