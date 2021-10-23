# A spell with a single target
from utils.gooey import Gooey

class Target:
	
	def cast(self, target):
		raise NotImplementedError("Target object must implement method 'cast'")

class NoviceHeal(Target):
	def __init__(self):
		self.name = "Novice Heal"
		self.apCost = 5
	def cast(self, target):
		Gooey.printLine(target.name + " was healed for " + str(150) + " health.")
		target.adjust_health(150)

class MasterHeal(Target):
	def __init__(self):
		self.name = "Master Heal"
		self.apCost = 5
	def cast(self, target):
		Gooey.printLine(target.name + " was healed for " + str(350) + " health.")
		target.adjust_health(350)


class EMPBlast(Target):
	def __init__(self):
		self.name = "EMP Blast"
		self.apCost = 6
	def cast(self, target):
		baseDamage = 50
		techDamageMultiplier = 1.0-float(target.humanity)
		totalDamage = baseDamage + 300*techDamageMultiplier
		Gooey.printLine(target.name + " was hit with an EMP blast for " + str(totalDamage) + " damage!")
		target.adjust_health(-totalDamage)
