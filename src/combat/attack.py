# attack
import random

from settings import *

class Attack:
	
	def __init__(self, base_dmg, shock_dmg, burn_dmg, poison_dmg, dodge, base_critical_chance, critical_dmg, weapon):
		self.base_dmg = base_dmg
		self.shock_dmg = shock_dmg
		self.burn_dmg = burn_dmg
		self.poison_dmg = poison_dmg
		self.dodge = dodge
		self.base_critical_chance = base_critical_chance
		self.critical_dmg = critical_dmg
		self.weapon = weapon
		
		critical_roll = random.random()
		#print("Rolled " + str(critical_roll) + " for " + self.base_critical_chance + ".")
		if critical_roll < float(self.base_critical_chance)*3:
			self.critical_chance = 1 + float(self.critical_dmg)
			print("CRITICAL HIT ("+str(self.critical_chance)+"x)")
		else: self.critical_chance = 1.0
		
		print("!!!!!!!! Crit multiplier = " + str(self.critical_chance) + " !!!!!!!!")
		
		self.base_dmg = float(self.base_dmg)*self.critical_chance
		self.shock_dmg = float(self.shock_dmg)*self.critical_chance
		self.burn_dmg = float(self.burn_dmg)*self.critical_chance
		self.poison_dmg = float(self.poison_dmg)*self.critical_chance
	
	def stats(self):
		
		
		
		if PRINT_DETAILED_STATS == True:
			self.print_output("PHY",self.base_dmg)
			self.print_output("SHK",self.shock_dmg)
			self.print_output("BRN",self.burn_dmg)
			self.print_output("PSN",self.poison_dmg)
			print()
		self.print_output("DAMAGE",self.base_dmg+
									self.shock_dmg+
									self.burn_dmg+
									self.poison_dmg)
	
	def print_output(self, text, value):
		value = str(value)
		filler_star_count = 20-len(text)-len(value)
		print(text+" "+"*"*filler_star_count+" "+value)