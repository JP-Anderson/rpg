import unittest

from skills.skill import Skill
from skills.skilltree import SkillTree
from utils.gooey import Gooey, MockGooey


class TestSkillTree(unittest.TestCase):
		
		def test_level_skill_tree_to_max(self):
			mockGUI = MockGooey()
			mockGUI.set_get_user_input_with_list_response(0)
			tree = self.get_example_skill_tree(mockGUI)
			self.assertEqual(0, tree.level)
			tree.levelUp()
			self.assertEqual(1, tree.level)
			tree.levelUp()
			self.assertEqual(2, tree.level)
			tree.levelUp()
			self.assertEqual(2, tree.level)

		def test_is_max_level(self):
			mockGUI = MockGooey()
			mockGUI.set_get_user_input_with_list_response(0)
			tree = self.get_example_skill_tree(mockGUI)
			self.assertFalse(tree.is_max_level())
			tree.levelUp()
			self.assertFalse(tree.is_max_level())
			tree.levelUp()
			self.assertTrue(tree.is_max_level())

		def test_correct_option_strings_for_each_level(self):
			mockGUI = MockGooey()
			mockGUI.set_get_user_input_with_list_response(0)
			tree = self.get_example_skill_tree(mockGUI)
			self.assertEqual(['1-1', '1-2'], tree.getOptionStrings())
			tree.levelUp()
			self.assertEqual(['2-1', '2-2'], tree.getOptionStrings())
			tree.levelUp()
			self.assertEqual([], tree.getOptionStrings())
		
		def test_correct_skill_added_for_each_selection(self):
			skill1Choice1 = Skill("1-1", "Description 1", "Target")
			skill1Choice2 = Skill("1-2", "Description 2", "Passive")
			s2c1 = Skill("2-1", "Description 2 1", "Target")
			s2c2 = Skill("2-2", "Description 2 2", "Target")
			mockGUI = MockGooey()
			mockGUI.set_get_user_input_with_list_response(0)
			tree = SkillTree("Skill Tree Name", "Description", 2, [[skill1Choice1, skill1Choice2],[s2c1, s2c2]], mockGUI)
			self.assertEqual(0, len(tree.selectedSkills))
			tree.levelUp()
			self.assertEqual(1, len(tree.selectedSkills))
			self.assertEqual(skill1Choice1, tree.selectedSkills[0])
			# Mock user input to choose the 2nd Skill for the 2nd decision.
			mockGUI.set_get_user_input_with_list_response(1)
			tree.levelUp()
			self.assertEqual(2, len(tree.selectedSkills))
			self.assertEqual(s2c2, tree.selectedSkills[1])
		
		def get_example_skill_tree(self, mock_gui):
			skill1Choice1 = Skill("1-1", "Description 1", "Target")
			skill1Choice2 = Skill("1-2", "Description 2", "Passive")
			s2c1 = Skill("2-1", "Description 2 1", "Target")
			s2c2 = Skill("2-2", "Description 2 2", "Target")
			return SkillTree("Skill Tree Name", "Description", 2, [[skill1Choice1, skill1Choice2],[s2c1, s2c2]], mock_gui)

if __name__ == '__main__':
	unittest.main()
