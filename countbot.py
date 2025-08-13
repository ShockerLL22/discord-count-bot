import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
channel_id = 1405256990875193434
count = 0

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    global count
    if message.channel.id == channel_id and not message.author.bot:
        count += 1
        await message.channel.edit(name=f"execution count : {count}")
    await bot.process_commands(message)

bot.run(token)
