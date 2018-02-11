import discord
from utils.language import Language

async def ex(args, message, client, invoke):
    lang = args[0]
    if not args:
        return
    await client.send_message(Language.set_language(message.server, lang))
