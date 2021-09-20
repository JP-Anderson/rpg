import unittest

from utils.loader import Weapons


class TestWeapon(unittest.TestCase):

	def setUp(self):
		self.weapons = Weapons()
	
	def test_item(self):
		sword = self.weapons.list()[13]
		self.assertEqual(sword.values["ID"], "13")
		self.assertEqual(sword.values["Name"], "Greatsword")
		self.assertEqual(sword.values["TID"], "7")
		self.assertEqual(sword.values["Class"], "Melee")
		self.assertEqual(sword.values["Type"], "Sword")
		self.assertEqual(sword.values["Weight"], "20")
		self.assertEqual(sword.values["Dodgeability"], "0.58")
		self.assertEqual(sword.values["BaseCritC"], "0.01")
		self.assertEqual(sword.values["CritD"], "0.1")
		self.assertEqual(sword.values["BaseD"], "170")
		self.assertEqual(sword.values["ShkD"], "0")
		self.assertEqual(sword.values["BrnD"], "0")
		self.assertEqual(sword.values["PsnD"], "0")
		self.assertEqual(sword.values["StrR"], "34")
		self.assertEqual(sword.values["StrB"], "5")
		self.assertEqual(sword.values["DexR"], "3")
		self.assertEqual(sword.values["DexB"], "-")
		self.assertEqual(sword.values["AmmoType"], "-")
		self.assertEqual(sword.values["ClipSize"], "-")
		self.assertEqual(sword.values["RndsPerShot"], "-")
		self.assertEqual(sword.values["ShotAP"], "5")
		self.assertEqual(sword.values["ReloadAP"], "-")
		self.assertEqual(sword.values["UpgradeSlots"], "1")


if __name__ == '__main__':
    unittest.main()
