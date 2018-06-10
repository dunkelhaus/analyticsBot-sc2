import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status

class BuildingUnits():
	def __init__(self, built, destroyed):
		self.built = built
		self.destroyed = destroyed

class ArmyUnits():
	def __init__(self, spawned, dead):
		self.spawned = spawned
		self.dead = dead

class WorkerUnits():
	def __init__(self, spawned, dead):
		self.spawned = spawned
		self.dead = dead

class State():
	def __init__(self, won, race):
		self.won = won
		self.race = race
