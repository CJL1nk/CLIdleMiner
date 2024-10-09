from layers import *

class World:

	def __init__(self, name, layers, blocksMined):
		self.name = name
		self.layers = layers
		self.blocksMined = blocksMined

	def getName(self):
		return self.name

	def getLayers(self):
		return self.layers

	def getBlocksMined(self):
		return self.blocksMined


worlds = {
    "ambermere": World("Ambermere", world1Layers, 0),
    "World 2": World("World 2", world1Layers, 1000000)
}

