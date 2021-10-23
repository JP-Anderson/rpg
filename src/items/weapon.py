# base weapon class
from settings import *
from combat.attack import Attack

class Weapon:

	def __init__(self, keyRow, valueRow):
		#print ("we are here")
		self.type = ObjectType.WEAPON
		number_of_keys = len(keyRow)
		self.values = {}
		#print (number_of_keys)
		for i in range(0, number_of_keys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i]])

	def to_string(self):
		print(self.values)
	
	def attack(self, strength, dexterity):
		base_dmg = int(self.values["BaseD"])
		if self.values["StrB"] != "-":
			str_bonus_dmg = int(self.values["StrB"]) * strength
			base_dmg = base_dmg + str_bonus_dmg
			print("Adding " + str(str_bonus_dmg) + " bonus strength damage!!!!!!!!!!!!!!")
		if self.values["DexB"] != "-":
			dex_bonus_dmg = int(self.values["DexB"]) * dexterity
			base_dmg = base_dmg + dex_bonus_dmg
			print("Adding " + str(dex_bonus_dmg) + " bonus dexterity damage!!!!!!!!!!!!!!")
		#Need to take weapon skill for this weapon from attacker
		
		attack = Attack(base_dmg,
						self.values["ShkD"],
						self.values["BrnD"],
						self.values["PsnD"],
						self.values["Dodgeability"],
						self.values["BaseCritC"],
						self.values["CritD"],
						self.values["Name"])
		return attack