# buff class
from settings import *

class Buff:

	def __init__(self, keyRow, valueRow):
		number_of_keys = len(keyRow)
		self.values = {}
		#print (number_of_keys)
		#print(keyRow)
		#print("VALUE ROW size: " + str(len(valueRow)))
		#print(valueRow)
		for i in range(0, number_of_keys):
			self.values[keyRow[i]] = valueRow[i]
			#print (keyRow[i]+" : "+self.values[keyRow[i

	def to_string(self):
		print(self.values)
	
	def apply_buff(self):
		print("Applying buff")
