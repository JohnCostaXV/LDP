import discord
import asyncio

async def ex(args, message, client, invoke):
    guild = message.server.id
    user = message.mentions[0]
    await client.ban(user)
    await client.send_message(message.channel, "👌 {}#{} foi banido com sucesso".format(user.name, user.discriminator))
