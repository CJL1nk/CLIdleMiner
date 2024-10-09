import signal
import sys
import os
import time
import random
import json
from funcs import getPickaxeData, getGearData, getOreData, getPlayerData, saveFile
from worlds import worlds
from pickaxes import pickaxes


activePickaxe = None
activeWorld = None
activeLayer = None

totalBlocksMined = getPlayerData()["blocksMined"]
oreInventory = getOreData()

def save(signum, frame):

	with open(saveFile, 'r') as file:
		data = json.load(file)

	data["ores"] = oreInventory

	with open(saveFile, 'w') as file:
		json.dump(data, file, indent=4)

def setActivePickaxe():

	os.system("cls")

	pickaxeSelected = False

	print("\n Select a pickaxe:\n")
	for pick in getPickaxeData():
			print(f" {pick}")

	while not pickaxeSelected:

		userPickaxe = input("\n >> ").lower()

		if userPickaxe in (pick.lower() for pick in getPickaxeData()):

			activePickaxe = pickaxes.get(userPickaxe.capitalize())
			if activePickaxe:
				pickaxeSelected = True
		else:
			print(" Invalid pickaxe!")

def selectWorld():

	worldSelected = False
	layerSelected = False

	global activeWorld
	global activeLayer

	os.system("cls")
	print("\n Select a World:\n")

	for world in worlds:
		print(f" {world}")

	while not worldSelected:

		userWorld = input("\n >> ").lower()

		activeWorld = worlds.get(userWorld.capitalize())

		if activeWorld:
			if totalBlocksMined >= activeWorld.getBlocksMined():
				worldSelected = True
			else:
				print(f"You need at least {activeWorld.getBlocksMined()} blocks mined to enter this world.")
		else:
			print("Invalid world!")

	os.system("cls")
	print("\n Select a layer:\n")

	for layer in activeWorld.getLayers():
		print(f" {layer}")

	while not layerSelected:

		userLayer = input("\n >> ").lower()

		activeLayer = activeWorld.getLayers().get(userLayer.capitalize())
		if activeLayer:
			layerSelected = True
		else:
			print("Invalid layer!")


signal.signal(signal.SIGTERM, save)
signal.signal(signal.SIGINT, save)

try:
	def mine():

		os.system("cls")

		ores = activeLayer.getOres()
		global totalBlocksMined

		while True:

			time.sleep(1 / activePickaxe.getBPS())

			for i in range(3):

				for ore in ores:
					if random.randint(1, ore.getRarity()) == 1:
						ore.find()

						if ore.getName() in oreInventory:
							oreInventory[ore.getName()] += 1
						else:
							oreInventory[ore.getName()] = 1

						break

				totalBlocksMined += 1


except KeyboardInterrupt:
	save(signal.SIGINT, None)

selectWorld()
setActivePickaxe()
mine()
