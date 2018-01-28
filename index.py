import discord
import asyncio
from discord import Embed


import config
# Comandos
from commandos import cmd_ping, cmd_clear, cmd_userinfo, cmd_ban, cmd_mute

commandos = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "userinfo": cmd_userinfo,
    "ban": cmd_ban,
    "mute": cmd_mute,

}


client = discord.Client(game=discord.Game(name=f"Estou sem reniciar"))

# Prefixo do bot
prefix = "?"



@client.event
async def on_ready():


@client.event
async def on_message(message):
    if message.content.startswith(config.PREFIX):
        invoke = message.content[len(config.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commandos.__contains__(invoke):
            await commandos.get(invoke).ex(args, message, client, invoke)





    


client.run("") # Liga o bot


