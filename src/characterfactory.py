# character creator
import time
import utils.state as State
from utils.gooey import Gooey
from character import Character

class CharacterFactory:
	
	def startBuilding():
		CharacterFactory.hey()
		name = Gooey.getUserInput("Enter character name: ")
		Gooey.printLine("You can select a class to read more information about"
		+ " the class, or you can create your own class.")
		time.sleep(2)
	
		prompt = "Select a class out of the following: "
		options = ["Human Weapons Expert",
			"Cyborg Ninja",
			"Black Hat",
			"White Hat",
			"Combat Android",
			"Dealer",
			"Make my own class"]
		
		Gooey.getUserInputWithList(prompt,options)
	
	def hey():
		print("hey")
