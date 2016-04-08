# game launcher class
from settings import *

import utils.state as State
from utils.characterfactory import CharacterFactory
from character import Character

from combat.mission import Mission
from combat.battle import Battle
from skills.targets import *

class Launcher:
	
	print("Launching")
	State.loadCSVs()
	m1 = Mission(1,4)
	m1.toString()
	
	cf = CharacterFactory()
	character1 = cf.build()
	character2 = cf.build()
	"""
	print("Creating characters.")
	
	print("    - Bob")
	bob = Character(endurance=25, dexterity=50, isPlayable=True)
	bob.strength = 10
	bob.agility = 8
	bob.speed = 2
	bob.abilityList.addAbility(MasterHeal())	
	
	bob.weapon = State.weapons[3]
	bob.equipArmour(State.armour[3])
	bob.equipArmour(State.armour[4])
	bob.equipArmour(State.armour[5])
	bob.getEquipmentLoad()
	
	bill = Character(endurance=25, dexterity=20, isPlayable=True)
	bill.strength = 80
	bill.agility = 19
	bill.speed = 10
	bill.name="Bill"
	
	bill.weapon = State.weapons[6]
	bill.equipArmour(State.armour[0])
	bill.equipArmour(State.armour[1])
	bill.equipArmour(State.armour[2])
	bill.getEquipmentLoad()
	bill.abilityList.addAbility(EMPBlast())
	"""
	for i in range (0,4):
		print("Battle " + str(i+1))
		battle = Battle([character1,character2], m1.stages[i])
	