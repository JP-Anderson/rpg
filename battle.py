# battle
from settings import *

class Battle:
	
	def __init__(self, friendlyCharacters, enemyCharacters):
		self.friendlies = friendlyCharacters
		self.enemies = enemyCharacters
		self.fighters = friendlyCharacters + enemyCharacters
		self.determineTurnOrder()
		self.start()
	
	def start(self):
		print("Battle starting!")
		self.battleStatus = 0 #ACTIVE
		
	
	def determineTurnOrder(self):
		charCount = len(self.fighters)
		if PRINT_DETAILED_STATS == True : print("Determining turn order ("+str(charCount)+" characters)")
		characterSpeeds = []
		
		print("Presort:")
		self.printCharSpeeds()
		
		for char in self.fighters:
			charIndex = self.fighters.index(char)
			charSpeed = char.speed
			characterSpeeds.append([charSpeed, charIndex])
		
		sortedCharacterSpeeds = sorted(characterSpeeds, reverse=True)
		sortedCharacters = []
		
		for pair in sortedCharacterSpeeds:
			characterID = pair[1]
			sortedCharacters.append(self.fighters[characterID])
		
		self.fighters = sortedCharacters
		print("Post sort:")
		self.printCharSpeeds()
		
	def printCharSpeeds(self):
		for char in self.fighters:
			print(char.speed)
		
	
	
	# per char
	#	if char is alive
	#	         and char effects doesnt contain stunned
	#		
	#		if char ap is not 0 and turn not ended
	#		get char input
	#		if input = attack
	#			select enemy, attack
	#		if input = end
	#			end turn
	