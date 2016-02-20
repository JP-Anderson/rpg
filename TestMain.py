# Test Main

from character import Character
from csvreader import CsvReader
from weapon import Weapon
from settings import *

class TestMain:

	bob = Character()
	jim = Character(name="Jim")
	
	print(bob.strength)
	
	bob.strength = 10
	bob.agility = 1
	bob.speed = 2
	
	jim.agility = 13
	jim.speed = 3
	print(bob.strength)
	
	
	weaponcsv = CsvReader.read("wep.csv")
	keys = weaponcsv[0]
	print(keys)
	numberOfObjects = len(weaponcsv)
	print(numberOfObjects)
	weapons = []
	
	for i in range (1,numberOfObjects):
		weapons.append(Weapon(keys,weaponcsv[i]))

	print("Weapons: "+str(len(weapons)))
	
	bob.weapon = weapons[0]
	jim.weapon = weapons[7]

	for i in range (0,14):
		print()
		jim.defend(bob.attack())
		print()
		bob.defend(jim.attack())