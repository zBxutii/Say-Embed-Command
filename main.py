import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('Bot Encendido')
  
@client.command()
async def say(ctx, saymsg):
  embed = discord.Embed(tile=f'{member} Sayed..', description=f'{saymsg}')
  
  await ctx.send(embed=embed)
  
client.run('token de tu bot')
