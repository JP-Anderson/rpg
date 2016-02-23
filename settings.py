#settings
from enum import Enum

PRINT_DETAILED_STATS = True

class ObjectType(Enum):
	WEAPON = 0
	ARMOUR = 1

class ArmourSlot(Enum):
	HEAD = 0
	CHEST = 1
	LEGS = 2

class WeaponType(Enum):
	PISTOL = 0
	SMG = 1
	RIFLE = 2
	SHOTGUN = 3
	ENERGY_PISTOL = 4
	ENERGY_RIFLE = 5
	KNIFE = 6
	SWORD = 7
	CLUB = 8
	
class WeaponClass(Enum):
	CONVENTIONAL = 0
	ENERGY = 1	
	MELEE = 2
	