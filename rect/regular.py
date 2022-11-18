from email import message
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import io
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ui import Button, View, Item
from datetime import datetime
import textwrap
import requests

from cogs import guild_ids

print("rectreguの読み込み完了")

class spla3(View):
    def __init__(self):
        super().__init__(timeout=86400)

    @discord.ui.button(
        style=discord.ButtonStyle.green,
        label="参加",
        custom_id="join"
    )
    async def callback_join(self, button: Button, interaction: discord.Interaction):
        for child in self.children: 
            child.disabled = True 
        embed = interaction.message.embeds[0]
        flag = True
        if embed:
            if len(embed.fields) == 0:
                return embed.add_field(name=f"参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=True)

            for idlist in embed.fields[0].value.split("\n"):
                match = re.search(f"{interaction.user.id}",idlist)

            if match:
                flag = False
                embed2 = discord.Embed(description=f"{interaction.user.name}は既に参加しています")
                await interaction.response.send_message(embed=embed2,ephemeral = True)
                return embed

            if flag:
                users = [interaction.user.mention]
                cm = embed.fields[0].value
                tmp = "\n".join([str(user) for user in users])
                summon = tmp if tmp else "なし"
                time = datetime.now().strftime("%H:%M")
                embed.set_field_at(0,name="参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
                await interaction.response.edit_message(embed=embed)
                embed = discord.Embed()
                embed.set_author(name=f"{interaction.user.name}が参加しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
                await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)                

    @discord.ui.button(
        style=discord.ButtonStyle.blurple,
        label="取り消し",
        custom_id="remove"
    )
    async def callback_remove(self, button: Button, interaction: discord.Interaction):
        for child in self.children: 
            child.disabled = True
        embed = interaction.message.embeds[0]     
        flag = True
        if embed:
            if len(embed.fields) == 1:
                return embed.add_field(name="不参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)

            for idlist in embed.fields[1].value.split("\n"):
                match = re.search(f"{interaction.user.id}",idlist)

            if match:
                flag = False
                embed2 = discord.Embed(description=f"{interaction.user.name}は既に取り消しています")
                await interaction.response.send_message(embed=embed2,ephemeral = True)
                return embed

            if flag:
                summon_users = [interaction.user.mention]
                cm = embed.fields[1].value
                tmp = "\n".join([str(user) for user in summon_users])
                summon = tmp if tmp else "なし"
                time = datetime.now().strftime("%H:%M")
                embed.set_field_at(1,name="不参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
                await interaction.response.edit_message(embed=embed)
                embed = discord.Embed()
                embed.set_author(name=f"{interaction.user.name}が参加を取り消しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
                await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)

    @discord.ui.button(
        style=discord.ButtonStyle.red,
        label="しめ",
        custom_id="sime"
    )
    async def callback_sime(self, button: Button, interaction: discord.Interaction):
        interaction.permissions.use_application_commands = True
        for child in self.children: 
            child.disabled = True 
        embed = discord.Embed()
        embed.set_author(name=f"{interaction.user.name}の募集〆", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        await interaction.message.reply(embed=embed)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(
        style=discord.ButtonStyle.grey,
        label="ステージ",
        custom_id="stage"
    )
    async def callback_stage(self, button: Button, interaction: discord.Interaction):
            await interaction.response.defer()

            url = "https://spla3.yuu26.com/api/regular/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            map = jsonData["results"][0]["stages"][0]["name"]
            map2 = jsonData["results"][0]["stages"][1]["name"]
            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][0]["stages"][0]["image"]
            image2 = jsonData["results"][0]["stages"][1]["image"]

            img = Image.new('RGB', (800,200), (0, 0, 0))
            im1 = Image.open(io.BytesIO(requests.get(image).content))
            im2 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary = io.BytesIO()
            img.paste(im1, (405,0))
            img.paste(im2, (0,0))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            embed = discord.Embed(
                                        title = "レギュラーマッチ",
                                        color=0x15db1d,

                                        description=f"**{n}から{n2}まで**\n\n**{map}**\n**{map2}**")
            file = discord.File(img_binary, filename='image.png')
            embed.set_image(url="attachment://image.png")
            embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
            embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

            await interaction.followup.send(embed=embed,file=file,ephemeral = True)

class rectregu(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="時間", required=False))
        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long, required=False))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        img = Image.open("images/rect/nawabari.png")
        draw = ImageDraw.Draw(img) 
        font_path = "data/Splatfont.ttf"
        font = ImageFont.truetype(font_path, 70)
        time = '' if self.children[0].value else "集まり次第"
        draw.text((1050,382), f"{self.children[0].value}{time}" ,(0,0,0),font=font)
        draw.text((1050,685), self.children[1].value ,(0,0,0),font=font)
        draw.text((1050,995), self.children[2].value ,(0,0,0),font=font)

        content = '' if self.children[3].value else "記載なし"
        wrap_list = textwrap.wrap(f"{self.children[3].value}{content}", 11)  
        font_path2 = "data/05TogeGothic-SemiBold.otf"
        font2 = ImageFont.truetype(font_path2,52)
        line_counter = 0 
        for line in wrap_list:
            y = line_counter*60+460
            draw.multiline_text((260, y),line, fill=(255,255,255), font=font2)
            line_counter = line_counter +1 
        img_binary = io.BytesIO()
        img.save(img_binary, format='PNG')
        img_binary.seek(0)
        f = discord.File(img_binary, filename='image.png')

        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0x23f010
        )
        embed.add_field(name="参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.followup.send(f"{interaction.user.mention}がナワバリ募集中！: {spla3.is_persistent(spla3())}", embed=embed, file=f, view=spla3())

class regucom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="rectナワバリ" ,guild_ids=guild_ids, description="ナワバリ募集を取り付けます。")
    async def regurect(self, interaction: discord.Interaction):
        if interaction.channel.id not in [1027901079368761426,802345513495822339,803028814736392192]:
            return await interaction.respond("エラー：ナワバリ募集コマンドは <#1027901079368761426> で実行して下さい。",ephemeral = True)  
        modal = rectregu(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            if message.channel.id not in [1027901079368761426,802345513495822339,803028814736392192]:
                return
            rectword=['がナワバリ募集中！']
            for word in rectword:
                if word in message.content:
                    await message.channel.send("<@&983297498271580170>", delete_after=5)
            return 

def setup(bot: commands.Bot):
    bot.add_cog(regucom(bot=bot))