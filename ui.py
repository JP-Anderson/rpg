# basic ui option

class UI:
	
	def getUserDecision(self, message, optionStrings):
		lowestOption = 0
		highestOption = len(optionStrings)
		option = -1
		while option <= lowestOption or option > highestOption: 
			self.printOptions(optionStrings)
			option = int(input(message))
		print("0 " + optionStrings[0])
		print("1 " + optionStrings[1])
		print("2 " + optionStrings[2])
		print("Selected option: " + optionStrings[option-1])
	
	def printOptions(self, optionStrings):
		currentOptionNumber = 1
		for string in optionStrings:
			print(str(currentOptionNumber) + ". " + string)
			currentOptionNumber = currentOptionNumber + 1
	