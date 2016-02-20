# character base class
import random

from settings import *

class Character:

	def __init__(self,
				name="Bob",
				level=1,
				strength=7,
				dexterity=7,
				endurance=7,
				agility=7,
				speed=7,
				humanity=1.0
				):
		self.name = name
		self.level = level
		self.strength = strength
		self.dexterity = dexterity
		self.endurance = endurance
		self.agility = agility
		self.speed = speed
		self.humanity = humanity
		
		hp = 50+endurance*8
		ap = 2*speed+2*agility
		print("\"Hello, world!\" said "+name)
		
	def attack(self):
		if self.weapon != None:
			text = self.name + " attacks with the " + self.weapon.values["Name"] + "!"
			print("-"*len(text))
			print(text)
			return self.weapon.attack()
		else: return None
	
	def defend(self, attack):
		dodgeRoll = random.random()
		dodgeChance = 0.3+self.agility*0.02+self.speed*0.01
		if PRINT_DETAILED_STATS == True:
			print(self.name + " needs to roll " + str(dodgeChance) + " or less...")
			print("Rolls " + str("%.3f" % dodgeRoll) + ".")
		if dodgeRoll <= dodgeChance: print(self.name + " dodges.")
		else: attack.stats()
			
		

	# Stats
	
	#name = None
	#level = None
	
	#strength = None
	#dexterity = None
	#endurance = None
	#agility = None
	#speed = None
	#humanity = None
	
	#hp = None
	#ap = None
	
	# Equipment
	weapon = None
	helmet = None
	chestArmour = None
	legArmour = None
	