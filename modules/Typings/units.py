import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status

class BuildingUnits():
	def __init__(self, built=0, destroyed=0):
		self.built = built
		self.destroyed = destroyed
	def __str__(self):
		return str("Buildings (build): %d | Buildings (destroyed): %d" %(self.built, self.destroyed))
		

class ArmyUnits():
	def __init__(self, spawned=0, dead=0):
		self.spawned = spawned
		self.dead = dead
	def __str__(self):
                return str("Army Units (spawn): %d | Army Units (dead): %d" %(self.spawned, self.dead))

class WorkerUnits():
	def __init__(self, spawned=0, dead=0):
		self.spawned = spawned
		self.dead = dead
	def __str__(self):
                return str("Worker Units (spawn): %d | Worker Units (dead): %d" %(self.spawned, self.dead))

class State():
	def __init__(self, won=0, race=0):
		self.won = won
		self.race = race
	def __str__(self):
                return str("Race: %d" %(self.race))
