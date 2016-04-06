# GUI class
from settings import *

class Gooey:

	def printLine(string):
		print(PROMPT + str(string))
	
	def printImportant(string):
		print((PROMPT + str(string)).upper())
	
	def getUserInput(prompt):
		print(PROMPT + PROMPT + str(prompt))
		return input()
	
	def getUserInputWithList(prompt, list):
		print(PROMPT + str(prompt))
		optionCount = 0
		for item in list:
			print(PROMPT + "("+str(optionCount)+") " + item)
			optionCount=optionCount+1
		while(True):
			try:
				inputInt = int(input(PROMPT + PROMPT))
				if inputInt < optionCount and inputInt >= 0: return inputInt
			except:
				pass
	
	def printTeamStats(friendlies, enemies):
		print(PROMPT + "TEAM 1")
		for friendly in friendlies:
			if friendly.status != Status.DEAD: print(NESTEDPROMPT + friendly.name + " " + str(friendly.hp) + "/" + str(friendly.maxHP))
			else: print(friendly.name + " DEAD")
		print(PROMPT + "TEAM 2")
		for enemy in enemies:
			if enemy.status != Status.DEAD : print(NESTEDPROMPT + enemy.name + " " + str(enemy.hp) + "/" + str(enemy.maxHP))
			else: print (enemy.name + " DEAD")
