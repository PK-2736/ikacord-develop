import discord
from discord.commands import slash_command, Option
from discord.ext import commands
import asyncio
import re

from cogs import guild_ids

print("fcの読み込み完了")

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(style=discord.ButtonStyle.red,label="削除",custom_id="rm") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.message.delete()

class fc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    fc = discord.SlashCommandGroup("fc", "フレンドコード関連", guild_ids = guild_ids)

    @commands.Cog.listener()
    async def on_message(self, message): 
        if message.channel.id not in [802345513495822339,982600148259602442,1028366913140703243]:
                return
        if message.author.bot:
                return
        discordname = message.author.mention
        words=['/fc登録']
        for word in words:
                if word in message.content:
                    before_words = message.content
                    after_words = re.search(r'(\d{4})-?(\d{4})-?(\d{4})', before_words)
                    if after_words:
                        global embed
                        embed = discord.Embed(
                        color=0xf09214, 
                        description=f'{discordname} フレンドコードを設定しました\n'
                                    '`/fc 検索`で確認出来ます'
                                            )
                        embed2 = discord.Embed( # Embedを定義する
                            color=0xf09214, # フレーム色指定(今回は緑)
                            description=f"{discordname} がフレンドコードを設定しました {after_words.group(0)}" # Embedの説明文 必要に応じて
                            )
                        channel = self.bot.get_channel(1028366913140703243)
                        await channel.send(embed=embed2)  
                        await message.channel.send(embed=embed, delete_after=10)
                        file = open("data/friendcodes.txt", "a")
                        file.write(f'{discordname} ')
                        file.write(f'{after_words.group(0)}\n')
                        file.close()
                    else:
                        embed = discord.Embed(
                        color=0xcf5547, 
                        description=f'適切なフレンドコードを入力して下さい\n再入力は`/fc 登録`で確認出来ます'
                                            )
                        await message.channel.send(embed=embed, delete_after=10)


    @fc.command(name="登録", guild_ids=guild_ids, description="自分のフレンドコードをセットします。")
    async def register(self, interaction: discord.Interaction, *, フレンドコード: Option(str, "例：1111-1111-1111")):
        discordname = interaction.user.id
        file = open("data/friendcodes.txt", "a")
        file.write(f'<@{discordname}> ')
        file.write(f'{フレンドコード}\n')
        file.close()
        embed = discord.Embed( # Embedを定義する
                          color=0xf09214, # フレーム色指定(今回は緑)
                          description=f"<@{discordname}> がフレンドコードを設定しました {フレンドコード}" # Embedの説明文 必要に応じて
                          )
        embed2 = discord.Embed(
                    color=0xf09214, 
                    description=f'{discordname} フレンドコードを設定しました\n'
                                 '`/fc 検索`で確認出来ます'
                                         ) 
        channel = self.bot.get_channel(1028366913140703243)
        await channel.send(embed=embed)
        await interaction.response.send_message(embed=embed2, delete_after=10)

    @fc.command(name="検索", guild_ids=guild_ids, description="特定の人のフレンドコードを表示します。")
    async def search(self, interaction: discord.Interaction, メンション: Option(str, "例：@PheyK")):
        searchfile = open("data/friendcodes.txt", "r")
        flag = True
        for line in searchfile:
            if f'{メンション}' in line:
                flag = False
                embed = discord.Embed( # Embedを定義する
                        color=0xd2691e, # フレーム色指定(今回は緑)
                            description=f"フレンドコード-> {line}" # Embedの説明文 必要に応じて
                            )
        if flag:
                embed1 = discord.Embed( # Embedを定義する
                            color=0xd2691e, # フレーム色指定(今回は緑)
                            title="未登録",
                            description="このユーザーのフレンドコードは登録されていません。") # Embedの説明文 必要に応じて
                await interaction.response.send_message(embed=embed1,ephemeral = True)
                return searchfile.close()

        await interaction.response.send_message(embed=embed,view=MyView(), delete_after=1000)

    @fc.command(name="削除", guild_ids=guild_ids, description="登録しているフレンドコードを削除します。")
    async def delete(self, ctx, メンション: Option(str, "例：@PheyK"), フレンドコード: Option(str, "例：1111-1111-1111")):
        with open("data/friendcodes.txt", "r") as f:
            lines = f.readlines()
        with open("data/friendcodes.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != f'{メンション} {フレンドコード}':
                    f.write(line)
            embed = discord.Embed( # Embedを定義する
                          color=0xe64b47, # フレーム色指定(今回は緑)
                          description="フレンドコードを削除しました" # Embedの説明文 必要に応じて
                          )
            await ctx.respond(embed=embed, delete_after=5)

def setup(bot):
    bot.add_cog(fc(bot))