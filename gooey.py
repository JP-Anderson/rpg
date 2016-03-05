# GUI class
from settings import *

class Gooey:

	def printLine(string):
		print(PROMPT + str(string))
	
	def printImportant(string):
		print((PROMPT + str(string)).upper())
	
	def getUserInput(prompt):
		print(PROMPT + str(prompt))
		return input()
	
	def getUserInputWithList(prompt, list):
		print(PROMPT + str(prompt))
		optionCount = 0
		for item in list:
			print(PROMPT + " ("+str(optionCount)+") " + item)
			optionCount=optionCount+1
		while(True):
			try:
				inputInt = int(input())
				if inputInt < optionCount and inputInt >= 0: return inputInt
			except:
				pass