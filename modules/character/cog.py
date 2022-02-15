from discord.ext import commands
from replit import db

class Character(commands.Cog, name="Character"):
  """Character Commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  @commands.command(pass_contect=True)
  async def register(self, ctx: commands.Context, charName, guild, charClass, tier, mem):
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
      
  @commands.command(pass_contect=True)
  async def update(self, ctx: commands.Context, oldCharName, charName, guild, charClass, tier, mem):
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
      
  @commands.command(pass_contect=True)
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
      
  @commands.command(pass_contect=True)
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
      
  @commands.command(pass_contect=True)
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