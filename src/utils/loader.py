# loader
from utils.csvreader import CsvReader
from items.weapon import  Weapon


class Weapons:
	
	def __init__(self, path_prefix=""):
		weaponcsv = CsvReader.read(path_prefix+"data\\wep.csv")
		keys = weaponcsv[0]
		number_of_objects = len(weaponcsv)
		self.weapons = []
		print("  Loading Weapons")
		for i in range (1, number_of_objects):
			self.weapons.append(Weapon(keys, weaponcsv[i]))
			print("    - " + str(weaponcsv[i][1]))
	
	def list(self):
		return self.weapons