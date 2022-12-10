from discord.ext import tasks, commands
import discord
from discord.commands import slash_command, Option
from datetime import datetime
import requests

print("test2の読み込み完了")

class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop4.start()

    @tasks.loop(seconds=10)
    async def loop4(self):
        url = "https://splatoon3.ink/data/gear.json"
        response = requests.get(url)
        jsonData = response.json()
        image = jsonData["data"]["gesotown"]["limitedGears"][5]["gear"]["image"]["url"]

        url2 = "https://api.koukun.jp/splatoon/3/geso/"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}
        response = requests.get(url2)
        jsonData = response.json()
        time = jsonData["limitedGears"][5]["saleEndTime"]
        t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        n = t.strftime('%m/%d %H:%M')
        gear = jsonData["limitedGears"][5]["gear"]["name"]
        brand = jsonData["limitedGears"][5]["gear"]["brand"]["name"]
        power1 = jsonData["limitedGears"][5]["gear"]["primaryGearPower"]
        price = jsonData["limitedGears"][5]["price"]

        henkan = (power1
                        .replace('ラストスパート', '<:gp1:1035875883493380196>')
                       .replace('イカニンジャ', '<:gp2:1035875858197512223>')
                       .replace('インク効率アップ(メイン)', '<:gp3:1035875881991811084>')
                       .replace('スペシャル減少量ダウン', '<:gp4:1035875877059297290>')
                       .replace('スタートダッシュ', '<:gp5:1035875870189047878>')
                       .replace('カムバック', '<:gp6:1035875861670395904>')
                       .replace('復活ペナルティアップ', '<:gp7:1035875889793224707>')
                       .replace('サブ性能アップ', '<:gp8:1035875866569347207>')
                       .replace('対物攻撃力アップ', '<:gp9:1035875888526532698>')
                       .replace('逆境強化', '<:gp10:1035875898030833684>')
                       .replace('リベンジ', '<:gp11:1035875884919439460>')
                       .replace('スーパージャンプ時間短縮', '<:gp12:1035875878854475846>')
                       .replace('インク回復力アップ', '<:gp13:1035875859631972383>')
                       .replace('相手インク影響軽減', '<:gp14:1035875894390161428>')
                       .replace('ステルスジャンプ', '<:gp15:1035875872055513088>')
                       .replace('受け身術', '<:gp16:1035875886798479370>')
                       .replace('サーマルインク', '<:gp17:1035875868431626291>')
                       .replace('追加ギアパワー倍化', '<:gp18:1035875896193732608>')
                       .replace('インク効率アップ(サブ)', '<:gp19:1035875863566221403>')
                       .replace('ヒト移動速度アップ', '<:gp20:1035875880507031562>')
                       .replace('スペシャル性能アップ', '<:gp21:1035875875448700928>')
                       .replace('イカダッシュ速度アップ', '<:gp22:1035875856553361438>')
                       .replace('スペシャル増加量アップ', '<:gp23:1035875873741619241>')
                       .replace('復活時間短縮', '<:gp24:1035875892775370752>')
                       .replace('アクション強化', '<:gp25:1035875854921764964>')
                       .replace('サブ影響軽減', '<:gp26:1035875865319456858>')
                       )
        hatena = '<:gp27:1035875901130416218>'
        okane = '<:cash:1035875899637248110>'                
        try:
            jsonData["limitedGears"][5]["gear"]["additionalGearPowers"][1]["name"]
        except IndexError:
            embed4 = discord.Embed(
                        title = "通常ピックアップ入荷",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")
            embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}", inline=True)
            embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed4.set_thumbnail(url=image)
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
        else:
            embed4 = discord.Embed(
                        title = "通常ピックアップ入荷",
                        color=0x457fce,
                        description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
            embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
            embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
            embed4.set_thumbnail(url=image)
            embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")

            try:
                jsonData["limitedGears"][5]["gear"]["additionalGearPowers"][2]["name"]
            except IndexError:    
                embed4 = discord.Embed(
                            title = "通常ピックアップ入荷",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n") 
                embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}", inline=True)
                embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed4.set_thumbnail(url=image)
                embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")
            else:
                embed4 = discord.Embed(
                            title = "通常ピックアップ入荷",
                            color=0x457fce,
                            description=f"**{n}まで**\n\n**{gear}/{brand}**\n\n")  
                embed4.add_field(name="ギアパワー", value=f"{henkan}|{hatena}{hatena}{hatena}", inline=True)
                embed4.add_field(name="おカネ", value=f"{okane}{price}", inline=True)
                embed4.set_thumbnail(url=image)
                embed4.set_footer(text="API: https://splatoon3.ink/| イカコード3")

        now = datetime.now().strftime('%H:%M')
        if now == '17:20':
            channel = self.bot.get_channel(1043379022685536256)
            await channel.send(embed=embed4)

def setup(bot):
    bot.add_cog(test2(bot))