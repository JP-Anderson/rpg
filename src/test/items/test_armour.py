import unittest

from utils.loader import Armours


class TestArmour(unittest.TestCase):

    def setUp(self):
        self.armour = Armours()

    def test_armour_fields(self):
        combat_helmet = self.armour.list()[3]
        self.assertEqual(3, int(combat_helmet.values["ID"]))
        self.assertEqual("Combat Helmet", combat_helmet.values["Name"])
        self.assertEqual(0, int(combat_helmet.values["Slot"]))
        self.assertEqual(4, int(combat_helmet.values["Weight"]))
        self.assertEqual(0.15, float(combat_helmet.values["PhysD"]))
        self.assertEqual(0.07, float(combat_helmet.values["ShkD"]))
        self.assertEqual(0.03, float(combat_helmet.values["BrnD"]))
        self.assertEqual(0.2, float(combat_helmet.values["PsnD"]))
        self.assertEqual(7, int(combat_helmet.values["StrReq"]))
    
    # Instantiate Attack objects and pass them into Armour.absorbDamage() function. https://github.com/JP-Anderson/rpg/blob/master/src/items/armour.py#L22

    # TODO: write test case testing absorbDamage() physical damage modification

    # TODO: write test cases testing absorbDamage() shock, burn and poison damage modification



if __name__ == '__main__':
    unittest.main()
