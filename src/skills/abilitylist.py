# A class to wrap up some of the functionality for a characters ability list

class AbilityList:
	
	def __init__(self):
		self.abilities = []
	
	def add_ability(self, ability):
		self.abilities.append(ability)
	
	def use_ability(self, index, target):
		self.abilities[index].cast(target)
	
	def is_empty(self):
		if not self.abilities:
			return True
		else: return False
	
	def return_name_strings(self):
		strings = []
		if len(self.abilities)>0:
			for ability in self.abilities:
				strings.append(ability.name)
		return strings
	
	def return_ability_costs(self):
		costs = []
		if len(self.abilities)>0:
			for ability in self.abilities:
				costs.append(ability.apCost)
		return costs
