# Tutorial here: https://www.youtube.com/watch?v=qwz5pSgFhrE

import discord
from discord.ext import commands

token = "MTEwMzMyNDQzODc0NjkwMjU0OA.G7n1Wc.7tH3z8FCIwzfn3GsgIcXgebsdUISLJibkR7G_M"
prefix = "-"
message_id = 1104070089801728150
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Add roles
@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "🟣" and payload.message_id ==  message_id:        #Pubg
        role = discord.utils.get(guild.roles, name="Pubg Mobile")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
    if payload.emoji.name == "🟡" and payload.message_id ==  message_id:        #Pubg
        role = discord.utils.get(guild.roles, name="Gamers™")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
    if payload.emoji.name == "🟢" and payload.message_id ==  message_id:        #Pubg
        role = discord.utils.get(guild.roles, name="Minecraft")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
    if payload.emoji.name == "🔵" and payload.message_id ==  message_id:        #Pubg
        role = discord.utils.get(guild.roles, name="CS:GO™")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
    if payload.emoji.name == "🟤" and payload.message_id ==  message_id:        #Pubg
        role = discord.utils.get(guild.roles, name="CRMP-SAMP")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
    if payload.emoji.name == "🟠" and payload.message_id ==  message_id:        #Pubg
        role = discord.utils.get(guild.roles, name="Valorant")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
# Remove roles
@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "🟣" and payload.message_id == message_id:          #Pubg
        role = discord.utils.get(guild.roles, name="Pubg Mobile")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
    if payload.emoji.name == "🟡" and payload.message_id == message_id:          #Pubg
        role = discord.utils.get(guild.roles, name="Gamers™")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
    if payload.emoji.name == "🟢" and payload.message_id == message_id:          #Pubg
        role = discord.utils.get(guild.roles, name="Minecraft")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
    if payload.emoji.name == "🔵" and payload.message_id == message_id:          #Pubg
        role = discord.utils.get(guild.roles, name="CS:GO™")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
    if payload.emoji.name == "🟤" and payload.message_id == message_id:          #Pubg
        role = discord.utils.get(guild.roles, name="CRMP-SAMP")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
    if payload.emoji.name == "🟠" and payload.message_id == message_id:          #Pubg
        role = discord.utils.get(guild.roles, name="Valorant")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

# Sends message with reaction
@bot.command()
async def react(ctx):
    message = """
    Rollar olish uchun U
    🟡 - Gamers™
    🟢 - Minecraft
    🟣 - Pubg Mobile
    🔵 - CS:GO™
    🟤 - CRMP-SAMP
    🟠 - Valorant
    """
    react_messasge = await ctx.send(message)
    await react_messasge.add_reaction(emoji="🟡")
    await react_messasge.add_reaction(emoji="🟢")
    await react_messasge.add_reaction(emoji="🟣")
    await react_messasge.add_reaction(emoji="🔵")
    await react_messasge.add_reaction(emoji="🟤")
    await react_messasge.add_reaction(emoji="🟠")
bot.run(token)