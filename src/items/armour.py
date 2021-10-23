# base armour class
from settings import *

class Armour:

	
	#lol
	def __init__(self, keyRow, valueRow):
		number_of_keys = len(keyRow)
		self.values = {}
		#print (number_of_keys)
		for i in range(0, number_of_keys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i
		
		self.type = ObjectType.ARMOUR
		self.slot = ArmourSlot(int(self.values["Slot"]))

	def to_string(self):
		print(self.values)
	
	def absorb_damage(self, attack):
		base_dmg = attack.base_dmg*self.values["PhysD"]
		shock_dmg = attack.shock_dmg*self.values["ShkD"]
		burn_dmg = attack.burn_dmg*self.values["BurnD"]
		poison_dmg = attack.poison_dmg*self.values["PsnD"]
		return [base_dmg, shock_dmg, burn_dmg, poison_dmg]