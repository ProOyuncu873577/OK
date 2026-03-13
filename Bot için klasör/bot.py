from ayarlar import ayarlar
import discord
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
ayricaliklar = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
ayricaliklar.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=ayricaliklar)


# Bot hazır olduğunda adını yazdıracak!
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')


# Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Kanka! Ben bir botum kanka!')
    if message.content.startswith('$artikyapmalutfen'):
        await message.channel.send('TMMDIR KANKAM')
    if message.content.startswith('$susmicam'):
        await message.channel.send('İlLaKi SuSaCaKSıN')
    if message.content.startswith('$sa'):
        await message.channel.send('as!')
    if message.content.startswith('$as'):
        await message.channel.send('sa!')
    if message.content.startswith('$laugh'):
        await message.channel.send('ehehehheehe')
    if message.content.startswith('$whoareyou'):
        await message.channel.send('Ben bir Discord botuyum, DJEko tarafından yapıldım.')
    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())  
    elif message.content.startswith('$susunartık'):
        await message.channel.send("TAMAM YAW SUSTUK İŞTE!")
    elif message.content.startswith('$knklerbotsizcehaklimi'):
        await message.channel.send("TABİİ Kİ :D")
    elif message.content.startswith('$seninyuzundenderseodaklanamiyoruz'):
        await message.channel.send("HEEEEEEEEEEE TAMAM SUSUYORUM HEMEN")
    elif message.content.startswith('$piirt'):
        await message.channel.send("OFFF KOKUTTUN YAW")
    elif message.content.startswith('$pass'):
        await message.channel.send(sifre_olusturucu(31))
    else:
        await message.channel.send("AMA PREFİX İLE KOMUTLARI KULLANMAZSAN ANLAYAMAM YAW (prefix = $, komutlar =`$seninyuzundenderseodaklanamiyoruz, $knklerbotsizcehaklimi, $susunartık, $coin, $smile, $whoareyou, $laugh, $as, $sa, $susmicam, $artikyapmalutfen, $hello, $random, $piirt`):((biri susmani istiyorsa sus)")
client.run(ayarlar["TOKEN"])