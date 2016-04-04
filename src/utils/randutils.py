# random utilities
import random

class RandUtils:
	
	def pickRandomFromList(list):
		listLength = len(list)
		probabilityPerItem = 100/listLength/100
		itemRanges = []
		
		rangeStart = 0
		rangeEnd = 0 + probabilityPerItem
		i = 0
		while i < listLength:
			itemRanges.append([rangeStart, rangeEnd])
			rangeStart = rangeEnd
			rangeEnd = rangeEnd + probabilityPerItem
			i = i +1
		
		print(itemRanges)
		roll = random.random()
		
		selection = -1
		for range in itemRanges:
			if roll >= range[0] and roll < range[1]:
				selection = itemRanges.index(range)
				print(str(selection))
				print(str(roll))
		
		if selection != -1:	return list[selection]
		else: return None
