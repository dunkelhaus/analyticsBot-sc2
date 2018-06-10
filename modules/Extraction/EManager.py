import os
import sys
import numpy as np
from Extraction import decodeJSON
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
import sc2reader
from Status.Status import Status
from Typings.playerStats import PlayerStats

class EManager:
	def __init__(self, jsonpath):
		self.status = Status("Extraction")
		self.playerList = self.extractJSON(jsonpath)
		self.examples = self.numpifyPlayers()

	def extractReplayDir(self, dirname):
		replays = sc2reader.load_replays("sc2reader/test_replays/2.1.4")

	def extractJSON(self, jsonpath):
		self.status.message(1, "extractJSON(self, jsonpath)")

		listings = decodeJSON.loadJSON(jsonpath)
		playerList = []
		
		for i in listings:
			player = PlayerStats(i)
			playerList.append(player)

		self.status.message(7)
		self.status.message(0, "extractJSON(self, jsonpath)")
		return playerList

	def numpifyPlayers(self):
		self.status.message(1, "numpifyPlayers(self)")
		examples = []
		
		for player in self.playerList:
			npyplayer = np.array([player.state.race, 
				player.buildings.built, 
				player.buildings.destroyed, 
				player.armyUnits.spawned, 
				player.armyUnits.dead, 
				player.workerUnits.spawned, 
				player.workerUnits.dead])
			examples.append(npyplayer)
		
		return np.asarray(examples)
