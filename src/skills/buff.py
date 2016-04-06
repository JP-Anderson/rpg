# buff class
from settings import *

class Buff:

	def __init__(self, keyRow, valueRow):
		numberOfKeys = len(keyRow)
		self.values = {}
		#print (numberOfKeys)
		#print(keyRow)
		#print("VALUE ROW size: " + str(len(valueRow)))
		#print(valueRow)
		for i in range(0, numberOfKeys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i

	def toString(self):
		print(self.values)
	
	def applyBuff(self):
		print("Applying buff")
