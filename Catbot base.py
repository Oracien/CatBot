import discord
from asyncio import *
import io
import champions
from discord.ext import commands
import random

bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), description ="@CatBot help")

champions.create_all()
champions.update_all()

#client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command(pass_context=True, description="Update pictures")
async def update(ctx, character:str=""):
    if (character == ""):
        champions.update_all()
        await bot.say("Updated albums of all champions")
    else:
        character = character.lower()
        if character in champions.list_of_champion_objects:
            champions.list_of_champion_objects[character].update()
            await bot.say("Updated album of " + character)
        else:
            await bot.say("No champion with that name")

@bot.command(pass_context=True, description="Get a single picture")
async def picture(ctx, character:str=""):
    try:
        name_champ = character.lower()
        image = champions.list_of_champion_objects[name_champ].random_picture()
        print("Retrieved Picture of " + character.title())
        await bot.say(image)
    except:
        await bot.say("Not able to retrieve a picture for the champion. Use /help for more info")

@bot.command(pass_context=True, description="Retrieve the link to the album")
async def album(ctx, character:str):
    try:
        name_champ = character.lower()
        album = champions.list_of_champion_objects[name_champ].album()
        print("Retrieved " + character.title() + "'s album link")
        await bot.say(album)
    except:
        await bot.say("Not able to retrieve the album link for the champion. Use /help for more info")


@bot.command(pass_context=False, description="Ahri needs your help")
async def Ahri():
    await bot.say("Ahri needs your help. Local foxgirls in YOUR area are looking for *caring* owners right now! Contact cutefoxgirls.com TODAY!")

@bot.command(pass_context=False, description="Ahri needs your help", hidden = True)
async def ahri():
    await bot.say("Ahri needs your help. Local foxgirls in YOUR area are looking for *caring* owners right now! Contact cutefoxgirls.com TODAY!")

@bot.command(pass_context=False, description="Syndra is the dark sovereign")
async def Syndra():
    await bot.say("Karina is my favourite summoner in all of the rift")

@bot.command(pass_context=False, description="Syndra is the dark sovereign", hidden = True)
async def syndra():
    await bot.say("Karina is my favourite summoner in all of the rift")

@bot.command(pass_context=True, description="Return list of pictures", hidden = True)
async def list_of_pictures(ctx, character:str):
    name_champ = character.lower()
    await bot.say((champions.list_of_champion_objects[name_champ]).list_of_pictures())



bot.run(#YourToken)
