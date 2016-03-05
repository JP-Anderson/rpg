# Test Main
from settings import *
from character import Character
from csvreader import CsvReader
from weapon import Weapon
from armour import Armour
from battle import Battle


class TestMain:

	print("LOADING!")
	print("  Loading Characters")
	print("    - Bob")
	bob = Character(endurance=25)
	bob.strength = 10
	bob.agility = 1
	bob.speed = 2
	
	
	print("    - orc1")
	
	orc1 = Character(name="orc1")
	orc1.agility = 13
	orc1.speed = 3
	
	orc2 = Character(name="orc2")
	orc2.speed=12
	
	
	orc3 = Character(name="orc3")
	orc3.speed=1
	
	
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
	
	
	
	bob.weapon = weapons[11]
	bob.equipArmour(armour[3])
	bob.equipArmour(armour[4])
	bob.equipArmour(armour[5])
	bob.getEquipmentLoad()
	
	orc1.weapon = weapons[7]
	orc1.equipArmour(armour[0])
	orc1.equipArmour(armour[1])
	orc1.equipArmour(armour[2])
	
	print(orc1.getDamageResistances())
	orc1.getEquipmentLoad()

	#battle = Battle([bob], [orc2, orc1, orc3])
	
	battle = Battle([bob], [orc2, orc1, orc3])
	
	#for i in range (0,4):
	#	print()
	#	orc1.defend(bob.attack())
	#	print()
	#	orc2.defend(bob.attack())
	
	