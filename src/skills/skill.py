# skill class
from settings import *

class Skill:

	
	#lol
	def __init__(self, name, description, skillType):
		#print ("we are here")
		self.name = name
		self.description = description
		self.skillType = skillType
	
		
	def toString(self):
		print(self.name)
		print("  " + self.description)