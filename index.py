import discord
import asyncio
from discord import Embed
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import config
# Comandos
from commandos import cmd_ping, cmd_clear, cmd_userinfo, cmd_ban, cmd_mute, cmd_set_mute_role

commandos = {

    "ping": cmd_ping,
    "clear": cmd_clear,
    "userinfo": cmd_userinfo,
    "ban": cmd_ban,
    "teste": cmd_set_mute_role,

}


client = discord.Client(game=discord.Game(name=f"Estou sem reniciar"))

# Prefixo do bot
prefix = "?"

class Object(object):
    pass

def init_funcs(client):
    # MySQL
    global cursor, engine, Session
    db = 'ldp_dev'
    engine = create_engine('mysql+pymysql://localhost/{}?charset=utf8mb4'.format(db), encoding='utf8')
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    client.mysql = Object()
    engine = client.mysql.engine = engine
    cursor = client.mysql.cursor = get_cursor


@property
def get_cursor(self):
    return Session()


@client.event
async def on_ready():
	#print("Eu estou vivo!")
	#print("Meu nome é {} e meu id foi definido como {}.".format(
	#	client.user.name, client.user.id))
    init_funcs(client)

@client.event
async def on_message(message):
    if message.content.startswith(config.PREFIX):
        invoke = message.content[len(config.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commandos.__contains__(invoke):
            await commandos.get(invoke).ex(args, message, client, invoke)

    def __init__(self, bot):
        self.bot = bot
@client.event
async def on_member_join(member):
    userid = member.id
    username = member.name
    discriminator = member.discriminator
    useravatar = member.avatar_url
    embed=discord.Embed(
        title=" ", 
        description="Olá <@{userid}>, seja bem vindo A Liga dos Programadores!", 
        color=0x7289da
    )
    embed.set_author(
        name="{username}#{discriminator}",
        icon_url=useravatar,
        )
    serverchannel = member.server.default_channel
    await client.send_message(client.get_channel("383418985443753988"),embed=embed)





    


client.run("") # Liga o bot


