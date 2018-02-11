import discord
import asyncio
<<<<<<< HEAD
import time
import os
import random
import datetime
start_time = time.time()





=======
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e
from discord import Embed


import config
<<<<<<< HEAD


# Comandos
from commandos import cmd_ping, cmd_clear, cmd_userinfo, cmd_ban, cmd_mute, cmd_softban, cmd_clearuser, cmd_tempmute, cmd_help

=======
# Comandos
from commandos import cmd_ping, cmd_clear, cmd_userinfo, cmd_ban, cmd_mute
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e

commandos = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "userinfo": cmd_userinfo,
    "ban": cmd_ban,
    "mute": cmd_mute,
<<<<<<< HEAD
    "softban": cmd_softban,
    "clearuser": cmd_clearuser,
    "tempmute": cmd_tempmute,
    "help": cmd_help,
=======
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e

}


client = discord.Client(game=discord.Game(name=f"Estou sem reniciar"))

# Prefixo do bot
prefix = "?"



<<<<<<< HEAD

@client.event
async def on_ready():
	#print("Eu estou vivo!")
	#print("Meu nome é {} e meu id foi definido como {}.".format(
	#	client.user.name, client.user.id))
    mensecs = ['Fiquem seguros', 'Em fase de testes', 'Visiste meu webiste: www.ldpbot.xyz', 'Partner programs is tru']
    pegarandom = random.SystemRandom()
    await client.change_presence(game=discord.Game(name=pegarandom.choice(mensecs)))

    #print("Estou em " + str(len(client.servers)) + " servers")
    #for x in range(len(servers)):
       # print(' ' + servers[x-1].name)

=======
@client.event
async def on_ready():
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e


@client.event
async def on_message(message):
<<<<<<< HEAD

        
    if message.content.startswith(config.PREFIX):

        
=======
    if message.content.startswith(config.PREFIX):
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e
        invoke = message.content[len(config.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commandos.__contains__(invoke):
            await commandos.get(invoke).ex(args, message, client, invoke)
<<<<<<< HEAD
            livecmds = client.get_channel('410144656857366529')
            await client.send_message(livecmds, "`{} >` **{}**: `{}`".format(message.server.name, message.author.name, message.content))


@client.event
async def on_server_join(server):
    embed = discord.Embed()
    embed.title = 'SERVER JOIN'
    embed.set_author(name='{0} <{0.id}>'.format(server.owner), icon_url=server.owner.avatar_url)
    embed.add_field(name='Server', value='{0.name} <{0.id}>'.format(server))
    embed.add_field(name='Membros', value='**{0}**/{1}'.format(sum(1 for x in server.members if x.status == discord.Status.online or x.status == discord.Status.idle), len(server.members)))
    embed.color = discord.Color.green()
    embed.timestamp = datetime.datetime.now()
    member = await client.get_user_info('269520755287523329')
    await client.send_message(member, embed=embed)

@client.event
async def on_message_edit(before, after):


    if before.server.id == "383418985443753985":

        if before.channel.id == "409403579661811712":
            return
        if after.channel.id == "409403579661811712":
            return

        if len(before.embeds) == 1:
            print("yes embed")
            return
        if len(after.embeds) == 1:
            return


        print(len(before.embeds))
        print(len(after.embeds))
    
        embed=discord.Embed(title="⚠ Mensagem editada", description="Canal <#{}>".format(str(before.channel.id)), color=0xffff00)
        embed.set_author(name="{}".format(before.author.name), icon_url="{}".format(before.author.avatar_url))
        embed.add_field(name="Mensagem antiga", value="```{}```".format(before.content))
        embed.add_field(name="Mensagem nova", value="```{}```".format(after.content))
        chanellog = client.get_channel('409403579661811712')
        await client.send_message(chanellog, embed=embed)
    else:
        return


@client.event
async def on_message_delete(message):


    if message.server.id == "383418985443753985":
        embed=discord.Embed(title="⚠ Mensagem Deletada", description="Canal <#{}>".format(str(message.channel.id)), color=0xff0000)
        embed.set_author(name="{}".format(message.author.name), icon_url="{}".format(message.author.avatar_url))
        embed.add_field(name="Mensagem", value="```{}```".format(message.content))
        chanellog = client.get_channel('409403579661811712')
        await client.send_message(chanellog, embed=embed)
    else:
        return

client.run(".") # Liga o bot
=======





    


client.run("") # Liga o bot
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e


