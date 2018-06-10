import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status
from NeuralNet.NNManager import NNManager
from Extraction.EManager import EManager
from Typings.playerStats import PlayerStats

class Admin():
	def __init__(self):
		self.status = Status("Admin")
		self.extraction = EManager('/home/service/analyticsBot-sc2/modules/Extraction/jsondump/output.json')
		self.neuralnet = NNManager()
		self.neuralnet.buildGAN(self.extraction.examples)
