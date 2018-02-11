import discord
import json

async def ex(args, message, client, invoke):
    roleid = args[0]
    path = './'
    fileName = 'teste.json'
    data = {}
    data['server'] = message.server.id
    data['roleid'] = roleid
    writeToJSONFile(data)


def writeToJSONFile(date):
    with open('teste.json', "a") as f:
        f.write(str(date))