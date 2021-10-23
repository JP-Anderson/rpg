import unittest

from character import Character, Class

class TestCharacter(unittest.TestCase):
		
	def test_damage_given_to_character_reduces_hp(self):
		character = Character(name="Bob",
				level=1,
				strength=7,
				dexterity=7,
				endurance=7,
				intelligence=7,
				agility=7,
				speed=7,
				humanity=1.0,
				is_playable=True,
				char_class = Class.FIGHTER)
		maxHP = 400 + 7 * 20
		self.assertEqual(maxHP, character.maxHP)
		self.assertEqual(maxHP, character.hp)
		
		character.adjust_health(-maxHP/2)
		self.assertEqual(maxHP/2, character.hp)
		
		character.adjust_health(-maxHP/2+1)
		self.assertEqual(1, character.hp)
	
	def test_is_dead(self):
		character = Character(name="Bob",
				level=1,
				strength=7,
				dexterity=7,
				endurance=7,
				intelligence=7,
				agility=7,
				speed=7,
				humanity=1.0,
				is_playable=True,
				char_class = Class.FIGHTER)
		self.assertFalse(character.is_dead())
		character.adjust_health(-character.maxHP + 1)
		self.assertFalse(character.is_dead())
		character.adjust_health(-1)
		self.assertTrue(character.is_dead())
	
	def test_gain_xp_triggers_level_up(self):
		character = Character(name="Bob",
			level=1,
			strength=7,
			dexterity=7,
			endurance=7,
			intelligence=7,
			agility=7,
			speed=7,
			humanity=1.0,
			is_playable=True,
			char_class = Class.FIGHTER)
		self.assertEqual(0, character.xp)
		self.assertEqual(1, character.level)
		character.gain_xp(100)
		self.assertEqual(2, character.level)
		
	def test_gain_xp_overflow_triggers_multiple_level_up(self):
		character = Character(name="Bob",
			level=1,
			strength=7,
			dexterity=7,
			endurance=7,
			intelligence=7,
			agility=7,
			speed=7,
			humanity=1.0,
			is_playable=True,
			char_class = Class.FIGHTER)
		self.assertEqual(0, character.xp)
		self.assertEqual(1, character.level)
		character.gain_xp(900)
		# 900 XP: level 1 -> 2 (100XP), level 2 -> 3 (300XP), level 3 -> 4 (500XP)
		self.assertEqual(4, character.level)
		
	def test_gain_xp_remainder_applied_towards_next_level(self):
		character = Character(name="Bob",
			level=1,
			strength=7,
			dexterity=7,
			endurance=7,
			intelligence=7,
			agility=7,
			speed=7,
			humanity=1.0,
			is_playable=True,
			char_class = Class.FIGHTER)
		self.assertEqual(0, character.xp)
		self.assertEqual(1, character.level)
		self.assertEqual(100, character.xp_to_next_level())
		character.gain_xp(101)
		self.assertEqual(2, character.level)
		self.assertEqual(1, character.xp)
		self.assertEqual(300, character.xp_to_next_level())
		character.gain_xp(301)
		self.assertEqual(2, character.xp)
		
	
if __name__ == '__main__':
	unittest.main()
