# mob factory class
from utils.loader import Weapons
from utils.randutils import RandUtils
from settings import *
from character import Character

class MobFactory:

	def __init__(self):
		self.weapons_list = Weapons().list()

	def buildMob(self, areaType, stage):
		print("Building a mob!")
		if areaType == 1:
				return self.populateSynthMob(stage)
	
	def populateSynthMob(self, stage):
		stageCounts = {0:1,1:2,2:2,3:3,4:3,5:4}
		mob = []
		for i in range (1,stageCounts[stage]+1):
			nameString = "synth" + str(i)
			synth = Character(nameString, endurance=19, agility=20, strength=22, dexterity=25, is_playable=False, humanity=0.0)
			possibleWeapons = [0,1,7]
			selectedWeapon = RandUtils.pickRandomFromList(possibleWeapons)
			synth.weapon = self.weapons_list[selectedWeapon]
			mob.append(synth)
		return mob
		
