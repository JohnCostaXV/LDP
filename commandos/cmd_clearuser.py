import discord
import calendar
import time
import asyncio

async def ex(args, message, client, invoke):


    mperms = message.author.server_permissions
    if mperms.manage_messages == True:
        if not message.mentions:
            embed=discord.Embed(title="Como usar", color=0xed1111)
            embed.set_image(url="https://media.giphy.com/media/l4pThpsSANlIQkVGg/giphy.gif")
            embed.add_field(name="O que esse comando faz?", value="Limpa as mensagens dos usuarios", inline=False)
            embed.add_field(name="Como usar?", value="?clearuser @user", inline=True)
            embed.set_footer(text="Fact #5: Sabia que o LDP foi totalmente inspirado no rowboat do mestre b1nzy")
            await client.send_message(message.channel, embed=embed)
            return
        user = message.mentions[0]
        if not user:
            embed=discord.Embed(title="Como usar", color=0xed1111)
            embed.set_image(url="https://media.giphy.com/media/l4pThpsSANlIQkVGg/giphy.gif")
            embed.add_field(name="O que esse comando faz?", value="Limpa as mensagens dos usuarios", inline=False)
            embed.add_field(name="Como usar?", value="?clearuser @user", inline=True)
            embed.set_footer(text="Fact #5: Sabia que o LDP foi totalmente inspirado no rowboat do mestre b1nzy")
            await client.send_message(message.channel, embed=embed)
            return

        def predicate(m):
            timestamp = calendar.timegm(m.timestamp.timetuple())
            now = time.time()

            LIMIT = now - (3600 * 24 * 14)

            return timestamp > LIMIT and (m.author.id == user.id or m == message)

        deleted_messages = await client.purge_from(
            message.channel,
            check=predicate
        )

        message_number = max(len(deleted_messages) - 1, 0)

        if message_number == 0:
            resp = "Deleted `0 message` 🙄  \n "
                      
        else:
            resp = " 👌 Deleted `{} message{}`  ".format(message_number,
                                                         "" if message_number <\
                                                            2 else "s")

        confirm_message = await client.send_message(
            message.channel,
            resp
        )

        await asyncio.sleep(8)
        await client.delete_message(confirm_message)
