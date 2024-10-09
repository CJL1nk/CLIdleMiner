
class Gear:

	def __init__(self, name, bps, luck, function):

		self.name = name
		self.bps = bps
		self.luck = luck

		self.function = function

	def getName(self):
		return self.name

	def getBPS(self):
			return self.bps

	def getLuck(self):
		return self.luck

	def killGearFunction():
		pass

	def startFunction(self):
		self.function()


def fragrhence():
    # do stuff
    pass


def anotherGear():
    pass


gears = {
	"fragrhence": Gear("Fragrhence", 0, 0.1, fragrhence)
}
