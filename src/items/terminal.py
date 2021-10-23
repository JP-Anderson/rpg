# base weapon class
from settings import *
from skills.buff import Buff

class Terminal:

	
	#lol
	def __init__(self, keyRow, valueRow):
		#print ("we are here")
		self.type = ObjectType.TERMINAL
		number_of_keys = len(keyRow)
		self.values = {}
		#print (number_of_keys)
		for i in range(0, number_of_keys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i]])

	def to_string(self):
		print(self.values)
