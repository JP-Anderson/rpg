from settings import *
from skills.skill import Skill

class SkillTree:

	
	#lol
	def __init__(self, name, description, levelCount, arrayOfChoices, gui):
		#print ("we are here")
		self.name = name
		self.level = 0
		self.description = description
		self.levelCount = levelCount
		self.skillList = arrayOfChoices
		self.selectedSkills = []
		self.gui = gui
		
	
	def levelUp(self):
		if self.is_max_level():
			print("This skill has been maxed out!")
			return
		selection = self.gui.getUserInputWithList("Choose the skill for this level",self.getOptionStrings())
		self.selectedSkills.append(self.skillList[self.level][selection])
		self.level = self.level+1
		self.gui.printLine("Level " + str(self.level) + " " + self.name + " " + " reached")
	
	def is_max_level(self):
		return self.level >= self.levelCount
	
	def getOptionStrings(self):
		if self.is_max_level():
			return []
		optionStrings = []
		availableSkillsAtThisLevel = self.skillList[self.level]
		optionStrings.append(availableSkillsAtThisLevel[0].name)
		optionStrings.append(availableSkillsAtThisLevel[1].name)
		return optionStrings
		
	
	def toString(self):
		print(self.name + " Skill Tree")
		print("  " + self.description)
		for skill in self.selectedSkills:
			print()
			skill.toString()