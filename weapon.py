# base weapon class

class Weapon:

	#lol
	def __init__(self, keyRow, valueRow):
		numberOfKeys = len(keyRow)
		values = {}
		for i in range(0, numberOfKeys-1):
			values[keyRow[i]] = valueRow[i]

	def getValue(self, key):
		return self.values[key]