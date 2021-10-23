import unittest

from utils.loader import Weapons


class TestWeapon(unittest.TestCase):

	def setUp(self):
		self.weapons = Weapons()
	
	def test_attack_with_strength_bonus(self):
		sword = self.weapons.list()[13]

		strength = 10
		dex = 1
		attack = sword.attack(strength, dex)

		sword_base_damage = int(sword.values["BaseD"])
		sword_str_bonus = int(sword.values["StrB"])
		self.assertEqual(170, sword_base_damage)
		self.assertEqual(5, sword_str_bonus)
		self.assertEqual(170 + 5 * strength, attack.base_dmg)

	def test_attack_with_dexterity_bonus(self):
		knife = self.weapons.list()[7]

		strength = 10
		dex = 39
		attack = knife.attack(strength, dex)

		knife_base_damage = int(knife.values["BaseD"])
		knife_str_bonus = "-"
		knife_dex_bonus = int(knife.values["DexB"])
		self.assertEqual(100, knife_base_damage)
		self.assertEqual(4, knife_dex_bonus)
		self.assertEqual("-", knife_str_bonus)
		self.assertEqual(100 + 4 * dex, attack.base_dmg)


if __name__ == '__main__':
    unittest.main()
