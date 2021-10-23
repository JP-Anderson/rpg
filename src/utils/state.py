# loaded objects
import os.path

from utils.csvreader import CsvReader
from items.weapon import Weapon
from items.terminal import Terminal
from items.armour import Armour
from skills.buff import Buff


weapons = []
terminals = []
armours = []
buffs = []

def load_csvs():
	weaponcsv = CsvReader.read(os.path.join("..","data","wep.csv"))
	keys = weaponcsv[0]
	number_of_objects = len(weaponcsv)
	print("  Loading Weapons")
	for i in range (1,number_of_objects):
		weapons.append(Weapon(keys,weaponcsv[i]))
		print("    - " + str(weaponcsv[i][1]))
		
	terminalcsv = CsvReader.read(os.path.join("..","data","terminal.csv"))
	keys = terminalcsv[0]
	number_of_objects = len(terminalcsv)
	print("  Loading Terminals")
	for i in range (1,number_of_objects):
		terminals.append(Terminal(keys,terminalcsv[i]))
		print("    - " + str(terminalcsv[i][1]))
	
	armourcsv = CsvReader.read(os.path.join("..","data","armour.csv"))
	keys = armourcsv[0]
	number_of_objects = len(armourcsv)
	print("  Loading Armour")
	for i in range (1,number_of_objects):
		armours.append(Armour(keys,armourcsv[i]))
		print("    - " + str(armourcsv[i][1]))
	
	buffcsv = CsvReader.read(os.path.join("..","data","buff.csv"))
	keys = buffcsv[0]
	number_of_objects = len(buffcsv)
	print("  Loading Buffs")
	for i in range (1,number_of_objects):
		buffs.append(Buff(keys,buffcsv[i]))
		print("    - " + str(buffcsv[i][1]))
