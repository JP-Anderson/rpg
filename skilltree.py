# skill class
from settings import *
from gooey import Gooey
from skill import Skill

class SkillTree:

	
	#lol
	def __init__(self, name, description, levelCount, arrayOfChoices):
		#print ("we are here")
		self.name = name
		self.level = 0
		self.description = description
		self.levelCount = levelCount
		self.skillList = arrayOfChoices
		self.selectedSkills = []
	
	def levelUp(self):
		if (self.level < self.levelCount):
			self.level = self.level+1
			Gooey.printLine("Level " + str(self.level) + " " + self.name + " " + " reached")
			selection = Gooey.getUserInputWithList("Choose the skill for this level",self.getOptionStrings(self.level))
			self.selectedSkills.append(self.skillList[self.level-1][selection])
		else: print("This skill has been maxed out!")
	
	
	def getOptionStrings(self, level):
		optionStrings = []
		availableSkillsAtThisLevel = self.skillList[self.level-1]
		optionStrings.append(availableSkillsAtThisLevel[0].name)
		optionStrings.append(availableSkillsAtThisLevel[1].name)
		return optionStrings
		
	
	def toString(self):
		print(self.name + " Skill Tree")
		print("  " + self.description)
		for skill in self.selectedSkills:
			print()
			skill.toString()