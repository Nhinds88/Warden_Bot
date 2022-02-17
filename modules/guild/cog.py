from discord.ext import commands
from replit import db

class Guilds(commands.Cog, name="Guilds"):
  """Commmands for Guilds"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  if 'guilds' in db.keys():
    pass;
  else:
    db['guilds'] = [];

  @commands.command(pass_contect=True, brief='Adds the guild “guildname” to the database.', description='Adds the guild “guildname” to the database.')
  async def addguild(self, ctx: commands.Context, guildname):
      guildList = db['guilds'];
      if guildname:
        if guildname in guildList:
          await ctx.send("This guild has already been added");
        else:
            db['guilds'].append(guildname);
            await ctx.send(guildname+" Has been added!");
      else:
        await ctx.send("Please enter in Guild Name.");
      
  @commands.command(pass_contect=True, brief='Edits the guild “guildname” in the database.', description='Edits the guild “guildname” in the database.')
  async def editguild(self, ctx: commands.Context, oldguildname, newguildname):
      guildLists = db['guilds'];
      if oldguildname:
        if newguildname:
          if oldguildname in guildLists:
            guildLists.remove(oldguildname);
            del db['guilds'];
            guildLists.append(newguildname);
            db['guilds'] = guildLists;
            await ctx.send("Guild "+oldguildname+" has been edited to "+newguildname);
          else:
            await ctx.send("No Guild named "+oldguildname+" found!");
        else:
          await ctx.send("Please enter in New Guild Name.");
      else:
        await ctx.send("Please enter in Old Guild Name.");
      
  @commands.command(pass_contect=True, brief='Removes the guild “guildname” from the database.', description='Removes the guild “guildname” from the database.')
  async def removeguild(self, ctx: commands.Context, *, guildname):
      guildList = db['guilds'];
      if guildname:
        if guildname in guildList:
          del db['guilds'];
          guildList.remove(guildname);
          db['guilds'] = guildList;
          await ctx.send(guildname+" has been deleted!");
        else:
          await ctx.send("No guild name "+guildname+" found!");
      else:
        await ctx.send("Please enter in Guild Name.");

def setup(bot: commands.Bot):
  bot.add_cog(Guilds(bot));