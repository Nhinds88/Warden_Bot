from discord.ext import commands
from replit import db

class Character(commands.Cog, name="Character"):
  """Character Commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  @commands.command(pass_contect=True, brief='Registers a character to the users profile.', description='Registers a character to the users profile. Guild to be selected from a list. Class and Tier to be selected from a list.')
  async def register(self, ctx: commands.Context, charName, guild, charClass, tier, mem):
      guildLists = db['guilds'];
      classes = db['classes'];
      tiers = db['tiers'];
      if charName:
        if guild:
          if guild in guildLists:
            pass;
          else:
            await ctx.send("Please add guild before registering character. See /guilds to check registered guilds.");
          if charClass:
            if charClass in classes:
              pass;
            else:
              await ctx.send("Please use one of the offical class names. See /classes for offical names.");
            if tier:
              if tier in tiers:
                pass;
              else:
                await ctx.send("Please use one of the offical tiers. See /tiers for offical tier list.");
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
      
  @commands.command(pass_contect=True, brief='Edits a character to the users profile.', description='Edits a character to the users profile. Guild to be selected from a list. Class and Tier to be selected from list.')
  async def update(self, ctx: commands.Context, oldCharName, charName, guild, charClass, tier, mem):
      guildLists = db['guilds'];
      classes = db['classes'];
      tiers = db['tiers'];
      if oldCharName:
        if charName:
          if guild:
            if guild in guildLists:
              pass;
            else:
              await ctx.send("Please add guild before registering character. See /guilds to check registered guilds.");
            if charClass:
              if charClass in classes:
                pass;
              else:
                await ctx.send("Please use one of the offical class names. See /classes for offical names.");
              if tier:
                if tier in tiers:
                  pass;
                else:
                  await ctx.send("Please use one of the offical tiers. See /tiers for offical tier list.");
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
      
  @commands.command(pass_contect=True, brief='Sets a character as the default (main) character in a users profile.', description='Sets a character as the default (main) character in a users profile.')
  async def default(self, ctx: commands.Context, charName,  mem):
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
      
  @commands.command(pass_contect=True, brief='Removes a character from a users profile.', description='Removes a character from a users profile.')
  async def remove(self, ctx: commands.Context, charName, mem):
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
      
  @commands.command(pass_contect=True, brief='Returns who owns a character.', description='Returns who owns a character.')
  async def whois(self, ctx: commands.Context, *, charName = None):
      if charName:
        if charName in db.keys():
          charProf = db[charName]
          await ctx.send(charName+" is "+charProf[4]);
        else:
          await ctx.send(charName+" Not found!");
      else:
        await ctx.send("please enter in a characters name.");

def setup(bot: commands.Bot):
  bot.add_cog(Character(bot));