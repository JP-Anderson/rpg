# loaded objects
import os.path

from utils.csvreader import CsvReader
from items.weapon import Weapon
from items.armour import Armour
from skills.buff import Buff


weapons = []
armour = []
buffs = []

def loadCSVs():
	weaponcsv = CsvReader.read(os.path.join("..","data","wep.csv"))
	keys = weaponcsv[0]
	numberOfObjects = len(weaponcsv)
	print("  Loading Weapons")
	for i in range (1,numberOfObjects):
		weapons.append(Weapon(keys,weaponcsv[i]))
		print("    - " + str(weaponcsv[i][1]))
	
	armourcsv = CsvReader.read(os.path.join("..","data","armour.csv"))
	keys = armourcsv[0]
	numberOfObjects = len(armourcsv)
	print("  Loading Armour")
	for i in range (1,numberOfObjects):
		armour.append(Armour(keys,armourcsv[i]))
		print("    - " + str(armourcsv[i][1]))
	
	buffcsv = CsvReader.read(os.path.join("..","data","buff.csv"))
	keys = buffcsv[0]
	numberOfObjects = len(buffcsv)
	print("  Loading Buffs")
	for i in range (1,numberOfObjects):
		buffs.append(Buff(keys,buffcsv[i]))
		print("    - " + str(buffcsv[i][1]))
