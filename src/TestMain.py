# Test Main
from settings import *
from character import Character
from utils.csvreader import CsvReader
from utils.character_creator import CharacterCreator
from items.weapon import Weapon
from items.armour import Armour
from combat.battle import Battle
from combat.mission import Mission
from skills.targets import *
from utils.loader import Weapons


class TestMain:

	print("LOADING!")
	
	weapons = Weapons(path_prefix="..\\")
	wep_list = weapons.list()
	number_of_objects = len(wep_list)
	print("  Loading Weapons")
	for i in range (1, number_of_objects):
		print("    - " + str(wep_list[i]))
	
	armourcsv = CsvReader.read("..\\data\\armour.csv")
	keys = armourcsv[0]
	number_of_objects = len(armourcsv)
	armour = []
	print("  Loading Armour")
	for i in range (1,number_of_objects):
		armour.append(Armour(keys,armourcsv[i]))
		print("    - " + str(armourcsv[i][1]))
		
	

	cf = CharacterCreator(free_stat_points=20)
	print("Create first character...")
	c1 = cf.build()
	print("Create second 0character...")
	c2 = cf.build()
	c1.ability_list.add_ability(MasterHeal())	
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
	c2.ability_list.add_ability(EMPBlast())
	
	
	mission = Mission(stage_count=4, weapons=weapons)
	
	for stage in mission.stages:
		battle = Battle([c1, c2], stage)
	