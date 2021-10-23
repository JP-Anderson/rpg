# character creator
import time
from settings import *
import utils.state as State
from utils.gooey import Gooey
from character import Character
			
class CharacterFactory:

	def __init__(self, free_stat_points=10):
		self.fighter_stats = []
		self.max_available_stat_points = free_stat_points
		self.unused_stat_points = self.max_available_stat_points
		
		self.name = ""
		self.char_class = 0
	
	def build(self):
		self.unused_stat_points = self.max_available_stat_points
		fighter_class = self.set_character_name_and_class()
		self.set_character_stats(fighter_class)
		self.set_character_humanity()
		return self.build_character()
		
	def set_character_name_and_class(self):
		class_chosen = False
		while class_chosen == False:
			self.name = self.set_character_name()
			class_choice = self.set_character_class()
			self.set_character_class_enum(class_choice)
			final_prompt = "Are you sure you want to be " + self.name + " the " + CLASS_NAMES[class_choice]
			final_options = ["No","Yes"]
			final_choice = Gooey.get_user_input_with_list(final_prompt, final_options)
			if final_choice == 1:
				class_chosen = True
		return class_choice
	
	def set_character_name(self):
		name = Gooey.get_user_input("Enter character name: ")
		return name
	
	def set_character_class(self):
		Gooey.print_empty(1)
		Gooey.print_line("Choose your class. You can select a class to read more information about"
			+ " the class.")
		prompt = "Select a class out of the following: "
		options = ["Fighter","Dealer","Hacker"]			
		class_choice = Gooey.get_user_input_with_list(prompt,options)
		Gooey.print_line(CLASS_DESCRIPTIONS[class_choice])
		return class_choice
	
	def set_character_class_enum(self, classInt):
		print("WERE SETTING CLASS TO:")
		print(str(Class(int(classInt))))
		self.char_class = Class(int(classInt))
	
	def set_character_stats(self, fighterClassID):
		Gooey.print_empty(1)
		Gooey.print_multi_line(["Stats represent the various characteristics of your fighter and determine your characters strengths and weaknesses.",
			"You can now adjust your starting stats."])
		
		self.fighter_stats = BASE_STATS[fighterClassID]
		stats_chosen = False
		while stats_chosen == False:
			self.print_assignable_stat_points()
			prompt = "Enter the stat ID for more information or to change the stat:"
			options = ["Strength: " + str(self.fighter_stats[0]),"Dexterity: " + str(self.fighter_stats[1]),
			"Endurance: " + str(self.fighter_stats[2]),"Intelligence: " + str(self.fighter_stats[3]),
			"Agility: " + str(self.fighter_stats[4]),"Speed: " + str(self.fighter_stats[5]),"CONTINUE"]
			stat_choice = Gooey.get_user_input_with_list(prompt, options)
			if self.is_integer(stat_choice) and stat_choice < 6:
				time.sleep(1)
				Gooey.print_line("")
				self.print_normal_stat_detail(stat_choice)
			elif stat_choice == 6:
				if self.unused_stat_points:
					Gooey.print_line("You still have unused stat points to assign!")
					time.sleep(4)
				else: stats_chosen = True
			
			Gooey.print_line("")
	
	def print_assignable_stat_points(self):
		Gooey.print_line("You have " + str(self.unused_stat_points) + " points to assign.")
		if self.unused_stat_points == 0:
			Gooey.print_line("You can lower any stat to redistribute the points to another stat.")
	
	def print_normal_stat_detail(self, statID):
		statValue = self.fighter_stats[statID]
		Gooey.print_multi_line([STAT_DESCRIPTIONS[statID],
			"You have " + str(statValue) + " " + BASE_STAT_NAMES[statID]])
		
		prompt = "Enter a new value for this stat, or a non-number to return to the stat list."
		userInput = Gooey.get_user_input(prompt)
		if self.is_integer(userInput):
			userInput = int(userInput)
			if self.is_stat_change_valid(statValue, userInput):
				self.fighter_stats[statID] = int(userInput)
			else:
				x = None	
	
	def is_integer(self, userInput):
		try:
			int(userInput)
			return True
		except:
			return False
	
	def is_stat_change_valid(self, old_value, new_value):
		if not self.new_stat_is_valid_number(new_value): return False
		stat_change = new_value-old_value
		if stat_change > 0:
			if stat_change <= self.unused_stat_points:
				self.unused_stat_points = self.unused_stat_points - stat_change
				return True
			else:
				Gooey.print_line("Not enough points, please reduce another stat first.") 
				return False
		else:
			self.unused_stat_points = self.unused_stat_points + -stat_change
			return True
			
	def new_stat_is_valid_number(self, new_value):
		if new_value <= STAT_LIMIT and new_value >= 1: return True
		Gooey.print_line("A stat must lie in range 1 to " + str(STAT_LIMIT)) 
		return False
	
	def set_character_humanity(self):
		Gooey.print_line("The last stat to choose is Humanity.")
		Gooey.print_line(STAT_DESCRIPTIONS[6])
		#time.sleep(10)
		humanity_chosen = False
		while humanity_chosen == False:
			Gooey.print_line("You have " + str(self.fighter_stats[6]) + " Humanity.")
			self.print_humanity_information(self.fighter_stats[6])
			prompt = "Change or confirm your Humanity"
			options = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,"CONTINUE"]			
			humanityChoice = Gooey.get_user_input_with_list(prompt,options)
			if 0 <= humanityChoice and humanityChoice <= 10:
				self.fighter_stats[6] = options[humanityChoice]
				pass
			elif humanityChoice == 11:
				print("We're here.")
				humanity_chosen = True
	
	def print_humanity_information(self, humanity):
		if humanity < 0.4:
			Gooey.print_multi_line(["Tech damage, buffs and abilities are very effective on you.",
			"Drugs (healing, damage/resistance/stat buffs) have little to no effect on you."])
		elif humanity < 0.7:
			Gooey.print_multi_line([
				"Tech damage, buffs and abilities will have a moderate effect on you.",
				"Drugs (healing, damage/resistance/stat buffs) will have a moderate effect on you."])
		elif humanity >= 0.7:
			Gooey.print_multi_line([
				"Tech damage, buffs and abilities will have little to no effect on you.",
				"Drugs (healing, damage/resistance/stat buffs) are very effective on you."])
	
	def build_character(self):
		return Character(name = self.name,
			char_class = self.char_class,
			strength = self.fighter_stats[0],
			dexterity = self.fighter_stats[1],
			endurance = self.fighter_stats[2],
			intelligence = self.fighter_stats[3],
			agility = self.fighter_stats[4],
			speed = self.fighter_stats[5],
			humanity = self.fighter_stats[6],
			is_playable = True)
		
