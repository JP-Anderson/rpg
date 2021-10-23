# A spell with a single target
from utils.gooey import Gooey

class Target:
	
	def cast(self, target):
		raise NotImplementedError("Target object must implement method 'cast'")

class NoviceHeal(Target):
	def __init__(self):
		self.name = "Novice Heal"
		self.ap_cost = 5
	def cast(self, target):
		Gooey.print_line(target.name + " was healed for " + str(150) + " health.")
		target.adjust_health(150)

class MasterHeal(Target):
	def __init__(self):
		self.name = "Master Heal"
		self.ap_cost = 5
	def cast(self, target):
		Gooey.print_line(target.name + " was healed for " + str(350) + " health.")
		target.adjust_health(350)


class EMPBlast(Target):
	def __init__(self):
		self.name = "EMP Blast"
		self.ap_cost = 6
	def cast(self, target):
		base_dmg = 50
		tech_damage_multiplier = 1.0-float(target.humanity)
		totalDamage = base_dmg + 300*tech_damage_multiplier
		Gooey.print_line(target.name + " was hit with an EMP blast for " + str(totalDamage) + " damage!")
		target.adjust_health(-totalDamage)
