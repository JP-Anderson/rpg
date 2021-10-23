# mission class
from settings import *
from utils.mobfactory import MobFactory

class Mission:

	def __init__(self, stage_count, weapons):
		self.stages = []
		self.stage_count = stage_count
		mob_factory = MobFactory(weapons)
		for i in range(0,self.stage_count):
			self.stages.append(mob_factory.build_mob(1,i))
	
	def to_string(self):
		for i in range (0, self.stage_count):
			for enemy in self.stages[i]:
				enemy.printStats()
				print()
	
			