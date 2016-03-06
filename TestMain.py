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
	bob = Character(endurance=25, dexterity=50, isPlayable=True)
	bob.strength = 10
	bob.agility = 8
	bob.speed = 2
	
	
	print("    - orc1")
	
	orc1 = Character(name="orc1", isPlayable=False)
	orc1.agility = 13
	orc1.speed = 3
	
	orc2 = Character(name="orc2", isPlayable=False)
	orc2.speed=12
	
	
	orc3 = Character(name="orc3", isPlayable=False)
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
	
	
	
	bob.weapon = weapons[3]
	bob.equipArmour(armour[3])
	bob.equipArmour(armour[4])
	bob.equipArmour(armour[5])
	bob.getEquipmentLoad()
	
	bill = Character(endurance=25, dexterity=20, isPlayable=True)
	bill.strength = 80
	bill.agility = 19
	bill.speed = 10
	bill.name="Bill"
	
	bill.weapon = weapons[6]
	bill.equipArmour(armour[0])
	bill.equipArmour(armour[1])
	bill.equipArmour(armour[2])
	bill.getEquipmentLoad()
	
	orc1.weapon = weapons[7]
	orc1.equipArmour(armour[0])
	orc1.equipArmour(armour[1])
	orc1.equipArmour(armour[2])
	
	print(orc1.getDamageResistances())
	orc1.getEquipmentLoad()
	
	orc2.weapon = weapons[4]
	orc3.weapon = weapons[9]

	#battle = Battle([bob], [orc2, orc1, orc3])
	
	battle = Battle([bob, bill], [orc2, orc1])
	
	#for i in range (0,4):
	#	print()
	#	orc1.defend(bob.attack())
	#	print()
	#	orc2.defend(bob.attack())
	
	