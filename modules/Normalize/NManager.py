import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Typings.playerStats import PlayerStats
from Status.Status import Status

class NManager():
	def __init__(self, playerStats):
		self.status = Status("NManager")
		self.playerStats = playerStats
		self.normalstats = self.normalize()

	def normalize(self):
		self.status.message(1, "normalize(self)")
		stats = PlayerStats()
		stats.state.race = self.bounds(self.playerStats[0], 0, 1)
		stats.buildings.built = self.bounds(self.playerStats[1], 0, 300)
		stats.buildings.destroyed = self.bounds(self.playerStats[2], 0, 50)
		stats.armyUnits.spawned = self.bounds(self.playerStats[3], 0, 1000)
		stats.armyUnits.dead = self.bounds(self.playerStats[4], 0, 500)
		stats.workerUnits.spawned = self.bounds(self.playerStats[5], 0, 1000)
		stats.workerUnits.dead = self.bounds(self.playerStats[6], 0, 500)

		self.status.message(0, "normalize(self)")
		return stats

	def bounds(self, value, lower, upper):
		# self.status.message(1, "bounds(self, value, lower, upper)")
		diff = upper - lower
		result = int((diff * value) + 1)

		# self.status.message(0, "bounds(self, value, lower, upper)")
		return result
