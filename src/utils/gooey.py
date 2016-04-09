# GUI class
from settings import *

class Gooey:

	def printLine(string):
		print(str(string))
		
	def printEmpty(emptyLines):
		for i in range(0,emptyLines): print("")
	
	def printMultiLine(lines):
		for line in lines:
			print(str(line))
	
	def printImportant(string):
		print((+ str(string)).upper())
	
	def getUserInput(prompt):
		print(str(prompt))
		return input(PROMPT)
	
	def getUserInputWithList(prompt, list):
		print(str(prompt))
		optionCount = 0
		for item in list:
			print("("+str(optionCount)+") " + str(item))
			optionCount=optionCount+1
		while(True):
			try:
				inputInt = int(input(PROMPT))
				if inputInt < optionCount and inputInt >= 0: return inputInt
			except:
				pass
	
	def printTeamStats(friendlies, enemies):
		print(PROMPT + "TEAM 1")
		for friendly in friendlies:
			if friendly.status != Status.DEAD: print(NESTEDPROMPT + friendly.name + " " + str(friendly.hp) + "/" + str(friendly.maxHP))
			else: print(NESTEDPROMPT + friendly.name + " DEAD")
		print(PROMPT + "TEAM 2")
		for enemy in enemies:
			if enemy.status != Status.DEAD : print(NESTEDPROMPT + enemy.name + " " + str(enemy.hp) + "/" + str(enemy.maxHP))
			else: print (NESTEDPROMPT + enemy.name + " DEAD")
