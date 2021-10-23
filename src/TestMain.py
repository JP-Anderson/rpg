# Test Main
from settings import *
from character import Character
from utils.csvreader import CsvReader
from utils.characterfactory import CharacterFactory
from items.weapon import Weapon
from items.armour import Armour
from combat.battle import Battle
from skills.targets import *
from utils.loader import Weapons


class TestMain:

	print("LOADING!")
	
	weapons = Weapons(path_prefix="..\\")
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
		
	

	cf = CharacterFactory(free_stat_points=20)
	print("Create first character...")
	c1 = cf.build()
	print("Create second 0character...")
	c2 = cf.build()
	c1.abilityList.addAbility(MasterHeal())	
	c1.weapon = wep_list[3]
	c1.equipArmour(armour[3])
	c1.equipArmour(armour[4])
	c1.equipArmour(armour[5])
	c1.getEquipmentLoad()
	
	c2.weapon = wep_list[6]
	c2.equipArmour(armour[0])
	c2.equipArmour(armour[1])
	c2.equipArmour(armour[2])
	c2.getEquipmentLoad()
	c2.abilityList.addAbility(EMPBlast())
	
	print("    - synth1")
	
	synth1 = Character(name="synth1", endurance=39, is_playable=False, humanity=0.0)
	synth1.agility = 13
	synth1.speed = 3
	
	synth2 = Character(name="synth2", endurance=10, speed=25, agility=25, is_playable=False, humanity=0.3)
	synth2.speed=12
	
	
	synth3 = Character(name="synth3", is_playable=False, humanity=0.6)
	synth3.speed=1
	
	synth1.weapon = wep_list[7]
	synth1.equipArmour(armour[0])
	synth1.equipArmour(armour[1])
	synth1.equipArmour(armour[2])
	
	print(synth1.getDamageResistances())
	synth1.getEquipmentLoad()
	
	synth2.weapon = wep_list[4]
	synth3.weapon = wep_list[9]
	
	battle = Battle([c1, c2], [synth1, synth2])	
	