import discord

async def ex(args, message, client, invoke):
    user = message.mentions[0]
    
<<<<<<< HEAD
    mperms = message.author.server_permissions
    if mperms.ban_members == True:
        try:
            await client.ban(user)
            await client.unban(client.get_server(message.server.id), user)
            await client.send_message(message.channel, "👌 {}#{} foi banido e teve suas mensagens limpas com sucesso".format(user.name, user.discriminator))
        except discord.HTTPException:
            await client.say("EROR")
=======
    
    try:
        await client.ban(user)
        await client.unban(client.get_server(message.server.id), user)
        await client.send_message(message.channel, "👌 {}#{} foi banido e teve suas mensagens limpas com sucesso".format(user.name, user.discriminator))
    except discord.HTTPException:
        await client.say("EROR")
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e
