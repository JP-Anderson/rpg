import unittest

from skills.skill import Skill
from skills.skilltree import SkillTree
from utils.gooey import Gooey, MockGooey


class TestSkillTree(unittest.TestCase):
		
		def test_level_skill_tree_to_max(self):
			skill1Choice1 = Skill("1-1", "Description 1", "Target")
			skill1Choice2 = Skill("1-2", "Description 2", "Passive")
			s2c1 = Skill("2-1", "Description 2 1", "Target")
			s2c2 = Skill("2-2", "Description 2 2", "Target")
			print("1")
			mockGUI = MockGooey()
			mockGUI.setGetUserInputWithListResponse(0)
			tree = SkillTree("Skill Tree Name", "Description", 2, [[skill1Choice1, skill1Choice2],[s2c1, s2c2]], mockGUI)
			
			self.assertEqual(0, tree.level)
			tree.levelUp()
			self.assertEqual(1, tree.level)
			tree.levelUp()
			self.assertEqual(2, tree.level)
			tree.levelUp()
			self.assertEqual(2, tree.level)

		def test_is_max_level(self):
			skill1Choice1 = Skill("1-1", "Description 1", "Target")
			skill1Choice2 = Skill("1-2", "Description 2", "Passive")
			s2c1 = Skill("2-1", "Description 2 1", "Target")
			s2c2 = Skill("2-2", "Description 2 2", "Target")
			print("1")
			mockGUI = MockGooey()
			mockGUI.setGetUserInputWithListResponse(0)
			tree = SkillTree("Skill Tree Name", "Description", 2, [[skill1Choice1, skill1Choice2],[s2c1, s2c2]], mockGUI)
			self.assertFalse(tree.is_max_level())
			tree.levelUp()
			self.assertFalse(tree.is_max_level())
			tree.levelUp()
			self.assertTrue(tree.is_max_level())

		def test_get_option_strings(self):
			skill1Choice1 = Skill("1-1", "Description 1", "Target")
			skill1Choice2 = Skill("1-2", "Description 2", "Passive")
			s2c1 = Skill("2-1", "Description 2 1", "Target")
			s2c2 = Skill("2-2", "Description 2 2", "Target")
			mockGUI = MockGooey()
			mockGUI.setGetUserInputWithListResponse(0)
			tree = SkillTree("Skill Tree Name", "Description", 2, [[skill1Choice1, skill1Choice2],[s2c1, s2c2]], mockGUI)
			self.assertEqual(['1-1', '1-2'], tree.getOptionStrings())
			self.assertEqual(0, tree.level)
			tree.levelUp()
			self.assertEqual(1, len(tree.selectedSkills))
			self.assertEqual(skill1Choice1, tree.selectedSkills[0])
			self.assertEqual(['2-1', '2-2'], tree.getOptionStrings())
			self.assertEqual(1, tree.level)
			# Mock user input to choose the 2nd Skill for the 2nd decision.
			mockGUI.setGetUserInputWithListResponse(1)
			tree.levelUp()
			self.assertEqual(2, len(tree.selectedSkills))
			self.assertEqual(s2c2, tree.selectedSkills[1])
			self.assertEqual([], tree.getOptionStrings())
			self.assertEqual(2, tree.level)


if __name__ == '__main__':
	unittest.main()
