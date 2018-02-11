import time
import discord
import asyncio
import datetime

async def ex(args, message, client, invoke):

    #Antes de tudo vamos ver se o usuario tem as permissões nescessarias
    mperms = message.author.server_permissions

    if mperms.kick_members == True:
       

        user = message.mentions[0]
        # Vamos verificar se o usuario já esta no banco
    
        overwrite = message.channel.overwrites_for(user) or \
        discord.PermissionOverwrite()
        overwrite.send_messages = False
        await client.edit_channel_permissions(
            message.channel,
            user,
            overwrite
        )        
        tempo = args[1]        
        timesquad = int(tempo)
        reallytime = "{}".format(datetime.timedelta(seconds=timesquad))

        await client.send_message(message.channel, "👌 {}#{} foi mutado com sucesso, duração: {}".format(user.name, user.discriminator, reallytime))
        time.sleep(timesquad)


        overwrite = message.channel.overwrites_for(user) or \
        discord.PermissionOverwrite()
        overwrite.send_messages = True
        await client.edit_channel_permissions(
            message.channel,
            user,
            overwrite
        )
        