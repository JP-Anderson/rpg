# GUI class
from settings import *

class Gooey:

	def print_line(string):
		print(str(string))
		
	def print_empty(emptyLines):
		for i in range(0,emptyLines): print("")
	
	def print_multi_line(lines):
		for line in lines:
			print(str(line))
	
	def print_important(string):
		print((+ str(string)).upper())
	
	def get_user_input(prompt):
		print(str(prompt))
		return input(PROMPT)
	
	def get_user_input_with_list(prompt, list):
		print(str(prompt))
		option_count = 0
		for item in list:
			print("("+str(option_count)+") " + str(item))
			option_count=option_count+1
		while(True):
			try:
				input_int = int(input(PROMPT))
				if option_count > input_int >= 0: return input_int
			except:
				pass
	
	def print_team_stats(friendlies, enemies):
		print(PROMPT + "TEAM 1")
		for friendly in friendlies:
			if friendly.status != Status.DEAD: print(NESTED_PROMPT + friendly.name + " " + str(friendly.hp) + "/" + str(friendly.max_hp))
			else: print(NESTED_PROMPT + friendly.name + " DEAD")
		print(PROMPT + "TEAM 2")
		for enemy in enemies:
			if enemy.status != Status.DEAD : print(NESTED_PROMPT + enemy.name + " " + str(enemy.hp) + "/" + str(enemy.max_hp))
			else: print (NESTED_PROMPT + enemy.name + " DEAD")

class MockGooey:
	
	def print_line(self, string):
		print(str(string))
		
	def print_empty(emptyLines):
		for i in range(0,emptyLines): print("")
	
	def print_multi_line(lines):
		for line in lines:
			print(str(line))
	
	def print_important(string):
		print((+ str(string)).upper())
	
	def get_user_input(prompt):
		print(str(prompt))
		return input(PROMPT)
	
	def set_get_user_input_with_list_response(self, i):
		self.get_user_input_with_list_response = i
	
	def get_user_input_with_list(self, prompt, list):
		return self.get_user_input_with_list_response