# A spell with a single target
from src.utils.gooey import Gooey

class Target:
	
	def cast(self, target):
		raise NotImplementedError("Target object must implement method 'cast'")

class NoviceHeal(Target):
	def __init__(self):
		self.name = "Novice Heal"
		self.apCost = 5
	def cast(self, target):
		target.hp = target.hp+150
		if target.hp > target.maxHP:
			target.hp = target.maxHP
		Gooey.printLine(target.name + " was healed back to " + str(target.hp) + " health.")

class MasterHeal(Target):
	def __init__(self):
		self.name = "Master Heal"
		self.apCost = 5
	def cast(self, target):
		target.hp = target.hp+350
		if target.hp > target.maxHP:
			target.hp = target.maxHP
		Gooey.printLine(target.name + " was healed back to " + str(target.hp) + " health.")

class EMPBlast(Target):
	def __init__(self):
		self.name = "EMP Blast"
		self.apCost = 6
	def cast(self, target):
		baseDamage = 50
		techDamageMultiplier = 1.0-float(target.humanity)
		totalDamage = baseDamage + 300*techDamageMultiplier
		target.hp = target.hp-totalDamage
		if target.hp < 0:
			target.die()
		Gooey.printLine(target.name + " was hit with an EMP blast for " + str(totalDamage) + " damage!")
		if target.checkIfDead():
			Gooey.printLine(target.name + " has died.")
		else: Gooey.printLine(target.name + " has " + str(target.hp) + " health remaining...")