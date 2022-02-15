from discord.ext import commands
from replit import db

class Guilds(commands.Cog, name="Guilds"):
  """Commmands for Guilds"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  @commands.command(pass_contect=True)
  async def addguild(self, ctx: commands.Context, guildname):
      if guildname:
        if guildname in db.keys():
          await ctx.send("This guild has already been added");
        else:
            db[guildname] = guildname;
            await ctx.send(guildname+" Has been added!");
      else:
        await ctx.send("Please enter in Guild Name.");
      
  @commands.command(pass_contect=True)
  async def editguild(self, ctx: commands.Context, oldguildname, newguildname):
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
      
  @commands.command(pass_contect=True)
  async def removeguild(self, ctx: commands.Context, *, guildname):
      if guildname:
        if guildname in db.keys():
          del db[guildname];
          await ctx.send(guildname+" has been deleted!");
        else:
          await ctx.send("No guild name "+guildname+" found!");
      else:
        await ctx.send("Please enter in Guild Name.");

def setup(bot: commands.Bot):
  bot.add_cog(Guilds(bot));