# mission class
from src.settings import *
from src.utils.mobfactory import MobFactory

class Mission:

	def __init__(self, missionType, stageCount):
		self.stages = []
		self.stageCount = stageCount
		for i in range(0,self.stageCount):
			self.stages.append(MobFactory.buildMob(1,i))
	
	def toString(self):
		for i in range (0, self.stageCount):
			for enemy in self.stages[i]:
				enemy.printStats()
				print()
	
			