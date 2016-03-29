# random utilities
import random

class RandUtils:
	
	def pickRandomFromList(list):
		listLength = len(list)
		probabilityPerItem = 100/listLength/100
		itemRanges = []
		
		rangeStart = 0
		rangeEnd = 0 + probabilityPerItem
		for i in range (1,listLength+1):
			itemRanges.append([rangeStart, rangeEnd])
			rangeStart = rangeEnd
			rangeEnd = rangeEnd + probabilityPerItem
		
		print(itemRanges)
		roll = random.random()
		

