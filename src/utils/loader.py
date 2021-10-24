# loader
from utils.csvreader import CsvReader
from items.weapon import  Weapon
from items.armour import Armour

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

class Armours:

    def __init__(self):
        armour_csv = CsvReader.read("..\\data\\armour.csv")
        keys = armour_csv[0]
        numberOfObjects = len(armour_csv)
        self.armour = []
        print("  Loading Armour")
        for i in range (1, numberOfObjects):
            self.armour.append(Armour(keys, armour_csv[i]))
            print("    - " + str(armour_csv[i][1]))

    def list(self):
        return self.armour
