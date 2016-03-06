# battle
from settings import *
from gooey import Gooey
import time

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
		self.fighterCount = len(self.fighters)
		self.currentFighterCounter = 0
		self.currentFighter = self.fighters[self.currentFighterCounter]
		print("fighter count " + str(self.fighterCount))
		self.turnCount = 1
		self.battleLoop()
	
	def battleLoop(self):
		while(True):
			gameIsRunning = self.checkBothTeamsAlive()
			if gameIsRunning:
				print()
				print()
				print("We're starting another round")
				time.sleep(2)
				for fighter in self.fighters:
					if fighter.status>0:
						fightersToAttack = []
						if fighter.isPlayable:
							for fighter2 in self.enemies:
								if fighter2.status > 0: fightersToAttack.append(fighter2)
						else:
							for fighter2 in self.friendlies:
								if fighter2.status > 0: fightersToAttack.append(fighter2)
						
						fighterNames = []
						for fighter2 in fightersToAttack:
								fighterNames.append(fighter2.name)
						if len(fightersToAttack) > 0:
							choice = Gooey.getUserInputWithList("Who do you want to attack, " + fighter.name + "?", fighterNames)
							fighterToAttack = fightersToAttack[choice]
							fighterToAttack.defend(fighter.attack())
						else:
							pass
					else: print("...")
			else:
				print("Game over!")
				break
	
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
		
	def checkBothTeamsAlive(self):
		print("We're here.")
		areFriendliesAlive = False
		areEnemiesAlive = False
		for friendly in self.friendlies:
			if friendly.status == 1: 
				areFriendliesAlive = True
		for enemy in self.enemies:
			if enemy.status == 1:
				areEnemiesAlive = True
		b = areFriendliesAlive and areEnemiesAlive
		if b:
			print("Returning true")
		else:
			print("Returning false")
		return b
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