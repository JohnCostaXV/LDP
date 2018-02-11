import discord


async def ex(args, message, client, invoke):

    await client.send_message(message.channel, "Pong!")