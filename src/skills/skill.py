# skill class
from settings import *

class Skill:

	
	#lol
	def __init__(self, name, description, skill_type):
		#print ("we are here")
		self.name = name
		self.description = description
		self.skill_type = skill_type
	
		
	def to_string(self):
		print(self.name)
		print("  " + self.description)