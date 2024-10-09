
class Pickaxe:

	def __init__(self, name, bps, recipe):

		self.name = name
		self.bps = bps
		self.recipe = recipe

	def getName(self):
		return self.name

	def getBPS(self):
			return self.bps

pickaxes = {
    "the pickaxe": Pickaxe("The Pickaxe", 5, {"Soakite": 1}),

	"the drill": Pickaxe("The Drill", 15, {"Silver": 1,
                                        	"Amber": 30,
                                         	"Iron": 1000,
                                          	"Copper": 1250,
                                           	"Stone": 40000}),

 	"parallaxe": Pickaxe("Parallaxe", 30, {"Paralite": 1,
											"Platinum": 1,
											"Gold": 5,
											"Titanium": 5,
											"Calcium": 70,
											"Pyrite": 140,
											"Lithium": 200,
											"Quartz": 15000,
											"Obsidian": 450000})
}



