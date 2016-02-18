# Test Main

from character import Character
from csvreader import CsvReader
from weapon import Weapon

class TestMain:

	bob = Character()
	jim = Character()
	
	
	bob.strength = 10
	print(bob.strength)
	
	
	weaponcsv = CsvReader.read("wep.csv")
	keys = weaponcsv[0]
	print(keys)
	numberOfObjects = len(weaponcsv)
	
	weapons = []
	
	for i in range (1,numberOfObjects):
		weapons.append(Weapon(keys,weaponcsv[i]))
	
	weapons[1].getValue['ID']
	