# character creator
import time
from settings import *
import utils.state as State
from utils.gooey import Gooey
from character import Character
			
class CharacterFactory:

	def __init__(self):
		self.fighterStats = []
		self.maxAvailableStatPoints = STARTING_STAT_POINTS
		self.unusedStatPoints = 0
		self.buildCharacter()
		
	
	def buildCharacter(self):
		fighterClass = self.setCharacterNameAndClass()
		self.setCharacterStats(fighterClass)		
		
		time.sleep(5)
		Gooey.printMultiLine(STAT_DESCRIPTIONS)
		time.sleep(32)	
		
	def setCharacterNameAndClass(self):
		classChosen = False
		while classChosen == False:
			name = self.setCharacterName()
			classChoice = self.setCharacterClass()			
			finalPrompt = "Are you sure you want to be " + name + " the " + CLASS_NAMES[classChoice]
			finalOptions = ["No","Yes"]
			finalChoice = Gooey.getUserInputWithList(finalPrompt,finalOptions)
			if finalChoice == 1:
				classChosen = True
		return classChoice
	
	def setCharacterName(self):
		name = Gooey.getUserInput("Enter character name: ")
		return name
	
	def setCharacterClass(self):
		Gooey.printLine("Choose your class. You can select a class to read more information about"
			+ " the class.")
		time.sleep(2)
		prompt = "Select a class out of the following: "
		options = ["Fighter","Dealer","Hacker"]			
		classChoice = Gooey.getUserInputWithList(prompt,options)
		Gooey.printLine(CLASS_DESCRIPTIONS[classChoice])
		return classChoice
	
	def setCharacterStats(self, fighterClassID):
		Gooey.printMultiLine(["Stats represent the various characteristics of your fighter and determine your characters strengths and weaknesses.",
			"You can now adjust your starting stats."])
		
		self.fighterStats = BASE_STATS[fighterClassID]
		statsChosen = False
		while statsChosen == False:
			self.printAssignableStatPoints()
			prompt = "Enter the stat for more information or to change the stat:"
			options = ["Strength: " + str(self.fighterStats[0]),"Dexterity: " + str(self.fighterStats[1]),
			"Endurance: " + str(self.fighterStats[2]),"Intelligence: " + str(self.fighterStats[3]),
			"Agility: " + str(self.fighterStats[4]),"Speed: " + str(self.fighterStats[5]),"Humanity: " + str(self.fighterStats[6])]
			statChoice = Gooey.getUserInputWithList(prompt, options)
			self.printNormalStatDetail(statChoice)
	
	def printAssignableStatPoints(self):
		Gooey.printLine("You have " + str(self.unusedStatPoints) + " points to assign.")
		if self.unusedStatPoints == 0:
			Gooey.printLine("You can lower any stat to redistribute the points to another stat.")
	
	def printNormalStatDetail(self, statID):
		statValue = self.fighterStats[statID]
		Gooey.printMultiLine([STAT_DESCRIPTIONS[statID],
			"You have " + str(statValue) + " " + BASE_STAT_NAMES[statID]])
		
		prompt = "Enter a new value for this stat, or a non-number to return to the stat list."
		userInput = Gooey.getUserInput(prompt)
		if self.isInteger(userInput):
			userInput = int(userInput)
			if self.isStatChangeValid(statValue, userInput):
				self.fighterStats[statID] = int(userInput)
			else:
				x = None	
	
	def isInteger(self, userInput):
		try:
			int(userInput)
			return True
		except:
			return False
	
	def isStatChangeValid(self, oldValue, newValue):
		if not self.newStatIsValidNumber(newValue): return False
		statChange = newValue-oldValue
		if statChange > 0:
			if statChange <= self.unusedStatPoints:
				self.unusedStatPoints = self.unusedStatPoints - statChange
				return True
			else:
				Gooey.printLine("Not enough points, please reduce another stat first.") 
				return False
		else:
			self.unusedStatPoints = self.unusedStatPoints + statChange
			return True
			
	def newStatIsValidNumber(self, newValue):
		if newValue <= STAT_LIMIT and newValue >= 1: return True
		Gooey.printLine("A stat must lie in range 1 to " + str(STAT_LIMIT)) 
		return False
		
		
	
			
