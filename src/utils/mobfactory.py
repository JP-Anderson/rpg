# mob factory class
from utils.loader import Weapons
from utils.randutils import RandUtils
from settings import *
from character import Character

class MobFactory:

	def __init__(self):
		self.weapons_list = Weapons().list()

	def build_mob(self, area_type, stage):
		print("Building a mob!")
		if area_type == 1:
				return self.populate_synth_mob(stage)
	
	def populate_synth_mob(self, stage):
		stage_counts = {0:1,1:2,2:2,3:3,4:3,5:4}
		mob = []
		for i in range (1,stage_counts[stage]+1):
			name = "synth" + str(i)
			synth = Character(name, endurance=19, agility=20, strength=22, dexterity=25, is_playable=False, humanity=0.0)
			possible_weapons = [0,1,7]
			synth.weapon = self.weapons_list[RandUtils.pick_random_from_list(possible_weapons)]
			mob.append(synth)
		return mob
		
