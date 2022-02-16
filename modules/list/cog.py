from discord.ext import commands
from replit import db

class Lists(commands.Cog, name="Lists"):
  """Commands for Lists"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  if 'classes' in db.keys():
    pass;
  else:
    db['classes'] = ['Berserker', 'Gunlancer', 'Paladin', 'Destroyer', 'Deadeye', 'Sharpshooter', 'Artillerist', 'Scouter', 'Gunslinger', 'Wardancer', 'Scrapper', 'Striker', 'Soulfist', 'Lance Master', 'Summoner', 'Bard', 'Arcana', 'Sorceress', 'Deathblade'];

  if 'tiers' in db.keys():
    pass;
  else:
    db['tiers'] = ['N/A', 'T1', 'T2', 'T3'];

  @commands.command(pass_contect=True, brief='List of classes.', description='List of classes in Lost Ark.')
  async def classes(self, ctx: commands.Context):
      classes = db['classes'];
      await ctx.send("Class List: ");
      for x in range(len(classes)):
        await ctx.send(classes[x]);
  
  @commands.command(pass_contect=True, brief='List of Tiers.', description='List of Tiers.')
  async def tiers(self, ctx: commands.Context):
      tier_list = db['tiers']
      await ctx.send("Tier List: ");
      for x in range(len(tier_list)):
        await ctx.send(tier_list[x]);

  @commands.command(pass_contect=True, brief='List of Guilds.', description='List of Guilds')
  async def guilds(self, ctx: commands.Context):
      guildList = db['guilds']
      await ctx.send("Guild List: ");
  
      for x in range(len(guildList)):
        await ctx.send(guildList[x]);

def setup(bot: commands.Bot):
  bot.add_cog(Lists(bot));