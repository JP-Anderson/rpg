# random utilities
import random

class RandUtils:
	
	def pick_random_from_list(list):
		list_length = len(list)
		probability_per_item = 100/list_length/100
		item_ranges = []
		
		range_start = 0
		range_end = 0 + probability_per_item
		i = 0
		while i < list_length:
			item_ranges.append([range_start, range_end])
			range_start = range_end
			range_end = range_end + probability_per_item
			i = i +1
		
		print(item_ranges)
		roll = random.random()
		
		selection = -1
		for range in item_ranges:
			if roll >= range[0] and roll < range[1]:
				selection = item_ranges.index(range)
				print(str(selection))
				print(str(roll))
		
		if selection != -1:	return list[selection]
		else: return None
