# character base class

class Character:

	def __init__(self,
					name="Bob",
					level=1,
					strength=7,
					dexterity=7,
					endurance=7,
					agility=7,
					speed=7,
					humanity=1.0
				):
		
		hp = 50+endurance*8
		ap = 2*speed+2*agility
		print("\"Hello, world!\" said "+name)

	# Stats
	
	name = None
	level = None
	
	strength = None
	dexterity = None
	endurance = None
	agility = None
	speed = None
	humanity = None
	
	hp = None
	ap = None
	
	# Equipment
	weapon = None
	helmet = None
	chestArmour = None
	legArmour = None
	