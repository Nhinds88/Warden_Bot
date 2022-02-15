import discord
from discord.ext import commands
from replit import db

client = commands.Bot(command_prefix="/")
token = 'xxx';

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client));
    
@client.command(pass_contect=True)
async def addguild(ctx, guildname):
    if guildname:
      if guildname in db.keys():
        await ctx.send("This guild has already been added");
      else:
          db[guildname] = guildname;
          await ctx.send(guildname+" Has been added!");
    else:
      await ctx.send("Please enter in Guild Name.");
    
@client.command(pass_contect=True)
async def editguild(ctx, oldguildname, newguildname):
    if oldguildname:
      if newguildname:
        if oldguildname in db.keys():
          del db[oldguildname];
          db[newguildname] = newguildname;
          await ctx.send("Guild "+oldguildname+" has been edited to "+newguildname);
        else:
          await ctx.send("No Guild named "+oldguildname+" found!");
      else:
        await ctx.send("Please enter in New Guild Name.");
    else:
      await ctx.send("Please enter in Old Guild Name.");
    
@client.command(pass_contect=True)
async def removeguild(ctx, *, guildname):
    if guildname:
      if guildname in db.keys():
        del db[guildname];
        await ctx.send(guildname+" has been deleted!");
      else:
        await ctx.send("No guild name "+guildname+" found!");
    else:
      await ctx.send("Please enter in Guild Name.");
      
@client.command(pass_contect=True)
async def register(ctx, charName, guild, charClass, tier, mem):
    if charName:
      if guild:
        if charClass:
          if tier:
            if mem:
              if charName in db.keys():
                await ctx.send("your character has already been added.");
              else:
                db[charName] = [charName, guild, charClass, tier, mem];
                await ctx.send(charName+" has been addded!");
            else:
                await ctx.send("Please enter in Username.");
          else:
            await ctx.send("Please enter in Tier.");
        else:
          await ctx.send("Please enter in Character Class.");
      else:
        await ctx.send("Please enter in Guild.");
    else:
      await ctx.send("Please enter in New Character Name.");
    
@client.command(pass_contect=True)
async def update(ctx, oldCharName, charName, guild, charClass, tier, mem):
    if oldCharName:
      if charName:
        if guild:
          if charClass:
            if tier:
              if mem:
                if oldCharName in db.keys():
                  del db[oldCharName];
                  db[charName] = [charName, guild, charClass, tier, mem];
                  await ctx.send(charName+" has been updated!");
                else:
                  await ctx.send("No character "+charName+" found.");
              else:
                await ctx.send("Please enter in Username.");
            else:
              await ctx.send("Please enter in Tier.");
          else:
            await ctx.send("Please enter in Character Class.");
        else:
          await ctx.send("Please enter in Guild.");
      else:
        await ctx.send("Please enter in New Character Name.");
    else:
      await ctx.send("Please enter in Old Character Name.");
    
@client.command(pass_contect=True)
async def default(ctx, charName,  mem):
    if charName:
      if mem:
        if charName in db.keys():
          db[mem] = [charName, mem, "default"];
          await ctx.send("Your default is set, "+mem);
        else:
          await ctx.send(charName+" not found, please register your character first.");
      else:
        await ctx.send("Please enter in Username.");
    else:
      await ctx.send("Please enter in Character name.");
    
@client.command(pass_contect=True)
async def remove(ctx, charName, mem):
    if charName:
      if mem:
        if charName in db.keys():
          del db[charName];
          if mem in db.keys():
            del db[mem];
          await ctx.send(charName+" deleted!");
        else:
          await ctx.send(charName+" Not Found!");
      else:
        await ctx.send("Please enter in Username.");
    else:
      await ctx.send("Please enter in Character name.");
    
@client.command(pass_contect=True)
async def whois(ctx, *, charName = None):
    if charName:
      if charName in db.keys():
        charProf = db[charName]
        await ctx.send(charName+" is "+charProf[4]);
      else:
        await ctx.send(charName+" Not found!");
    else:
      await ctx.send("please enter in a characters name.");

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