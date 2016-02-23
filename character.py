# character base class
import random

from settings import *
from weapon import Weapon
from armour import Armour

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
		
		self.maxHP = 200+endurance*50
		self.hp = self.maxHP
		self.status = 1
		self.maxAP = 2*speed+2*agility
		self.ap = self.maxAP
		
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
		else: 
			#attack.stats()
			resistances = self.getDamageResistances()
			phD = (1-resistances["PhysD"])*float(attack.baseD)
			print("Physical damage..."+str(phD) + " out of " + str(attack.baseD))
			shD = (1-resistances["ShkD"])*float(attack.shkD)
			print("Shock damage......"+str(shD) + " out of " + str(attack.shkD))
			buD = (1-resistances["BrnD"])*float(attack.brnD)
			print("Burn damage......."+str(buD) + " out of " + str(attack.brnD))
			poD = (1-resistances["PsnD"])*float(attack.psnD)
			print("Poison damage....."+str(poD) + " out of " + str(attack.psnD))
			totalDamage = int(phD + shD + buD + poD)
			print("Total............." + str(totalDamage))
			#print(str(sum(resistances)))
			#print(str((1-sum(resistances))*totalDamage))
			self.hp = self.hp-totalDamage
			print(self.name + " has " + str(self.hp) + "/" + str(self.maxHP) + " left.")
			if self.hp < 0:
				print(self.name + " has died.")
				self.status = 0
			else: 
				print(self.name + " has " + str(self.hp) + " left.")
		

	def equipArmour(self, armour):
		if ObjectType(int(armour.values["Slot"])) == ObjectType.HELMET: 
			print("Setting " + armour.values["Name"] + " as a helmet.")
			self.helmet = armour
		elif ObjectType(int(armour.values["Slot"])) == ObjectType.CHEST:
			print("Setting " + armour.values["Name"] + " as chest.")
			self.chestArmour = armour
		elif ObjectType(int(armour.values["Slot"])) == ObjectType.LEGS:
			print("Setting " + armour.values["Name"] + " as a legs.")
			self.legArmour = armour
	
	def getEquipmentLoad(self):
		equipmentLoad = 0
		print(self.name + " Equipment Load")
		
		if self.weapon.type == ObjectType.WEAPON:
			weight = int(self.weapon.values["Weight"])
			equipmentLoad = equipmentLoad + weight
			if PRINT_DETAILED_STATS == True: 
				print(self.weapon.values["Name"] + " -- " + self.weapon.values["Weight"])
		
		if self.helmet.type == ObjectType.HELMET:
			weight = int(self.helmet.values["Weight"])
			equipmentLoad = equipmentLoad + weight
			if PRINT_DETAILED_STATS == True: 
				print(self.helmet.values["Name"] + " -- " + self.helmet.values["Weight"])
		
		if self.chestArmour.type == ObjectType.CHEST:
			if PRINT_DETAILED_STATS == True: 
				print(self.chestArmour.values["Name"] + " -- " + self.chestArmour.values["Weight"])
				#print(str(self.chestArmour.values["Weight"])+" "+self.chestArmour.values("Name"))
			weight = int(self.chestArmour.values["Weight"])
			equipmentLoad = equipmentLoad + weight
		
		if self.legArmour.type == ObjectType.LEGS:
			if PRINT_DETAILED_STATS == True: 
				print(self.legArmour.values["Name"] + " -- " + self.legArmour.values["Weight"])
				#print(str(self.legArmour.values["Weight"])+" "+self.legArmour.values("Name"))
			weight = int(self.legArmour.values["Weight"])
			equipmentLoad = equipmentLoad + weight
		
		print(equipmentLoad)
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
	