# Test Main

from character import Character
from csvreader import CsvReader
from weapon import Weapon
from armour import Armour
from settings import *

class TestMain:

	print("LOADING!")
	print("  Loading Characters")
	print("    - Bob")
	bob = Character(endurance=20)
	print("    - Jim")
	jim = Character(name="Jim")
	bob.strength = 10
	bob.agility = 1
	bob.speed = 2
	
	jim.agility = 13
	jim.speed = 3
	
	weaponcsv = CsvReader.read("wep.csv")
	keys = weaponcsv[0]
	numberOfObjects = len(weaponcsv)
	weapons = []
	print("  Loading Weapons")
	for i in range (1,numberOfObjects):
		weapons.append(Weapon(keys,weaponcsv[i]))
		print("    - " + str(weaponcsv[i][1]))
	
	armourcsv = CsvReader.read("armour.csv")
	keys = armourcsv[0]
	numberOfObjects = len(armourcsv)
	armour = []
	print("  Loading Armour")
	for i in range (1,numberOfObjects):
		armour.append(Armour(keys,armourcsv[i]))
		print("    - " + str(armourcsv[i][1]))
	
	
	print(str(type(armour[3])))
	bob.weapon = weapons[2]
	bob.equipArmour(armour[3])
	bob.equipArmour(armour[4])
	bob.equipArmour(armour[5])
	
	print(bob.getDamageResistances())
	
	bob.getEquipmentLoad()
	
	jim.weapon = weapons[7]
	jim.equipArmour(armour[0])
	jim.equipArmour(armour[1])
	jim.equipArmour(armour[2])
	
	print(jim.getDamageResistances())
	jim.getEquipmentLoad()
	

	for i in range (0,40):
		print()
		jim.defend(bob.attack())
		print()
		bob.defend(jim.attack())
	
	
	