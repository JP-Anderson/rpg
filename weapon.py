# base weapon class
from settings import *
from attack import Attack

class Weapon:

	
	#lol
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
	
	def attack(self):
		attack = Attack(self.values["BaseD"],
						self.values["ShkD"],
						self.values["BrnD"],
						self.values["PsnD"],
						self.values["Dodgeability"],
						self.values["BaseCritC"],
						self.values["CritD"],
						self.values["Name"])
		return attack