# base weapon class
from settings import *
from combat.attack import Attack

class Weapon:

	def __init__(self, keyRow, valueRow):
		#print ("we are here")
		self.type = ObjectType.WEAPON
		numberOfKeys = len(keyRow)
		self.values = {}
		#print (numberOfKeys)
		for i in range(0, numberOfKeys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i]])

	def toString(self):
		print(self.values)
	
	def attack(self, strength, dexterity):
		baseDamage = int(self.values["BaseD"])
		if self.values["StrB"] != "-":
			strBonusDamage = int(self.values["StrB"]) * strength
			baseDamage = baseDamage + strBonusDamage
			print("Adding " + str(strBonusDamage) + " bonus strength damage!!!!!!!!!!!!!!")
		if self.values["DexB"] != "-":
			dexBonusDamage = int(self.values["DexB"]) * dexterity
			baseDamage = baseDamage + dexBonusDamage
			print("Adding " + str(dexBonusDamage) + " bonus dexterity damage!!!!!!!!!!!!!!")
		#Need to take weapon skill for this weapon from attacker
		
		attack = Attack(baseDamage,
						self.values["ShkD"],
						self.values["BrnD"],
						self.values["PsnD"],
						self.values["Dodgeability"],
						self.values["BaseCritC"],
						self.values["CritD"],
						self.values["Name"])
		return attack