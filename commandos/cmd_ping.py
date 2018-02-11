import discord


async def ex(args, message, client, invoke):
<<<<<<< HEAD

    await client.send_message(message.channel, "Pong!")
=======
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Argumentos: %s*" % args.__str__()[1:-1].replace("'", "")
    await client.send_message(message.channel, "Pong!" + args_out)
>>>>>>> 078b07368765b7e1cb0784986305ebd934bada8e
