# mission class
from settings import *
from utils.mobfactory import MobFactory

class Mission:

	def __init__(self, missionType, stageCount):
		self.stages = []
		self.stageCount = stageCount
		mob_factory = MobFactory()
		for i in range(0,self.stageCount):
			self.stages.append(mob_factory.buildMob(1,i))
	
	def toString(self):
		for i in range (0, self.stageCount):
			for enemy in self.stages[i]:
				enemy.printStats()
				print()
	
			