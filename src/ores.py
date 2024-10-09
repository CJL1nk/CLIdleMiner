import pygame
import os

class Ore:

	def __init__(self, name, rarity):
		self.name = name
		self.rarity = rarity
		self.count = 0

	def getName(self):
		return self.name

	def getRarity(self):
		return self.rarity

	def getCount(self):
		return self.count

	def find(self):

		pygame.mixer.init()

		self.count += 1

		if self.rarity > 85000:
			print(f" You have found {self.name}")

			if self.rarity >= 100000000:
				pygame.mixer.music.load(f"{os.getcwd()}\\src\\sfx\\unfathomable.wav")
				pygame.mixer.music.play()
			elif self.rarity >= 50000000 and self.rarity < 100000000:
				pygame.mixer.music.load(f"{os.getcwd()}\\src\\sfx\\enigmatic.wav")
				pygame.mixer.music.play()
			elif self.rarity > 15000000 and self.rarity < 50000000:
				pygame.mixer.music.load(f"{os.getcwd()}\\src\\sfx\\transcendant.wav")
				pygame.mixer.music.play()
			elif self.rarity > 7500000 and self.rarity < 15000000:
				pygame.mixer.music.load(f"{os.getcwd()}\\src\\sfx\\exquisite.wav")
				pygame.mixer.music.play()
			elif self.rarity >= 1000000 and self.rarity < 7500000:
				pygame.mixer.music.load(f"{os.getcwd()}\\src\\sfx\\exotic.wav")
				pygame.mixer.music.play()



