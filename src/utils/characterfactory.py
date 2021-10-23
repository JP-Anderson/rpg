# character creator
import time
from settings import *
import utils.state as State
from utils.gooey import Gooey
from character import Character
			
class CharacterFactory:

	def __init__(self, free_stat_points=10):
		self.fighterStats = []
		self.maxAvailableStatPoints = free_stat_points
		self.unusedStatPoints = self.maxAvailableStatPoints
		
		self.name = ""
		self.charClass = 0
	
	def build(self):
		self.unusedStatPoints = self.maxAvailableStatPoints
		fighterClass = self.setCharacterNameAndClass()
		self.setCharacterStats(fighterClass)
		self.setCharacterHumanity()
		return self.buildCharacter()
		
	def setCharacterNameAndClass(self):
		classChosen = False
		while classChosen == False:
			self.name = self.setCharacterName()
			classChoice = self.setCharacterClass()
			self.setCharacterClassEnum(classChoice)
			finalPrompt = "Are you sure you want to be " + self.name + " the " + CLASS_NAMES[classChoice]
			finalOptions = ["No","Yes"]
			finalChoice = Gooey.getUserInputWithList(finalPrompt,finalOptions)
			if finalChoice == 1:
				classChosen = True
		return classChoice
	
	def setCharacterName(self):
		name = Gooey.getUserInput("Enter character name: ")
		return name
	
	def setCharacterClass(self):
		Gooey.printEmpty(1)
		Gooey.printLine("Choose your class. You can select a class to read more information about"
			+ " the class.")
		prompt = "Select a class out of the following: "
		options = ["Fighter","Dealer","Hacker"]			
		classChoice = Gooey.getUserInputWithList(prompt,options)
		Gooey.printLine(CLASS_DESCRIPTIONS[classChoice])
		return classChoice
	
	def setCharacterClassEnum(self, classInt):
		print("WERE SETTING CLASS TO:")
		print(str(Class(int(classInt))))
		self.charClass = Class(int(classInt))
	
	def setCharacterStats(self, fighterClassID):
		Gooey.printEmpty(1)
		Gooey.printMultiLine(["Stats represent the various characteristics of your fighter and determine your characters strengths and weaknesses.",
			"You can now adjust your starting stats."])
		
		self.fighterStats = BASE_STATS[fighterClassID]
		statsChosen = False
		while statsChosen == False:
			self.printAssignableStatPoints()
			prompt = "Enter the stat ID for more information or to change the stat:"
			options = ["Strength: " + str(self.fighterStats[0]),"Dexterity: " + str(self.fighterStats[1]),
			"Endurance: " + str(self.fighterStats[2]),"Intelligence: " + str(self.fighterStats[3]),
			"Agility: " + str(self.fighterStats[4]),"Speed: " + str(self.fighterStats[5]),"CONTINUE"]
			statChoice = Gooey.getUserInputWithList(prompt, options)
			if self.isInteger(statChoice) and statChoice < 6:
				time.sleep(1)
				Gooey.printLine("")
				self.printNormalStatDetail(statChoice)
			elif statChoice == 6:
				if self.unusedStatPoints:
					Gooey.printLine("You still have unused stat points to assign!")
					time.sleep(4)
				else: statsChosen = True
			
			Gooey.printLine("")
	
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
			self.unusedStatPoints = self.unusedStatPoints + -statChange
			return True
			
	def newStatIsValidNumber(self, newValue):
		if newValue <= STAT_LIMIT and newValue >= 1: return True
		Gooey.printLine("A stat must lie in range 1 to " + str(STAT_LIMIT)) 
		return False
	
	def setCharacterHumanity(self):
		Gooey.printLine("The last stat to choose is Humanity.")
		Gooey.printLine(STAT_DESCRIPTIONS[6])
		#time.sleep(10)
		humanityChosen = False
		while humanityChosen == False:
			Gooey.printLine("You have " + str(self.fighterStats[6]) + " Humanity.")
			self.printHumanityInformation(self.fighterStats[6])
			prompt = "Change or confirm your Humanity"
			options = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,"CONTINUE"]			
			humanityChoice = Gooey.getUserInputWithList(prompt,options)
			if 0 <= humanityChoice and humanityChoice <= 10:
				self.fighterStats[6] = options[humanityChoice]
				pass
			elif humanityChoice == 11:
				print("We're here.")
				humanityChosen = True
	
	def printHumanityInformation(self, humanity):
		if humanity < 0.4:
			Gooey.printMultiLine(["Tech damage, buffs and abilities are very effective on you.",
			"Drugs (healing, damage/resistance/stat buffs) have little to no effect on you."])
		elif humanity < 0.7:
			Gooey.printMultiLine([
				"Tech damage, buffs and abilities will have a moderate effect on you.",
				"Drugs (healing, damage/resistance/stat buffs) will have a moderate effect on you."])
		elif humanity >= 0.7:
			Gooey.printMultiLine([
				"Tech damage, buffs and abilities will have little to no effect on you.",
				"Drugs (healing, damage/resistance/stat buffs) are very effective on you."])
	
	def buildCharacter(self):
		return Character(name = self.name,
			charClass = self.charClass,
			strength = self.fighterStats[0],
			dexterity = self.fighterStats[1],
			endurance = self.fighterStats[2],
			intelligence = self.fighterStats[3],
			agility = self.fighterStats[4],
			speed = self.fighterStats[5],
			humanity = self.fighterStats[6],
			isPlayable = True)
		
