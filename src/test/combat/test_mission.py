import unittest

from utils.state import *

from combat.mission import Mission

class TestMission(unittest.TestCase):

	def test_new_synth_mission(self):
		mission = Mission(4, weapons)
		# Assert 4 stages
		self.assertEqual(4, len(mission.stages))
		# First stage has 1 enemy
		self.assertEqual(1, len(mission.stages[0]))
		# Second stage has 2 enemies
		self.assertEqual(2, len(mission.stages[1]))
		# Third stage has 2 enemies
		self.assertEqual(2, len(mission.stages[2]))
		# Fourth stage has 3 enemies
		self.assertEqual(3, len(mission.stages[3]))
		for i in range(0, 3):
			for enemy in mission.stages[i]:
				self.assertEqual("synth", enemy.name[0:5])


if __name__ == '__main__':
	unittest.main()
