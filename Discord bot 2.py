import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

Bot =commands.Bot(command_prefix="DerpBot")

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on "+ bot.user.name)
    print ("with the ID: " + bot.user.id)

bot.run("NDYzNTQ3ODY2NzkxNTQyNzg1.DhyTxg.yUPmvSebXqXt_-IM6iZJ1ztwW1g")