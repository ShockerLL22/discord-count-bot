import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import re
from datetime import datetime, timedelta

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SOURCE_TEXT_CHANNEL = 1405160957994598460
TARGET_VOICE_CHANNEL = 1405256990875193434

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
count = 0

@bot.event
async def on_ready():
    global count
    await bot.wait_until_ready()
    source_channel = bot.get_channel(SOURCE_TEXT_CHANNEL)
    if source_channel and isinstance(source_channel, discord.TextChannel):
        async for msg in source_channel.history(limit=1):
            match = re.search(r'\d+', msg.content)
            if match:
                count = int(match.group())
    keep_alive.start()

@tasks.loop(minutes=5)
async def keep_alive():
    pass

@bot.event
async def on_message(message):
    global count
    if message.channel.id != SOURCE_TEXT_CHANNEL or message.author.bot:
        return
    count += 1
    voice_channel = bot.get_channel(TARGET_VOICE_CHANNEL)
    if voice_channel and isinstance(voice_channel, discord.VoiceChannel):
        try:
            await voice_channel.edit(name=f"execution count : {count}")
        except Exception as e:
            print(f"Failed to edit voice channel: {e}")
    await bot.process_commands(message)

bot.run(TOKEN)
