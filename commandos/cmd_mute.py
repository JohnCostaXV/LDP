import discord
import asyncio


#  overwrite = message.channel.overwrites_for(user) or \
        #discord.PermissionOverwrite()
      #  overwrite.send_messages = False
       # await client.edit_channel_permissions(
       #     message.channel,
        #    user,
        #    overwrite
        #)
        #await client.send_message(message.channel, "👌 {}#{} foi mutado com sucesso".format(user.name, user.discriminator))

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
        await client.send_message(message.channel, "👌 {}#{} foi mutado com sucesso".format(user.name, user.discriminator))






