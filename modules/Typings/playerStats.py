import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status
from Typings.units import BuildingUnits, ArmyUnits, WorkerUnits, State

class PlayerStats():
	def __init__(self, data):
		self.status = Status("PlayerStats")
		self.state = None
		self.buildings = None
		self.armyUnits = None
		self.workerUnits = None
		self.populate(data)

	def getBuildingUnits(self, playerDict):
		self.status.message(1, "getBuildingUnits(self, playerDict)")

		self.status.message(0, "getBuildingUnits(self, playerDict)")
		return BuildingUnits(playerDict["buildingBuilt"], playerDict["buildingKilled"])

	def getArmyUnits(self, playerDict):
		self.status.message(1, "getArmyUnits(self, playerDict)")

		self.status.message(0, "getArmyUnits(self, playerDict)")
		return ArmyUnits(playerDict["armyBuilt"], playerDict["armyKilled"])

	def getWorkerUnits(self, playerDict):
		self.status.message(1, "getWorkerUnits(self, playerDict)")

		self.status.message(0, "getWorkerUnits(self, playerDict)")
		return WorkerUnits(playerDict["workerBuilt"], playerDict["workerKilled"])

	def getState(self, playerDict):
		self.status.message(1, "getState(self, playerDict)")
		# print(playerDict)
		try:
			if playerDict["result"] == "Loss":
				won = False
			else:
				won = True
	
			if playerDict["race"] == "Zerg":
				race = 0
			elif playerDict["race"] == "Protoss":
				race = 1
			elif playerDict["race"] == "Terran":
				race = 2
			else:
				race = 0
		except KeyError:
			print("Key error occured. Using defaults.")
			won = False
			race = 0
		self.status.message(0, "getState(self, playerDict)")
		return State(won, race)

	def populate(self, playerDict):
		self.status.message(1, "populate(self, playerDict)")
				
		self.state = self.getState(playerDict)
		self.buildings = self.getBuildingUnits(playerDict)
		self.armyUnits = self.getArmyUnits(playerDict)
		self.workerUnits = self.getWorkerUnits(playerDict)

		self.status.message(0, "populate(self, playerDict)")
		return True
