# skill and skill tree testing class
from settings import *

from skilltree import SkillTree
from skill import Skill


class SkillTest:

	DOS = Skill("DOS", "Chance to freeze an enemy for X turns", "Target")
	overload = Skill("Overload", "Do X tech damage to target", "Target")
	
	dBoost = Skill("Damage boost", "Boosts damage of hacking attacks", "Passive")
	persistence = Skill("Persistence","Cast buffs last for longer","Passive")
	
		
	tree = SkillTree("BH", "Hacking", 2, [[DOS,overload],[dBoost,persistence]])
	
	print("Level 0")
	tree.toString()
	
	tree.levelUp()
	print("Level 1")
	tree.toString()
	
	
	tree.levelUp()
	print("Level 2")
	tree.toString()
	
	tree.levelUp()
	
	