import discord
import asyncio
from discord.ext import commands

print("botuseの読み込み完了")

class botuse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return 
        if message.content == "IkacordBOTの使い方":
            global embedbotuse
            embedbotuse = discord.Embed( 
                            title="IkacordBOTの使い方",
                            description="バンカラ(オープン)"
                                            "```/stage バンカラオープン```\n"
                                            "バンカラ(チャレンジ)"
                                            "```/stage バンカラオープン```\n"
                                            "レギュラー"
                                            "```/stage レギュラー```\n"
                                            "サーモンラン"
                                            "```/stage サーモンラン```\n"
                                            "ランダムに武器を表示"
                                            "```/ランダム武器```\n"
                                            "ブランド別ギア表を表示"
                                            "```/ギア表```\n"
                                            "フレンドコードを保存する"
                                            "```/fc 登録 (自分のフレンドコード)```\n"
                                            "フレンドコードを検索する"
                                            "```/fc 検索 (対象の人をメンション)```\n"
                                            "自分のフレンドコードを削除する"
                                            "```/fc 削除 (自分をメンション) (自分のフレンドコード)```\n"
                                            "バンカラ募集"
                                            "```/rectバンカラ```\n"
                                            "レギュラー募集"
                                            "```/rectレギュラー```\n"
                                            "バイト募集"
                                            "```/rectバイト```\n"
                                            "なんでも募集"
                                            "```/rectスプラ```\n"
                                            "フェス募集(フェス期間のみ)"
                                            "```/rectフェス(各陣営)```\n"
                                            "読み上げを開始"
                                            "```/join```\n"
                                            "読み上げを終了"
                                            "```/disconnect```\n"
                                            "単語登録"
                                            "```/dictionary add before: after:```\n"
                                            "話者変更"
                                            "```/setvoice 話者:```\n"
                                            "読み上げbotのコマンドヘルプ"
                                            "```/dictionary help```\n"                                                                                                                                   
                                            "ikacordのコマンド別help表示"
                                            "```/help```"
                                            "bot情報"
                                            "```/bot 情報```\n"                                                                                       
                            ,color=0x30f05d, )

            channel = self.bot.get_channel(982600408704892998)

            await channel.send(embed=embedbotuse)

def setup(bot):
    bot.add_cog(botuse(bot))

