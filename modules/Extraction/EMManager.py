import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2")
import sc2reader

class EMManager:
	def __init__(self):
		self.status = Status("Extraction")
		self.player = None
		self.opponent = None

	def extractReplayDir(self, dirname):
		replays = sc2reader.load_replays("/home/service/
