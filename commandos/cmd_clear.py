import discord
import asyncio
import calendar
import time

async def ex(args, message, client, invoke):

    mperms = message.author.server_permissions
    
    if mperms.administrator == True:
        number = min(int(args[0]), 1000)
        if number < 1:
            return

        def predicate(message):
            timestamp = calendar.timegm(message.timestamp.timetuple())
            now = time.time()

            LIMIT = now - (3600 * 24 * 14)
            return timestamp > LIMIT

        deleted_messages = await client.purge_from(
            message.channel,
            limit=100,
            check=predicate
        )

        message_number = max(len(deleted_messages) - 1, 0)

        delete = True

        if message_number == 0:
            resp = "Eu não posso fazer isso por conta de uma limitação do discord"
            delete = False
        else:
           resp = "👌 Deletado {} message{} ".format(message_number,
                                                         "" if message_number <\
                                                            2 else "s")


        confirm_message = await client.send_message(message.channel, resp)

        if delete:
            await asyncio.sleep(8)
            await client.delete_message(confirm_message)
    else:
        await client.send_message(message.channel, "<:error:384111227648999434> Você não pode fazer isso!")

 
