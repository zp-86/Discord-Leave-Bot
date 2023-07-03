import discord
from discord import app_commands

#The server id of the server you want to run the commands in
serverid=
#Paste your bot token below
Token = 'Bot Token Here'

server = discord.Object(id=serverid)
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=server)
        await self.tree.sync(guild=server)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))
    async for guild in client.fetch_guilds(limit=150):
        print(guild.name, guild.id)

@client.tree.command()
@app_commands.describe(
    sid='The server ID to leave'
)
async def leave(interaction: discord.Interaction, sid: str):
    to_leave = client.get_guild(int(sid))
    await to_leave.leave()
    await interaction.response.send_message(f'Left the server! ({sid})', ephemeral=True)

@client.tree.command()
async def guilds(interaction: discord.Interaction):
    guilds_info = []
    async for guild in client.fetch_guilds(limit=250):
        name_list = [str(name) for name in guild.name] if isinstance(guild.name, (list, tuple)) else [str(guild.name)]
        id_list = [str(id_) for id_ in guild.id] if isinstance(guild.id, (list, tuple)) else [str(guild.id)]
        name_str = ', '.join(name_list)
        id_str = ', '.join(id_list)
        guild_info = f"{name_str}, {id_str}"
        guilds_info.append(guild_info)

    message = '\n'.join(guilds_info)
    await interaction.response.send_message(message, ephemeral=True)




@client.tree.command()
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hi, {interaction.user.mention}', ephemeral=True)


@client.tree.command()
async def info(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Hey! This is a Discord bot that can leave servers made by user86, for commands use /cmds, to leave a server use /leave', ephemeral=True)


@client.tree.command()
async def cmds(interaction: discord.Interaction):
    await interaction.response.send_message(
        '/test - Is it working? \n '
        '/Info - Info about the bot \n '
        '/guilds - Shows all guilds the bot is in (Limit 250)', ephemeral=True)


client.run(Token)
