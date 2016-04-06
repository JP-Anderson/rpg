# battle
from settings import *
from utils.gooey import Gooey
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
			print("---------------------- ----------------------- --------- WE'RE HERE --------- ---------------------------- ---------")
			gameIsRunning = self.checkBothTeamsAlive()
			if gameIsRunning:
				print()
				print()
				print("Next round")
				time.sleep(1)
				for fighter in self.fighters:
					print("We're here at the start of the fighter loop")
					if fighter.checkIfAlive():
						choice = 0
						while choice != 2:
							fightersToAttack = []
							if fighter.isPlayable:
								for potentialTarget in self.enemies:
									if potentialTarget.status != Status.DEAD: fightersToAttack.append(potentialTarget)
							else:
								for potentialTarget in self.friendlies:
									if potentialTarget.status != Status.DEAD: fightersToAttack.append(potentialTarget)
							print("while choice is not 2")
							fighterNames = []
							for fighter2 in fightersToAttack:
									fighterNames.append(fighter2.name)
							print("about to check if len fighters to attack is over 0")
							if len(fightersToAttack) > 0:
								print("len fightersToAttack is over 0")
								#Gooey.printTeamStats(self.friendlies, self.enemies)
								choices = ["Attack","Ability","End Turn","Check stats"]
								Gooey.printLine("It's " + fighter.name + "'s turn")
								choice = Gooey.getUserInputWithList(fighter.name + " has " + str(fighter.ap) + " AP remaining.", choices)
							
								if choice == 0: # ATTACK
									choice = Gooey.getUserInputWithList("Who do you want to attack, " + fighter.name + "?", fighterNames)
									if fighter.weapon == None:
										Gooey.printLine("No weapon equipped")										
									else:
										weaponAPCost = int(fighter.weapon.values["ShotAP"])
										if fighter.ap >= weaponAPCost:
											fighterToAttack = fightersToAttack[choice]
											fighterToAttack.defend(fighter.attack())
										else:
											Gooey.printLine("Not enough AP. " + fighter.weapon.values["Name"] + " requires " + str(weaponAPCost) + " AP to use.")
											time.sleep(1)
											Gooey.printLine("")
								elif choice == 1: # ABILITY
									abilityNames = fighter.abilityList.returnNameStrings()
									abilityCosts = fighter.abilityList.returnAbilityCosts()
									if len(abilityNames)>0:
										abilityChoice = Gooey.getUserInputWithList("What ability do you want to use?",abilityNames)
										abilityName = abilityNames[abilityChoice]
										abilityCost = abilityCosts[abilityChoice]
										
										if fighter.ap >= abilityCosts[abilityChoice]:
											fighterNames = []
											targetableFighters = []
											for abilityTarget in self.fighters:
												if abilityTarget.status != Status.DEAD: 
													fighterNames.append(abilityTarget.name)
													targetableFighters.append(abilityTarget)
											#print(targetableFighters)
											#print(self.fighters)
											targetChoice = Gooey.getUserInputWithList("Who would you like to target?", fighterNames)
											fighter.useAbility(abilityChoice, targetableFighters[targetChoice])
										else: 
											Gooey.printLine("Not enough AP. " + abilityName + " costs " + str(abilityCost) + " AP to use.") 
									else: Gooey.printLine("No abilities")
								elif choice == 2: # SKIP
									print("You have selected 2")
									pass
								elif choice == 3: 
									Gooey.printLine("Printing stats")
									Gooey.printTeamStats(self.friendlies, self.enemies)
									time.sleep(1)
									Gooey.printLine("")
							else:
								break
							print("We get here!")
							time.sleep(1)
						fighter.ap = fighter.ap+fighter.startAP
						if fighter.ap > fighter.maxAP: fighter.ap = fighter.maxAP
						print("End of our fighters loop.")
					else:
						pass
				else: print("...")
			else:
				print("Game over!")
				break
	
	def determineTurnOrder(self):
		charCount = len(self.fighters)
		if PRINT_DETAILED_STATS == True: print("Determining turn order ("+str(charCount)+" characters)")
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
			if friendly.checkIfAlive(): 
				areFriendliesAlive = True
		for enemy in self.enemies:
			if enemy.checkIfAlive():
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
