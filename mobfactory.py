# mob factory class
from settings import *
from character import Character

class MobFactory:

	#def __init__(self)
	
	def buildMob(areaType, stage):
		print("Building a mob!")
		if areaType == 1:
			return MobFactory.populateSynthMob(stage)		
	
	def populateSynthMob(stage):
		stageCounts = {0:1,1:2,2:2,3:3,4:3,5:4}
		mob = []
		for i in range (1,stageCounts[stage]+1):
			nameString = "synth" + str(i)
			synth = Character(nameString, endurance=39, agility=20, strength=22, dexterity=25, isPlayable=False, humanity=0.0)
			mob.append(synth)
		return mob