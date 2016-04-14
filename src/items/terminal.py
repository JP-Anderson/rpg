# base weapon class
from settings import *
from skills.buff import Buff

class Terminal:

	
	#lol
	def __init__(self, keyRow, valueRow):
		#print ("we are here")
		self.type = ObjectType.TERMINAL
		numberOfKeys = len(keyRow)
		self.values = {}
		#print (numberOfKeys)
		for i in range(0, numberOfKeys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i]])

	def toString(self):
		print(self.values)
