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
    print('We have logged in as {0.user}'.format(client));
    
@client.command(pass_contect=True)
async def addguild(ctx, guildname):
    if guildname in db.keys():
      await ctx.send("This guild has already been added")
    else:
        db[guildname] = guildname;
        await ctx.send(guildname+" Has been added!");
    
@client.command(pass_contect=True)
async def editguild(ctx, oldguildname, newguildname):
    if oldguildname in db.keys():
      del db[oldguildname];
      db[newguildname] = newguildname;
      await ctx.send("Guild "+oldguildname+" has been edited to "+newguildname);
    else:
      await ctx.send("No Guild named "+oldguildname+" found!");
    
@client.command(pass_contect=True)
async def removeguild(ctx, *, guildname):
    if guildname in db.keys():
      del db[guildname];
      await ctx.send(guildname+" has been deleted!");
    else:
      await ctx.send("No guild name "+guildname+" found!");
    
@client.command(pass_contect=True)
async def register(ctx, charName, guild, charClass, tier, mem):
    if charName in db.keys():
      await ctx.send("your character has already been added.");
    else:
      db[charName] = [charName, guild, charClass, tier, mem];
      await ctx.send(charName+" has been addded!");
    
@client.command(pass_contect=True)
async def update(ctx, oldCharName, charName, guild, charClass, tier, mem):
    if oldCharName in db.keys():
      del db[oldCharName];
      db[charName] = [charName, guild, charClass, tier, mem];
      await ctx.send(charName+" has been updated!");
    else:
      await ctx.send("No character "+charName+" found.");
    
@client.command(pass_contect=True)
async def default(ctx, charName,  mem):
    if charName in db.keys():
      db[mem] = [charName, mem, "default"];
      await ctx.send("Your default is set, "+mem);
    else:
      await ctx.send(charName+" not found, please register your character first.");
    
@client.command(pass_contect=True)
async def remove(ctx, charName, mem):
    if charName in db.keys():
      del db[charName];
      if mem in db.keys():
        del db[mem];
      await ctx.send(charName+" deleted!");
    else:
      await ctx.send(charName+" Not Found!");
    
@client.command(pass_contect=True)
async def whois(ctx, *, charName):
    if charName in db.keys():
      charProf = db[charName]
      await ctx.send(charName+" is "+charProf[4]);
    else:
      await ctx.send(charName+" Not found!");

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