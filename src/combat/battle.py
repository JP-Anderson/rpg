# battle
from settings import *
from utils.gooey import Gooey
import time

class Battle:
	
	def __init__(self, friendly_characters, enemy_characters):
		self.friendlies = friendly_characters
		self.enemies = enemy_characters
		self.fighters = friendly_characters + enemy_characters
		self.determine_turn_order()
		self.start()
	
	def start(self):
		print("Battle starting!")
		self.battleStatus = 0 #ACTIVE
		self.fighterCount = len(self.fighters)
		self.currentFighterCounter = 0
		self.currentFighter = self.fighters[self.currentFighterCounter]
		print("fighter count " + str(self.fighterCount))
		self.turnCount = 1
		self.start_loop()
		if self.friendlies_alive():
			print("You win!")
	
	def start_loop(self):
		round_count = 0
		battle_is_ongoing = self.check_both_teams_alive()
		while(battle_is_ongoing):
			print()
			print()
			round_count = round_count + 1
			print("Round " + str(round_count))
			time.sleep(1)
			for fighter in self.fighters:
				if not fighter.is_dead():
					choice = 0
					while choice != 2:
						fighters_to_attack = []
						if fighter.is_playable:
							for potential_target in self.enemies:
								if potential_target.status != Status.DEAD: fighters_to_attack.append(potential_target)
						else:
							for potential_target in self.friendlies:
								if potential_target.status != Status.DEAD: fighters_to_attack.append(potential_target)
						fighter_names = []
						for f in fighters_to_attack:
								fighter_names.append(f.name)
						if len(fighters_to_attack) > 0:
							#Gooey.printTeamStats(self.friendlies, self.enemies)
							choices = ["Attack","Ability","End Turn","Check stats"]
							Gooey.printLine("It's " + fighter.name + "'s turn")
							choice = Gooey.getUserInputWithList(fighter.name + " has " + str(fighter.ap) + " AP remaining.", choices)
						
							if choice == 0: # ATTACK
								choice = Gooey.getUserInputWithList("Who do you want to attack, " + fighter.name + "?", fighter_names)
								if fighter.weapon == None:
									Gooey.printLine("No weapon equipped")										
								else:
									weapon_ap_cost = int(fighter.weapon.values["ShotAP"])
									if fighter.ap >= weapon_ap_cost:
										fighter_to_attack = fighters_to_attack[choice]
										fighter_to_attack.defend(fighter.attack())
									else:
										Gooey.printLine("Not enough AP. " + fighter.weapon.values["Name"] + " requires " + str(weapon_ap_cost) + " AP to use.")
										time.sleep(1)
										Gooey.printLine("")
							elif choice == 1: # ABILITY
								ability_names = fighter.ability_list.return_name_strings()
								ability_costs = fighter.ability_list.return_ability_costs()
								if len(ability_names)>0:
									ability_choice = Gooey.getUserInputWithList("What ability do you want to use?",ability_names)
									ability_name = ability_names[ability_choice]
									ability_cost = ability_costs[ability_choice]
									
									if fighter.ap >= ability_costs[ability_choice]:
										fighter_names = []
										targetableFighters = []
										for abilityTarget in self.fighters:
											if abilityTarget.status != Status.DEAD: 
												fighter_names.append(abilityTarget.name)
												targetableFighters.append(abilityTarget)
										#print(targetableFighters)
										#print(self.fighters)
										targetChoice = Gooey.getUserInputWithList("Who would you like to target?", fighter_names)
										fighter.use_ability(ability_choice, targetableFighters[targetChoice])
									else: 
										Gooey.printLine("Not enough AP. " + ability_name + " costs " + str(ability_cost) + " AP to use.") 
								else: Gooey.printLine("No abilities")
							elif choice == 2: # SKIP
								pass
							elif choice == 3: 
								Gooey.printLine("")
								Gooey.printLine("Printing stats")
								Gooey.printTeamStats(self.friendlies, self.enemies)
								time.sleep(1)
								Gooey.printLine("")
						else:
							break
						time.sleep(1)
					fighter.ap = fighter.ap+fighter.startAP
					if fighter.ap > fighter.maxAP: fighter.ap = fighter.maxAP
				else:
					pass
			else: print("...")
			
			battle_is_ongoing = self.check_both_teams_alive()	 
	
	def determine_turn_order(self):
		charCount = len(self.fighters)
		if PRINT_DETAILED_STATS == True: print("Determining turn order ("+str(charCount)+" characters)")
		characterSpeeds = []
		
		#print("Presort:")
		#self.print_speeds()
		
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
		#print("Post sort:")
		#self.print_speeds()
		
	def print_speeds(self):
		for char in self.fighters:
			print(char.speed)
		
	def check_both_teams_alive(self):
		return self.friendlies_alive() and self.enemies_alive()
	
	def friendlies_alive(self):
		for f in self.friendlies:
			if not f.is_dead():
				return True
	
	def enemies_alive(self):
		for e in self.enemies:
			if not e.is_dead():
				return True
	
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
