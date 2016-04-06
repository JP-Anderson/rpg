# A class to wrap up some of the functionality for a characters ability list

class AbilityList:
	
	def __init__(self):
		self.abilities = []
	
	def addAbility(self, ability):
		self.abilities.append(ability)
	
	def useAbility(self, index, target):
		self.abilities[index].cast(target)
	
	def isEmpty(self):
		if not self.abilities:
			return True
		else: return False
	
	def returnNameStrings(self):
		strings = []
		if len(self.abilities)>0:
			for ability in self.abilities:
				strings.append(ability.name)
		return strings
	
	def returnAbilityCosts(self):
		costs = []
		if len(self.abilities)>0:
			for ability in self.abilities:
				costs.append(ability.apCost)
		return costs
