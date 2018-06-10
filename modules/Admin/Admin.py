import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status
from NeuralNet.NNManager import NNManager
from Extraction.EManager import EManager

class Admin():
	def __init__(self):
		self.status = Status("Admin")
