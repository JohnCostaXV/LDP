import discord
import asyncio
<<<<<<< HEAD
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
=======


async def ex(args, message, client, invoke):

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
        return

    cleared = 0
    failed = 0

    async for m in client.logs_from(message.channel, limit=ammount):
        try:
            await client.delete_message(m)
            cleared += 1
        except:
            failed += 1
            pass

    failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""
    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
    await asyncio.sleep(4)
    await client.delete_message(returnmsg)
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e

 
