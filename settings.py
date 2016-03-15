#settings
from enum import Enum
import random

#logging
PRINT_DETAILED_STATS = True
PROMPT = "... "
NESTEDPROMPT = "...... "

#fighter statistic variables
BASE_HEALTH = 400
STARTING_STAT_POINTS = 35
#                ENDURANCE =  1           5              10             15             20             25             30             35             40
CARRY_WEIGHTS_BY_ENDURANCE = [15,17,19,21,23,25,27,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]
#                1   2   3   4    5     6    7  8    9     10    11    12     13   14    15    16
XP_PER_LEVEL = [100,300,500,1000,1500,2500,4000,6000,8000,10000,12000,16000,20000,32000,43000,50000]

#enums
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

class EncumbranceThreshold(Enum):
	LOW = 0.35
	HIGH = 0.7

class Encumbrance(Enum):
	LOW = 0
	MED = 1
	HIGH = 2

class Status(Enum):
	DEAD = 0
	STUNNED = 1
	NORMAL = 2