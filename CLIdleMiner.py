# slend
import sys
sys.path.append("src")

import threading
import json
import os
import time
import random
import json

from funcs import getOreData, getGearData, getPickaxeData, getPlayerData, saveFile
from pickaxes import pickaxes
from worlds import worlds

oreInventory = getOreData()
totalBlocksMined = getPlayerData()["totalBlocksMined"]

def main():

	exit = False

	while not exit:
		menu()


def menu():

	userInput = -1

	options = {
		1: mine,
		2: displayOreInventory,
		3: pickaxeInventory,
		4: gearInventory,
		5: shop,
		0: exit
	}

	os.system("cls")
	print("\n 1. Start Mining")
	print(" 2. Ore Inventory")
	print(" 3. Pickaxes")
	print(" 4. Gears")
	print(" 5. Shop")
	print(" 0. Save and Exit\n")

	while not 0 <= userInput <= 5:
		try:
			userInput = int(input("\n >> "))
			if not 0 <= userInput <= 5:
				print(" Invalid option!")
		except ValueError:
			print(" Invalid option!")
			userInput = -1

	options[userInput]()


def mine():

	activeWorld, activeLayer = selectWorld()
	activePickaxe = setActivePickaxe()

	# had to redeclare here because threading is tism
	totalBlocksMined = getPlayerData()["totalBlocksMined"]

	os.system("cls")

	ores = activeLayer.getOres()

	stop = False

	def mainLoop():

		global totalBlocksMined

		while not stop:

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

		with open(saveFile, 'r') as file:
			data = json.load(file)

		data["ores"] = oreInventory
		data["player"]["totalBlocksMined"] = totalBlocksMined

		with open(saveFile, 'w') as file:
			json.dump(data, file, indent=4)

	thread = threading.Thread(target=mainLoop)
	thread.start()

	input("\n Press enter to stop mining...\n\n")
	stop = True
	time.sleep( 1 / activePickaxe.getBPS() + 0.1) # to prevent extra print


def displayOreInventory():

	os.system("cls")

	print(f"\n {getPlayerData()['totalBlocksMined']} blocks mined\n")

	for ore, count in getOreData().items():
		print(f" {ore}: {count}")

	input("\n ...")


def pickaxeInventory():

	os.system("cls")
	print("\n")

	for pickaxe in getPickaxeData():
		print(f" {pickaxe}")

	input("\n ...")


def gearInventory():

	os.system("cls")
	print("\n")

	for gear in getGearData():
		print(f" {gear}")

	input("\n ...")


def shop():

	os.system("cls")
	print("\n")

	userInput = 0

	print(" 1. Pickaxe Shop")
	print(" 2. Gear shop")

	while not 1 <= userInput <= 2:
		try:
			userInput = int(input("\n >> "))
			if not 1 <= userInput <= 2:
				print(" Invalid option!")
		except ValueError:
			print(" Invalid option!")
			userInput = 0

	print("\n")

	if (userInput == 1):

		for pickaxe in pickaxes:
			if pickaxe not in (pick.lower() for pick in getPickaxeData()):
				print(pickaxe)

	input("\n ...")


def setActivePickaxe():

	os.system("cls")

	pickaxeSelected = False
	activePickaxe = None

	print("\n Select a pickaxe:\n")
	for pick in getPickaxeData():
			print(f" {pick}")

	while not pickaxeSelected:

		userPickaxe = input("\n >> ").lower()

		if userPickaxe in (pick.lower() for pick in getPickaxeData()):

			activePickaxe = pickaxes.get(userPickaxe)
			if activePickaxe:
				pickaxeSelected = True
		else:
			print(" Invalid pickaxe!")

	return activePickaxe


def selectWorld():

	worldSelected = False
	layerSelected = False

	activeWorld = None
	activeLayer = None

	os.system("cls")
	print("\n Select a World:\n")

	for world in worlds:
		print(f" {world}")

	while not worldSelected:

		userWorld = input("\n >> ").lower()

		activeWorld = worlds.get(userWorld)

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

	return activeWorld, activeLayer


def exit():
	sys.exit()


if __name__ == "__main__":
	main()
