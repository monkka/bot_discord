import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="Dando aulas na Kodland")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Estamos logados como {bot.user}')
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Bem-vindo ao servidor, {member.mention}! 🎉')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)