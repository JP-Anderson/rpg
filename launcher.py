# game launcher class
import state
from mission import Mission
from settings import *

class Launcher:
	
	print("Launching")
	state.loadCSVs()
	
	m1 = Mission(1,4)
	m1.toString()