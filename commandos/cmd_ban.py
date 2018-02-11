import discord
import asyncio

async def ex(args, message, client, invoke):
    guild = message.server.id
<<<<<<< HEAD

    if not message.mentions:
        embed=discord.Embed(title="Como usar", color=0xed1111)
        embed.set_image(url="https://media.giphy.com/media/l4pTepntuWzyqmfyo/giphy.gif")
        embed.add_field(name="O que esse comando faz?", value="Da ban em no usuario mencionado", inline=False)
        embed.add_field(name="Como usar?", value="?ban @user", inline=True)
        embed.set_footer(text="Fact #1: Sabia que só uma pessoa descobriu o significado de ldp?")
        await client.send_message(message.channel, embed=embed)
        return

    user = message.mentions[0]


    mperms = message.author.server_permissions
    if mperms.ban_members == True:
        await client.ban(user)
        await client.send_message(message.channel, "👌 {}#{} foi banido com sucesso".format(user.name, user.discriminator))
    else:
        await client.send_message(message.channel, "<:erro:326509900115083266> Você não pode fazer isso!")
=======
    user = message.mentions[0]
    await client.ban(user)
    await client.send_message(message.channel, "👌 {}#{} foi banido com sucesso".format(user.name, user.discriminator))
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e
