### TODO
    # Create bot class
    # Add automatic channel decorations
    # Add suggestions
    # Add stats for the server

from discord import Intents, ChannelType, TextChannel, CategoryChannel
from discord.ext.commands import Bot, is_owner, command, Context
import asyncio

from settings import TOKEN


class Bot(Bot):
    def __init__(self):
        super().__init__(command_prefix='-', intents=Intents.all())
    
    async def setup_hook(self):
        print(f'{self.user.name} is offically online!')
        pass


bot = Bot()
tree = bot.tree

@command()
@is_owner()
async def sync(context:Context):
    msg = await context.send("Syncing..")
    await tree.sync()
    await msg.edit(content="Done!")




#🍃 
#🍂
# set channel names to emojis
# manual for now, will make automatic later
@bot.command()
@is_owner()
async def emoji_names(ctx:Context):
    guild = ctx.guild
    sorted_catagories = sorted([chan for chan in guild.channels if chan.type == ChannelType.category], key=lambda x:x.position)

    sorted_channels:list[TextChannel] = []
    for catagory in sorted_catagories:
        for channel in sorted(catagory.channels, key=lambda x:x.position):
            sorted_channels.append(channel)
    
  
    for index, channel in enumerate(sorted_channels):
        if channel.category.id == 1272662393306087554: continue

        name = f"🍃{channel.name}" if index % 2 else f"🍂{channel.name}"
        await channel.edit(name=name)
        asyncio.sleep(1)


    await ctx.send("Done!")

    



bot.run(TOKEN)