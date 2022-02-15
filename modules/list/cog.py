from discord.ext import commands

class Lists(commands.Cog, name="Lists"):
  """Commands for Lists"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  @commands.command(pass_contect=True)
  async def classes(self, ctx: commands.Context):
      classes = ['Berserker', 'Gunlancer', 'Paladin', 'Destroyer', 'Deadeye', 'Sharpshooter', 'Artillerist', 'Scouter', 'Gunslinger', 'Wardancer', 'Scrapper', 'Striker', 'Soulfist', 'Lance Master', 'Summoner', 'Bard', 'Arcana', 'Sorceress', 'Deathblade'];
      await ctx.send("Class List: ");
  
      for x in range(len(classes)):
        await ctx.send(classes[x]);
  
  @commands.command(pass_contect=True)
  async def tiers(self, ctx: commands.Context):
      tier_list = ['N/A', 'T1', 'T2', 'T3']
      await ctx.send("Tier List: ");
  
      for x in range(len(tier_list)):
        await ctx.send(tier_list[x]);

def setup(bot: commands.Bot):
  bot.add_cog(Lists(bot));