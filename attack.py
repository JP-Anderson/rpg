# attack
import random

from settings import *

class Attack:
	
	def __init__(self, baseD, shkD, brnD, psnD, dodge, baseCritC, critD, weapon):
		self.baseD = baseD
		self.shkD = shkD
		self.brnD = brnD
		self.psnD = psnD
		self.dodge = dodge
		self.baseCritC = baseCritC
		self.critD = critD
		self.weapon = weapon
		
		critRoll = random.random()
		#print("Rolled " + str(critRoll) + " for " + self.baseCritC + ".")
		if critRoll < float(self.baseCritC)*3:
			self.crit = 1 + float(self.critD)
			print("CRITICAL HIT ("+str(self.crit)+"x)")
		else: self.crit = 1.0
		
		print("!!!!!!!! Crit multiplier = " + str(self.crit) + " !!!!!!!!")
		
		self.baseD = float(self.baseD)*self.crit
		self.shkD = float(self.shkD)*self.crit
		self.brnD = float(self.brnD)*self.crit
		self.psnD = float(self.psnD)*self.crit
	
	def stats(self):
		
		
		
		if PRINT_DETAILED_STATS == True:
			self.printOutput("PHY",self.baseD)
			self.printOutput("SHK",self.shkD)
			self.printOutput("BRN",self.brnD)
			self.printOutput("PSN",self.psnD)
			print()
		self.printOutput("DAMAGE",self.baseD+
									self.shkD+
									self.brnD+
									self.psnD)
	
	def printOutput(self, text, value):
		value = str(value)
		fillerStarCount = 20-len(text)-len(value)
		print(text+" "+"*"*fillerStarCount+" "+value)