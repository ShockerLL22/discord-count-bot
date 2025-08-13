import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SOURCE_TEXT_CHANNEL = 1405160957994598460
TARGET_VOICE_CHANNEL = 1405256990875193434

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
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

@bot.event
async def on_message(message):
    global count
    if message.channel.id != SOURCE_TEXT_CHANNEL:
        return
    if message.author.bot:
        return
    count += 1
    voice_channel = bot.get_channel(TARGET_VOICE_CHANNEL)
    if voice_channel and isinstance(voice_channel, discord.VoiceChannel):
        await voice_channel.edit(name=f"execution count : {count}")
    await bot.process_commands(message)

bot.run(TOKEN)
