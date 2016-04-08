# character creator
import time
from settings import *
import utils.state as State
from utils.gooey import Gooey
from character import Character

classDescriptions = ["The Fighter is skilled with all types of weapons, but you can choose which types of weapons to specialise in.\n The Fighter can be android or human.",
						"The Dealer is trained in the production and application of cutting edge battle stimulants and healing medications.\n The Dealer can be android or human.",
						"The Hacker utilises jamming and electromagnetic devices to deal tech damage and cast powerful buffs/debuffs on androids .\n The Hacker must be at least partially android."]
STAT_DESCRIPTIONS = ["Strength is required to wield larger weapons, and gives damage bonuses for strength based weapons.\n",
					"Dexterity gives damage bonuses and/or is required for certain finesse based weapons.\n",
					"Endurance determines a fighters equipment load, and max health.\n",
					"Intelligence is required for hackers to execute certain abilities and operate terminals.\n",
					"Agility determines a fighters ability to effectively dodge incoming attacks.\n",
					"Speed determines the order in which fighters take their turn, and slightly affects dodge chance.\n",
					"Humanity represents the amount of cybernetic/biological enhancements a fighter bears.",
					"Unlike the other stats, Humanity cannot be changed after being set. The lower a fighters", 
					"humanity, the more susceptible they are to tech based weapons/abilities. Fighters with",
					"a higher humanity also gain more benefits from stims and chems.",
					"Humanity isn't represented by integers like the other skills, but a 0 to 1 decimal scale:",
					"1.0          0.5          0.0",
					"|-------------|-------------|",
					"Pure human    Cyborg       Android"]
						
class CharacterFactory:
	
	
	
	def startBuilding():
		CharacterFactory.hey()
		
		classChosen = False
		while classChosen == False:
			name = Gooey.getUserInput("Enter character name: ")
			Gooey.printLine("You can select a class to read more information about"
			+ " the class, or you can create your own class.")
			time.sleep(2)
			prompt = "Select a class out of the following: "
			options = ["Fighter",
						"Dealer",
						"Hacker"]
			
			classChoice = Gooey.getUserInputWithList(prompt,options)
			description = classDescriptions[classChoice]
			Gooey.printLine(description)
			finalPrompt = "Are you sure you want to be " + name + " the " + options[classChoice]
			finalOptions = ["No","Yes"]
			finalChoice = Gooey.getUserInputWithList(finalPrompt,finalOptions)
			if finalChoice == 1:
				classChosen = True
		
		Gooey.printMultiLine(STAT_DESCRIPTIONS)
		time.sleep(32)		
			
	def hey():
		print("hey")
