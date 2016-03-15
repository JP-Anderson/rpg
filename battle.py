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
				time.sleep(1)
				for fighter in self.fighters:
					if fighter.status != Status.DEAD:
						fightersToAttack = []
						if fighter.isPlayable:
							for potentialTarget in self.enemies:
								if potentialTarget.status != Status.DEAD: fightersToAttack.append(potentialTarget)
						else:
							for potentialTarget in self.friendlies:
								if potentialTarget.status != Status.DEAD: fightersToAttack.append(potentialTarget)
						
						fighterNames = []
						for fighter2 in fightersToAttack:
								fighterNames.append(fighter2.name)
						if len(fightersToAttack) > 0:
							Gooey.printTeamStats(self.friendlies, self.enemies)
							choices = ["Attack","Ability","End Turn"]
							choice = Gooey.getUserInputWithList(fighter.name + " has " + str(fighter.ap) + "/" + str(fighter.maxAP) + " AP remaining.", choices)
							
							if choice == 0: # ATTACK
								choice = Gooey.getUserInputWithList("Who do you want to attack, " + fighter.name + "?", fighterNames)
								fighterToAttack = fightersToAttack[choice]
								fighterToAttack.defend(fighter.attack())
							elif choice == 1: # ABILITY
								abilityNames = fighter.abilityList.returnNameStrings()
								if len(abilityNames)>0:
									abilityChoice = Gooey.getUserInputWithList("What ability do you want to use?",abilityNames)
									fighterNames = []
									targetableFighters = []
									for abilityTarget in self.fighters:
										if abilityTarget.status != Status.DEAD: 
											fighterNames.append(abilityTarget.name)
											targetableFighters.append(abilityTarget)
									print(targetableFighters)
									print(self.fighters)
									targetChoice = Gooey.getUserInputWithList("Who would you like to target?", fighterNames)
									fighter.useAbility(abilityChoice, targetableFighters[targetChoice])
								else: print("No abilities")
							elif choice == 3: # SKIP
								pass
							
							fighter.ap = fighter.maxAP
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
			if friendly.status != Status.DEAD: 
				areFriendliesAlive = True
		for enemy in self.enemies:
			if enemy.status != Status.DEAD:
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