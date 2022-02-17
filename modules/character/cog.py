from discord.ext import commands
from replit import db

class Character(commands.Cog, name="Character"):
  """Character Commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot;

  @commands.command(pass_contect=True, brief='Registers a character to the users profile.', description='Registers a character to the users profile. Guild to be selected from a list. Class and Tier to be selected from a list.')
  async def register(self, ctx: commands.Context, character_name, guild, character_class, tier, discord_username):
      guildLists = db['guilds'];
      classes = db['classes'];
      tiers = db['tiers'];
      if character_name:
        if guild:
          if guild in guildLists:
            pass;
          else:
            await ctx.send("Please add guild before registering character. See /guilds to check registered guilds.");
            return;
          if character_class:
            if character_class in classes:
              pass;
            else:
              await ctx.send("Please use one of the offical class names. See /classes for offical names.");
              return;
            if tier:
              if tier in tiers:
                pass;
              else:
                await ctx.send("Please use one of the offical tiers. See /tiers for offical tier list.");
                return;
              if discord_username:
                if character_name in db.keys():
                  await ctx.send("your character has already been added.");
                else:
                  db[character_name] = [character_name, guild, character_class, tier, discord_username];
                  await ctx.send(character_name+" has been addded!");
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
  async def update(self, ctx: commands.Context, old_character_name, character_name, guild, character_class, tier, discord_username):
      guildLists = db['guilds'];
      classes = db['classes'];
      tiers = db['tiers'];
      if old_character_name:
        if character_name:
          if guild:
            if guild in guildLists:
              pass;
            else:
              await ctx.send("Please add guild before registering character. See /guilds to check registered guilds.");
              return;
            if character_class:
              if character_class in classes:
                pass;
              else:
                await ctx.send("Please use one of the offical class names. See /classes for offical names.");
                return;
              if tier:
                if tier in tiers:
                  pass;
                else:
                  await ctx.send("Please use one of the offical tiers. See /tiers for offical tier list.");
                  return;
                if discord_username:
                  if old_character_name in db.keys():
                    del db[old_character_name];
                    db[character_name] = [character_name, guild, character_class, tier, discord_username];
                    await ctx.send(character_name+" has been updated!");
                  else:
                    await ctx.send("No character "+character_name+" found.");
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
  async def default(self, ctx: commands.Context, character_name,  discord_username):
      if character_name:
        if discord_username:
          if character_name in db.keys():
            db[discord_username] = [character_name, discord_username, "default"];
            await ctx.send("Your default is set, "+discord_username);
          else:
            await ctx.send(character_name+" not found, please register your character first.");
        else:
          await ctx.send("Please enter in Username.");
      else:
        await ctx.send("Please enter in Character name.");
      
  @commands.command(pass_contect=True, brief='Removes a character from a users profile.', description='Removes a character from a users profile.')
  async def remove(self, ctx: commands.Context, character_name, discord_username):
      if character_name:
        if discord_username:
          if character_name in db.keys():
            del db[character_name];
            if discord_username in db.keys():
              del db[discord_username];
            await ctx.send(character_name+" deleted!");
          else:
            await ctx.send(character_name+" Not Found!");
        else:
          await ctx.send("Please enter in Username.");
      else:
        await ctx.send("Please enter in Character name.");
      
  @commands.command(pass_contect=True, brief='Returns who owns a character.', description='Returns who owns a character.')
  async def whois(self, ctx: commands.Context, *, character_name = None):
      if character_name:
        if character_name in db.keys():
          charProf = db[character_name]
          await ctx.send(character_name+" is "+charProf[4]);
        else:
          await ctx.send(character_name+" Not found!");
      else:
        await ctx.send("please enter in a characters name.");

def setup(bot: commands.Bot):
  bot.add_cog(Character(bot));