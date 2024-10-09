import json
import os

saveFile = f"{os.getcwd()}\\SaveData\\data.json"

# I don't wanna hear it I know
def getPlayerData():
    with open (saveFile, 'r') as file:
        data = json.load(file)

    return data.get("player")

def getOreData():

    with open (saveFile, 'r') as file:
        data = json.load(file)

    return data.get("ores")

def getPickaxeData():

    with open (saveFile, 'r') as file:
        data = json.load(file)

    return data.get("pickaxes")

def getGearData():

    with open (saveFile, 'r') as file:
        data = json.load(file)

    return data.get("gears")

def saveData():
    pass
