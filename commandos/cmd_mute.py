import discord
import asyncio
import pymongo
from pymongo import MongoClient


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
    mongocli = MongoClient('localhost', 27017)
    print(mongocli)
    db = mongocli.clients
    collection = db['clients2']
    cursor = collection.find({})

    user = message.mentions[0]
    # Vamos verificar se o usuario já esta no banco
    if collection.find({"id": user.id, "server_id": message.server.id}).count() > 0:
        await client.send_message(message.channel, "Você não pode mutar um usuario que já esta mutado!")
    else:
        collection.insert({"nick": "{}".format(user.name), "id": "{}".format(user.id), "server_id": "{}".format(message.server.id)})
        overwrite = message.channel.overwrites_for(user) or \
        discord.PermissionOverwrite()
        overwrite.send_messages = False
        await client.edit_channel_permissions(
            message.channel,
            user,
            overwrite
        )
        await client.send_message(message.channel, "👌 {}#{} foi mutado com sucesso".format(user.name, user.discriminator))






