# Test Main
from settings import *
from character import Character
from utils.csvreader import CsvReader
from items.weapon import Weapon
from items.armour import Armour
from combat.battle import Battle
from skills.targets import *
from utils.loader import Weapons


class TestMain:

	print("LOADING!")
	
	weapons = Weapons()
	wep_list = weapons.list()
	numberOfObjects = len(wep_list)
	print("  Loading Weapons")
	for i in range (1, numberOfObjects):
		print("    - " + str(wep_list[i]))
	
	armourcsv = CsvReader.read("..\\data\\armour.csv")
	keys = armourcsv[0]
	numberOfObjects = len(armourcsv)
	armour = []
	print("  Loading Armour")
	for i in range (1,numberOfObjects):
		armour.append(Armour(keys,armourcsv[i]))
		print("    - " + str(armourcsv[i][1]))
		
	
	print("  Loading Characters")
	print("    - Bob")
	bob = Character(endurance=25, dexterity=50, isPlayable=True)
	bob.strength = 10
	bob.agility = 8
	bob.speed = 2
	bob.abilityList.addAbility(MasterHeal())	
	
	bob.weapon = wep_list[3]
	bob.equipArmour(armour[3])
	bob.equipArmour(armour[4])
	bob.equipArmour(armour[5])
	bob.getEquipmentLoad()
	
	bill = Character(endurance=25, dexterity=20, isPlayable=True)
	bill.strength = 80
	bill.agility = 19
	bill.speed = 10
	bill.name="Bill"
	
	bill.weapon = wep_list[6]
	bill.equipArmour(armour[0])
	bill.equipArmour(armour[1])
	bill.equipArmour(armour[2])
	bill.getEquipmentLoad()
	bill.abilityList.addAbility(EMPBlast())
	
	print("    - synth1")
	
	synth1 = Character(name="synth1", endurance=39, isPlayable=False, humanity=0.0)
	synth1.agility = 13
	synth1.speed = 3
	
	synth2 = Character(name="synth2", endurance=10, speed=25, agility=25, isPlayable=False, humanity=0.3)
	synth2.speed=12
	
	
	synth3 = Character(name="synth3", isPlayable=False, humanity=0.6)
	synth3.speed=1
	
	synth1.weapon = wep_list[7]
	synth1.equipArmour(armour[0])
	synth1.equipArmour(armour[1])
	synth1.equipArmour(armour[2])
	
	print(synth1.getDamageResistances())
	synth1.getEquipmentLoad()
	
	synth2.weapon = wep_list[4]
	synth3.weapon = wep_list[9]

	#battle = Battle([bob], [synth2, synth1, synth3])
	
	battle = Battle([bob, bill], [synth2, synth1])
	
	#for i in range (0,4):
	#	print()
	#	synth1.defend(bob.attack())
	#	print()
	#	synth2.defend(bob.attack())
	
	