import json
import discord
from discord.ext import commands
# from dotenv import load_dotenv
from replit import db
import os

# https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

client = commands.Bot(command_prefix="/")
# token = os.environ.get('DISCORD_BOT_SECRET')
token = 'xxx';

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.command(pass_contect=True)
async def addguild(ctx, *, guildname):
    await ctx.send("Guild to be added to DB "+guildname);
    
@client.command(pass_contect=True)
async def editguild(ctx, oldguildname, newguildname):
    await ctx.send("Edit Guild "+oldguildname+" to "+newguildname);
    
@client.command(pass_contect=True)
async def removeguild(ctx, *, guildname):
    await ctx.send("remove guild from db "+guildname);
    
@client.command(pass_contect=True)
async def register(ctx, charName, guild, charClass, tier, mem):
    await ctx.send("register the member with the following: "+charName+" , "+guild+" , "+charClass+" , "+tier+" , "+mem);
    
@client.command(pass_contect=True)
async def update(ctx, charName, guild, charClass, tier, mem):
    await ctx.send("update the member with the following: "+charName+" , "+guild+" , "+charClass+" , "+tier+" , "+mem);
    
@client.command(pass_contect=True)
async def default(ctx, charName,  mem):
    await ctx.send("set the follow character as default "+charName+" , "+mem);
    
@client.command(pass_contect=True)
async def remove(ctx, charName, mem):
    await ctx.send("remove the following character: "+charName+" , "+mem);
    
@client.command(pass_contect=True)
async def whois(ctx, *, charName):
    await ctx.send("returns the owner of : "+charName);

@client.command(pass_contect=True)
async def classes(ctx):
    classes = ['Berserker', 'Gunlancer', 'Paladin', 'Destroyer', 'Deadeye', 'Sharpshooter', 'Artillerist', 'Scouter', 'Gunslinger', 'Wardancer', 'Scrapper', 'Striker', 'Soulfist', 'Lance Master', 'Summoner', 'Bard', 'Arcana', 'Sorceress', 'Deathblade'];
    await ctx.send("Class List: ");

    for x in range(len(classes)):
      await ctx.send(classes[x]);

@client.command(pass_contect=True)
async def tiers(ctx):
    tier_list = ['N/A', 'T1', 'T2', 'T3']
    await ctx.send("Tier List: ");

    for x in range(len(tier_list)):
      await ctx.send(tier_list[x]);
    
client.run(token)