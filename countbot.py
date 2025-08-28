import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import time
import httpx

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

view_totals = {}
embed_messages = {}
API_URL = "https://zefame-free.com/api_free.php?action=order"

async def send_request(video_id):
    async with httpx.AsyncClient() as client:
        payload = {
            "action": "order",
            "service": "229",
            "link": f"https://www.tiktok.com/@user/video/{video_id}",
            "uuid": "38dc8fb0-0d2b-4b4b-a506-17871835682b",
            "videoId": video_id
        }
        response = await client.post(API_URL, data=payload, timeout=10)
        success = "Commande pass" in response.text
        print(f"Request for {video_id} sent. Success: {success}")
        return 300 if success else 0

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="view")
@app_commands.describe(link="TikTok video URL", duration="How many seconds to run the booster")
async def view(interaction: discord.Interaction, link: str, duration: int):
    await interaction.response.defer()
    video_id = link.rstrip("/").split("/")[-1]
    view_totals[video_id] = 0

    embed = discord.Embed(
        title="🚀 TikTok View Booster",
        description=f"Boosting video: `{video_id}`",
        color=0xff0050
    )
    embed.set_thumbnail(url=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg")
    embed.add_field(name="Total Views Added", value=0, inline=True)
    embed.add_field(name="Video Link", value=f"[Click Here]({link})", inline=False)

    msg = await interaction.followup.send(embed=embed)
    embed_messages[video_id] = msg

    end_time = time.time() + duration
    while time.time() < end_time:
        added_views = await send_request(video_id)
        view_totals[video_id] += added_views
        embed.set_field_at(0, name="Total Views Added", value=view_totals[video_id])
        await msg.edit(embed=embed)
        await asyncio.sleep(1)

    embed.add_field(name="Status", value=f"Finished running for {duration} seconds", inline=False)
    await msg.edit(embed=embed)

bot.run(os.environ.get("DISCORD_TOKEN"))

