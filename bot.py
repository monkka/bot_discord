import discord
import random
from discord.ext import commands, tasks 
from dotenv import load_dotenv
import os 

# VARIÁVEIS DE AMBIENTE
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID_STR = os.getenv('SERVER_ID') or "0" 
CANAL_ID = int(SERVER_ID_STR)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.counter = 0 

@bot.event
async def on_ready():
    activity = discord.Game(name="Dando aulas na Kodland")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    
    if not my_background_task.is_running():
        my_background_task.start()
        
    print(f'Estamos logados como {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user.name}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@tasks.loop(seconds=60)
async def my_background_task():
    channel = bot.get_channel(CANAL_ID) 
    if channel:
        bot.counter += 1
        await channel.send(f"Contador atual: {bot.counter}")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Bem-vindo ao servidor, {member.mention}! 🎉')
        
@bot.command()
async def caraoucoroa(ctx):
    resultado = random.choice(["Cara", "Coroa"])
    
    if resultado == "Cara":
        emoji = "🪙 (Cara)"
    else:
        emoji = "👑 (Coroa)"
        
    await ctx.send(f'O resultado foi: **{emoji}**')
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpar(ctx, quantidade: int = 10):
    await ctx.channel.purge(limit=quantidade + 1)
    msg = await ctx.send(f'🧹 Faxina feita! Limpei {quantidade} sujeirices.')
    await msg.delete(delay=3)

@limpar.error
async def limpar_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 Nem, você não tem permissão para apagar por aqui...")
        
@bot.command(name="8ball")
async def magic_8ball(ctx, *, pergunta=None):
    if not pergunta:
        await ctx.send("❓ Por favor, faça uma pergunta para a Bola 8 Mágica responder.")
        return
    respostas = [
        "Com certeza!",
        "Minhas fontes dizem que não.",
        "Talvez sim, talvez não...",
        "Pergunte novamente mais tarde.",
        "Sem dúvida alguma.",
        "Não conte com isso.",
        "Sim, definitivamente!",
        "Sinais apontam que sim."
    ]
    
    resposta_escolhida = random.choice(respostas)
    
    embed = discord.Embed(title="🎱 A Bola 8 Mágica responde:", color=0x000000)
    embed.add_field(name="Pergunta:", value=pergunta, inline=False)
    embed.add_field(name="Resposta:", value=resposta_escolhida, inline=False)
    
    await ctx.send(embed=embed)

bot.run(TOKEN)
