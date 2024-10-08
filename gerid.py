import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Merhaba geri dönüşüm hakkında bilgi almak istiyorum.'):
        await message.channel.send("Tabi! Geri dönüşüm terim olarak, kullanım dışı kalan geri dönüştürülebilir atık malzemelerin çeşitli geri dönüşüm yöntemleri ile ham madde olarak tekrar imalat süreçlerine kazandırılmasıdır.")
    elif message.content.startswith('Peki geri dönüştürülebilir atıkların doğaya karışma süreleri nedir?'):
        await message.channel.send("Strafor 5000 yıl - 2 Milyon yıl, Cam Şişe 4000 yıl, Plastik 1000 yıl, Pet Şişe 400 yıl, Kutu Kola 10 yıl, Deterjan 400 yıl, Plastik Tabak 500 yıl, Pil 300 yıl, Alüminyum 100 yıl, Tahta Parçaları 15 yıl, Sigara İzmariti 1 yıl - 2 yıl, Gazete 3 ay, Çakmak 100 yıl")
    elif message.content.startswith("Geri dönüştürülebilir atıklar nelerdir?"):
        await message.channel.send("Kâğıt, metal, motor yağları, cam, karton, alüminyum, strafor, yeşil atık, ahşap,plastik pil")
    else:
        await message.channel.send(message.content)

client.run("MTI4MzQ2NjAyODcxNzgzODM5Nw.Gpr_9w.cq0BkqbI3wipxBXubtq1Xk50l_4Wcb3dK_BvaU")