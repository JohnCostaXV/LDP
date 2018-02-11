import asyncio
import aiohttp
import discord

async def ex(args, message, client, invoke):
    teste = message.author.server_permissions
    print(teste)