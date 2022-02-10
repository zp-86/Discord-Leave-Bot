import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

from discord.ext.commands import Context

Token = 'Bot Token Here'

client = commands.Bot(command_prefix='$', description="This is a Leave Tool User#2987")


@client.event
async def on_ready():
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))
    async for guild in client.fetch_guilds(limit=150):
        print(guild.name, guild.id)


@client.command()
async def leave(ctx, arg):
    to_leave = client.get_guild(int(arg))
    await to_leave.leave()
    await ctx.reply('Left the server!', mention_author=True)



@client.command()
async def guilds(ctx):
    async for guild in client.fetch_guilds(limit=250):
        await ctx.send(guild.name)
        await ctx.send(guild.id)


@client.command()
async def test(ctx):
    await ctx.reply('Its working!', mention_author=True)


@client.command()
async def info(ctx):
    await ctx.reply('Hey! This is a Discord bot that can leave servers made by User#2987, for commands use $cmds, to leave a server use $leave',
                    mention_author=True)


@client.command()
async def cmds(ctx):
    await ctx.reply(
                    '$test - Is it working?  '
                    '$Info - Info about the bot'
                    '$guilds - Shows all guilds the bot is in (Limit 250)  ', mention_author=True)


client.run(Token)
