import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_CHANNEL_ID = 1405256990875193434  # Text channel to update name
SOURCE_CHANNEL_ID = 1405160957994598460  # Text channel to read last count

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
count = 0

@bot.event
async def on_ready():
    global count
    print(f"Bot logged in as {bot.user}")
    await bot.wait_until_ready()
    
    source_channel = bot.get_channel(SOURCE_CHANNEL_ID)
    if source_channel and isinstance(source_channel, discord.TextChannel):
        async for msg in source_channel.history(limit=1):
            match = re.search(r'\d+', msg.content)
            if match:
                count = int(match.group())
    print(f"Execution count initialized: {count}")

@bot.event
async def on_message(message):
    global count
    print(f"Received message in channel {message.channel.id} from {message.author}")
    
    if message.channel.id == TARGET_CHANNEL_ID and not message.author.bot:
        count += 1
        print(f"Incremented count to {count}")
        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel and isinstance(channel, discord.TextChannel):
            await channel.edit(name=f"execution count : {count}")
            print(f"Updated channel name to 'execution count : {count}'")
    
    await bot.process_commands(message)

bot.run(TOKEN)
