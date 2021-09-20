# loader
from utils.csvreader import CsvReader
from items.weapon import  Weapon


class Weapons:
	
	def __init__(self):
		weaponcsv = CsvReader.read("..\\data\\wep.csv")
		keys = weaponcsv[0]
		numberOfObjects = len(weaponcsv)
		self.weapons = []
		print("  Loading Weapons")
		for i in range (1, numberOfObjects):
			self.weapons.append(Weapon(keys, weaponcsv[i]))
			print("    - " + str(weaponcsv[i][1]))
	
	def list(self):
		return self.weapons
