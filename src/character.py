# character base class
import random

from settings import *
from items.weapon import Weapon
from items.armour import Armour
from skills.abilitylist import AbilityList

class Character:

	#Use the utils/CharacterCreator class to create a Character
	def __init__(self,
				name="Bob",
				level=1,
				strength=7,
				dexterity=7,
				endurance=7,
				intelligence=7,
				agility=7,
				speed=7,
				humanity=1.0,
				is_playable=True,
				char_class = Class.FIGHTER
				):
		self.name = name
		self.level = level
		self.char_class = char_class
		self.strength = strength
		self.dexterity = dexterity
		self.endurance = endurance
		self.intelligence = intelligence
		self.agility = agility
		self.speed = speed
		self.humanity = humanity
		self.is_playable = is_playable
		self.ability_list = AbilityList()
		
		self.max_hp = BASE_HEALTH + endurance*20
		self.hp = self.max_hp
		self.status = Status.NORMAL
		self.maxAP = self.setMaxAP()
		self.startAP = self.maxAP-2
		self.ap = self.startAP
		self.xp = 0
		
		self.weapon = None
		self.terminal = None
	
	def attack(self):
		if self.weapon != None:
			text = self.name + " attacks with the " + self.weapon.values["Name"] + "!"
			print("-"*len(text))
			print(text)
			self.ap = self.ap - int(self.weapon.values["ShotAP"])
			return self.weapon.attack(self.strength, self.dexterity)
		else: return None
	
	def defend(self, attack):
		dodgeRoll = random.random()
		dodgeChance = 0.1+self.agility*0.02+self.speed*0.01
		dodgeChance2 = dodgeChance * float(attack.dodge)
		if PRINT_DETAILED_STATS == True:
			print(self.name + " needs to roll " + str(dodgeChance) + " or less...")
			print("Agility " + str(0.02*self.agility) + "  +  Speed " + str(0.01*self.speed) + "  + 0.2")
			print("Dodgeability applied " + str(dodgeChance2))
			print("Rolls " + str("%.3f" % dodgeRoll) + ".")
		if dodgeRoll <= dodgeChance: print(self.name + " dodges.")
		else: 
			#attack.stats()
			resistances = self.getDamageResistances()
			phD = (1-resistances["PhysD"])*float(attack.base_dmg)
			print("Physical damage..."+str(phD) + " out of " + str(attack.base_dmg))
			shD = (1-resistances["ShkD"])*float(attack.shock_dmg)
			print("Shock damage......"+str(shD) + " out of " + str(attack.shock_dmg))
			buD = (1-resistances["BrnD"])*float(attack.burn_dmg)
			print("Burn damage......."+str(buD) + " out of " + str(attack.burn_dmg))
			poD = (1-resistances["PsnD"])*float(attack.poison_dmg)
			print("Poison damage....."+str(poD) + " out of " + str(attack.poison_dmg))
			totalDamage = int(phD + shD + buD + poD)
			print("Total............." + str(totalDamage))
			#print(str(sum(resistances)))
			#print(str((1-sum(resistances))*totalDamage))
			self.adjust_health(-totalDamage)
	
	def adjust_health(self, health_change):
		if health_change < 0:
			self.hp = self.hp + health_change
			if self.hp <= 0:
				print(self.name + " has died.")
				self.die()
				return
		else:
			self.hp = self.hp + health_change
			if self.hp > self.max_hp:
				self.hp = self.max_hp
		print(self.name + " has " + str(self.hp) + "/"+ str(self.max_hp) +" health remaining.")
	
	def use_ability(self, abilityChoice, target):
		self.ability_list.use_ability(abilityChoice, target)
		abilityCost = self.ability_list.abilities[abilityChoice].ap_cost
		self.ap = self.ap - abilityCost
	
	def equipArmour(self, armour):
		if armour.slot == ArmourSlot.HEAD: 
			print("Setting " + armour.values["Name"] + " as a helmet.")
			self.helmet = armour
		elif armour.slot == ArmourSlot.CHEST:
			print("Setting " + armour.values["Name"] + " as chest.")
			self.chestArmour = armour
		elif armour.slot == ArmourSlot.LEGS:
			print("Setting " + armour.values["Name"] + " as a legs.")
			self.legArmour = armour
	
	def equipWeapon(self, weapon):
		if weapon.type == ObjectType.WEAPON:
			self.weapon = weapon
	
	def equipTerminal(self, terminal):
		if terminal.type == ObjectType.TERMINAL:
			self.terminal = terminal
	
	def getEquipmentLoad(self):
		equipmentLoad = 0
		self.maxCarryWeight = CARRY_WEIGHTS_BY_ENDURANCE[self.endurance]
		
		print(self.name + " Equipment Load")
		
		if self.weapon.type == ObjectType.WEAPON:
			weight = int(self.weapon.values["Weight"])
			equipmentLoad = equipmentLoad + weight
			if PRINT_DETAILED_STATS == True: 
				print(self.weapon.values["Name"] + " -- " + self.weapon.values["Weight"])
		
		if self.helmet.type == ObjectType.ARMOUR:
			weight = int(self.helmet.values["Weight"])
			equipmentLoad = equipmentLoad + weight
			if PRINT_DETAILED_STATS == True: 
				print(self.helmet.values["Name"] + " -- " + self.helmet.values["Weight"])
		
		if self.chestArmour.type == ObjectType.ARMOUR:
			if PRINT_DETAILED_STATS == True: 
				print(self.chestArmour.values["Name"] + " -- " + self.chestArmour.values["Weight"])
				#print(str(self.chestArmour.values["Weight"])+" "+self.chestArmour.values("Name"))
			weight = int(self.chestArmour.values["Weight"])
			equipmentLoad = equipmentLoad + weight
		
		if self.legArmour.type == ObjectType.ARMOUR:
			if PRINT_DETAILED_STATS == True: 
				print(self.legArmour.values["Name"] + " -- " + self.legArmour.values["Weight"])
				#print(str(self.legArmour.values["Weight"])+" "+self.legArmour.values("Name"))
			weight = int(self.legArmour.values["Weight"])
			equipmentLoad = equipmentLoad + weight
		
		encumbrancePerc = equipmentLoad/self.maxCarryWeight
		self.encumbrance = Encumbrance.MED
		if encumbrancePerc <= EncumbranceThreshold.LOW.value:
			self.encumbrance = Encumbrance.LOW
		elif encumbrancePerc > EncumbranceThreshold.HIGH.value:
			self.encumbrance = Encumbrance.HIGH
		
		print(str(equipmentLoad) + " CURRENT LOAD")
		print(str(self.maxCarryWeight) + " MAX LOAD")
		print(encumbrancePerc)
		print(str(self.encumbrance))
		return equipmentLoad
	
	def getDamageResistances(self):
		damageResistances = {}
		for damageType in ["PhysD","ShkD","BrnD","PsnD"]:
			damageResistances[damageType] = 0
			if self.helmet is not None:
				#print(self.helmet.values["Name"] + " has a " + damageType + " damage of " + self.helmet.values[damageType])
				damageResistances[damageType] = damageResistances[damageType] + float(self.helmet.values[damageType])
			if self.chestArmour is not None:
				damageResistances[damageType] = damageResistances[damageType] + float(self.chestArmour.values[damageType])
			if self.legArmour is not None:
				damageResistances[damageType] = damageResistances[damageType] + float(self.legArmour.values[damageType])
		
		return damageResistances
		
	def die(self):
		self.status = Status.DEAD
		##  :(
	
	def is_dead(self):
		if self.status == Status.DEAD: return True
		else: return False
	
	def setMaxAP(self):
		agilityAndSpeed = self.agility + self.speed
		if agilityAndSpeed < 12: return 5
		elif agilityAndSpeed < 18: return 6
		elif agilityAndSpeed < 21: return 7
		elif agilityAndSpeed < 30: return 8
		elif agilityAndSpeed < 40: return 9
		elif agilityAndSpeed < 52: return 10
		elif agilityAndSpeed < 65: return 11
		else: return 12
	
	def printStats(self):
		print(self.name)
		print(str(self.level))
		print(str(self.strength) + " " + str(self.dexterity) + " " + str(self.endurance) + " " + str(self.agility)  + " " + str(self.speed) + " " + str(self.humanity))
		
		print("HP " + str(self.hp) + "/" + str(self.max_hp))
		print("AP " + str(self.ap) + "/" + str(self.maxAP))
		if self.weapon != None:
			print(self.weapon.values["Name"] + " equipped")
	
	def gain_xp(self, xp):
		self.xp = self.xp + xp
		while self.xp >= self.xp_to_next_level():
			remainder = self.xp - self.xp_to_next_level()
			print("level up 1")
			self.level_up()
			self.xp = remainder
	
	def xp_to_next_level(self):
		return XP_PER_LEVEL[self.level-1]
	
	def level_up(self):
		self.level = self.level + 1
	
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
	
