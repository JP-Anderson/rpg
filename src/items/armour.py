# base armour class
from src.settings import *

class Armour:

	
	#lol
	def __init__(self, keyRow, valueRow):
		numberOfKeys = len(keyRow)
		self.values = {}
		#print (numberOfKeys)
		for i in range(0, numberOfKeys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i
		
		self.type = ObjectType.ARMOUR
		self.slot = ArmourSlot(int(self.values["Slot"]))

	def toString(self):
		print(self.values)
	
	def absorbDamage(self, attack):
		baseD = attack.baseD*self.values["PhysD"]
		shkD = attack.shkD*self.values["ShkD"]
		brnD = attack.brnD*self.values["BurnD"]
		psnD = attack.psnD*self.values["PsnD"]
		return [baseD, shkD, brnD, psnD]