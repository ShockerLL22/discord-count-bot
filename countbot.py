import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_CHANNEL_ID = 1405256990875193434 
SOURCE_CHANNEL_ID = 1405160957994598460  

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
count = 0

@bot.event
async def on_ready():
    global count
    print(f"Logged in as {bot.user}")
    await bot.wait_until_ready()
    
    source_channel = bot.get_channel(SOURCE_CHANNEL_ID)
    if source_channel:
        async for msg in source_channel.history(limit=1):
            match = re.search(r'\d+', msg.content)
            if match:
                count = int(match.group())
    print(f"Execution count initialized: {count}")

@bot.event
async def on_message(message):
    global count
    if message.channel.id == TARGET_CHANNEL_ID and not message.author.bot:
        count += 1
        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel:
            await channel.edit(name=f"execution count : {count}")
    await bot.process_commands(message)

bot.run(TOKEN)
