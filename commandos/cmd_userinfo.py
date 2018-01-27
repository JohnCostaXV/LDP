import discord
import asyncio


async def ex(args, message, client, invoke):
    try:
        user = message.mentions[0]
        userjoinedat = str(user.joined_at).split('.', 1)[0]
        usercreatedat = str(user.created_at).split('.', 1)[0]

        embed = discord.Embed()

        embed.set_thumbnail(
            url =  user.avatar_url
        )
        embed.set_author(
            name = user.name,
            icon_url = user.avatar_url
        )

        embed.add_field(
            name="❯ User Information", 
            value='ID: {}   \nProfile: <@{}>\nCreated: {}'.format(user.id, user.id, usercreatedat))
        embed.add_field(
            name="❯ Member Information", 
            value='Joined: {}'.format(userjoinedat))
        
        await client.send_message(message.channel, embed=embed)
    except IndexError:
        await client.send_message(message.channel, "Can't get this user")
    


