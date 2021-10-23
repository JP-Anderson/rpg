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
from utils.state import *


class TestMain:

	print("LOADING!")
	load_csvs()
	wep_list = weapons
	armour_list = armours
	
	cf = CharacterCreator(free_stat_points=20)
	print("Create first character...")
	c1 = cf.build()
	print("Create second character...")
	c2 = cf.build()
	c1.ability_list.add_ability(MasterHeal())	
	c1.weapon = wep_list[3]
	c1.equipArmour(armour_list[3])
	c1.equipArmour(armour_list[4])
	c1.equipArmour(armour_list[5])
	c1.getEquipmentLoad()
	
	c2.weapon = wep_list[6]
	c2.equipArmour(armour_list[0])
	c2.equipArmour(armour_list[1])
	c2.equipArmour(armour_list[2])
	c2.getEquipmentLoad()
	c2.ability_list.add_ability(EMPBlast())
	
	
	mission = Mission(stage_count=4, weapons=weapons)
	
	for stage in mission.stages:
		battle = Battle([c1, c2], stage)
	