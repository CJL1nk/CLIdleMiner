from ores import Ore

class Layer:

	def __init__(self, name, ores):
		self.name = name
		self.ores = ores

	def getName(self):
		return self.name

	def getOres(self):
		return self.ores

world1Layers = {
    "Stone": Layer("Stone",
	[
    Ore("Astatine", 100000000),
    Ore("Promethium", 67045000),
    Ore("Xenonite", 22202000),
    Ore("Black Opal", 15000000),
    Ore("Diamond", 1000000),
    Ore("Unirite", 312000),
    Ore("Lauranium", 158600),
    Ore("Silver", 50400),
    Ore("Goron", 14000),
    Ore("Cobalt", 5666),
    Ore("Nickel", 3490),
    Ore("Amber", 1000),
    Ore("Tin", 300),
    Ore("Lead", 110),
    Ore("Iron", 55),
    Ore("Copper", 40),
    Ore("Coal", 25),
    Ore("Stone", 1),
	]),
	"Andesite": Layer("Andesite",
	[
    Ore("Phantasmium", 812000000),
    Ore("Ghosterium", 166666667),
    Ore("Kaleidium", 30300000),
    Ore("Actinium", 15000000),
    Ore("Bromine", 5800000),
    Ore("Bismuth", 2300000),
    Ore("Vanadium", 789000),
    Ore("Osmium", 100100),
    Ore("Titanium", 60000),
    Ore("Palladium", 21012),
    Ore("Calcium", 4500),
    Ore("Potassium", 2300),
    Ore("Lithium", 1515),
    Ore("Gallium", 250),
    Ore("Sodium", 200),
    Ore("Zinc", 65),
    Ore("Manganese", 50),
    Ore("Quartz", 20),
    Ore("Andesite", 1),
	]),
	"Obsidian": Layer("Obsidian",
	[
    Ore("Altum Aurum", 777777777),
    Ore("Tanzanite", 540000000),
    Ore("Plamenium", 290070092),
    Ore("Heli'ite", 48340000),
    Ore("Caesium", 10700000),
    Ore("Citrilarum", 5330000),
    Ore("Red Beryl", 3550000),
    Ore("Platinum", 450000),
    Ore("Helium Membrane", 346000),
    Ore("Gold", 99000),
    Ore("Pele's Hair", 15800),
    Ore("Palagonite", 7000),
    Ore("Pyrite", 3400),
    Ore("Crying Obsidian", 950),
    Ore("Snowflake Obsidian", 450),
    Ore("Apache Tear", 180),
    Ore("Sideromelane", 65),
    Ore("Tachylite", 60),
    Ore("Pumice", 30),
    Ore("Obsidian", 1),
	]),
 	"Bedrock": Layer("Bedrock",
	[
    Ore("Death Granule", 320101000),
    Ore("Terrasperite", 50232000),
    Ore("Kinerethium", 43090000),
    Ore("Drainhelion", 28000000),
    Ore("Lorilal", 24000000),
    Ore("Dhinsophite", 18750000),
    Ore("Hematitium", 16450000),
    Ore("Bleeding Paralite", 12500000),
    Ore("Frosted Paralite", 10250000),
    Ore("Blazing Paralite", 8500000),
    Ore("Paralite", 5000000),
    Ore("Julearus", 2300000),
    Ore("Rhenium", 1700000),
    Ore("Lapis Lazuli", 230000),
    Ore("Maroonstone", 78200),
    Ore("Occularite", 12000),
    Ore("Angorstone", 300),
    Ore("Philistone", 10),
    Ore("Bedrock", 1),
	]),
  	"Upper Mantle": Layer("Upper Mantle",
	[
    Ore("Pure Lonsdaleite", 900000000),
    Ore("Crystal Kalamite", 430000000),
    Ore("Lonsdaleite", 255000000),
    Ore("Viscous Kalamite", 58750000),
    Ore("Sphere of Harmony", 32000000),
    Ore("Ubiquitite", 15000000),
    Ore("Granadite", 7650000),
    Ore("Neptunium", 3200000),
    Ore("Plutonium", 1430000),
    Ore("Francium", 690000),
    Ore("Protactinium", 430300),
    Ore("Lutetium", 255000),
    Ore("Tungsten", 160000),
    Ore("Praseodymium", 76540),
    Ore("Thorium", 54000),
    Ore("Neodymium", 20780),
    Ore("Rubidium", 8600),
    Ore("Phosphorus", 2750),
    Ore("Uranium", 1430),
    Ore("Antimony", 730),
    Ore("Indium", 560),
    Ore("Iridium", 180),
    Ore("Vanadium", 150),
    Ore("Calcite", 50),
    Ore("Graphite", 30),
    Ore("Upper Mantle", 1),
	]),
   	"Lower Mantle": Layer("Lower Mantle",
	[
    Ore("Diamane", 850500000),
    Ore("Graphene", 200000000),
    Ore("Amorphous Kalamite", 64750000),
    Ore("Sphere of Discord", 32000000),
    Ore("Ukihnite", 18500000),
    Ore("Hytravium", 6700000),
    Ore("Wasdeite", 4500000),
    Ore("Holmium", 2350000),
    Ore("Hafnium", 850000),
    Ore("Samarium", 570800),
    Ore("Ytterbium", 480000),
    Ore("Erbium", 230000),
    Ore("Gadolinium", 95600),
    Ore("Niobium", 45000),
    Ore("Gallium", 18950),
    Ore("Nitrogite", 12670),
    Ore("Strontium", 3400),
    Ore("Flourine", 1250),
    Ore("Chlorine", 680),
    Ore("Sulfur", 430),
    Ore("Chromium", 200),
    Ore("Aluminum", 120),
    Ore("Phosphite", 40),
    Ore("Silicon", 25),
    Ore("Lower Mantle", 1),
	]),
    "Core": Layer("Core",
	[
    Ore("Aeternus", 1500000000),
    Ore("Acherium", 616000616),
    Ore("Tartarite", 313000313),
    Ore("Molten Kalamite", 86750000),
    Ore("Sphere of Resonance", 32000000),
    Ore("Devil's Blood", 6660666),
    Ore("Life Granule", 3201010),
    Ore("Beaststone", 610016),
    Ore("Drakeon", 137500),
    Ore("Hellfire Gem", 66666),
    Ore("Praulitite", 4120),
    Ore("Blaze Gem", 1750),
    Ore("Criticalium", 430),
    Ore("Swelterite", 100),
    Ore("Flame Gem", 85),
    Ore("Effervenscence", 25),
    Ore("Molten Silicate", 15),
    Ore("Core", 1),
	])
}
