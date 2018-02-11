
import discord
import json

def get_avatar(user)
    if user.avatar_url:
        avatar = user.avatar_url
    else:
        avatar = user.default_avatar_url
    
    return avatar

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'W') as fp:
        json.dump(data, fp)