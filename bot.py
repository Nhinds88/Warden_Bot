import discord
from discord.ext import commands
from bot_server import bot_server
import os

def main():
  client = commands.Bot(command_prefix="/")
  token = 'xxx';
  
  @client.event
  async def on_ready():
      print('We have logged in as {0.user}'.format(client));

  # loading Cogs
  for folder in os.listdir("modules"):
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
      client.load_extension(f"modules.{folder}.cog");
  
  client.run(token);

if __name__== '__main__':
  bot_server()
  main()