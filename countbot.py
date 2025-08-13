import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_TO_PROMOTE = 1402987082388869282

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

link_pattern = re.compile(r"(https?://\S+|discord\.gg/\S+)", re.IGNORECASE)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if "key" in content:
        await message.reply(f"Hey {message.author.mention}, check out this channel: <#{CHANNEL_TO_PROMOTE}>")

    if "mango" in content:
        await message.reply("MENGO MENGO FJWEFHEWHFWHEFEHW")

    if link_pattern.search(message.content):
        try:
            await message.delete()
            await message.channel.send(f"Hey {message.author.mention}, don't send links!")
        except discord.Forbidden:
            print("Missing permissions to delete messages")

    await bot.process_commands(message)

bot.run(TOKEN)
