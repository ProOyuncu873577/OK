import discord
from discord.ext import commands
import random as rnd
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

# Memler ve kategorileri
mems = {
    "common": ["mem1.png"],
    "rare": ["mem2.png"],
    "legendary": ["mem3.png"]
}

# Rarity ağırlıkları
rarity_weights = [60, 30, 10]  # common daha sık, legendary nadir

@bot.command()
async def random(ctx):
    # Rarity seçimi
    rarity = rnd.choices(list(mems.keys()), weights=rarity_weights)[0]
    img_name = rnd.choice(mems[rarity])

    with open(f"images/{img_name}", "rb") as f:
        picture = discord.File(f)

    await ctx.send(f"Rarity: **{rarity.upper()}**")
    await ctx.send(file=picture)

bot.run("TOKEN")