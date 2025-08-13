import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
MOD_CHANNEL_ID = 1402987082388869282

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

link_pattern = re.compile(r"(https?://\S+|discord\.gg/\S+)", re.IGNORECASE)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == MOD_CHANNEL_ID:
        if "key" in message.content.lower():
            await message.reply(f"Hey {message.author.mention}, check out this channel: <#{MOD_CHANNEL_ID}>")

        if link_pattern.search(message.content):
            try:
                await message.delete()
                await message.channel.send(f"Hey {message.author.mention}, don't send links!")
            except discord.Forbidden:
                print("Missing permissions to delete messages")
    
    await bot.process_commands(message)

bot.run(TOKEN)

