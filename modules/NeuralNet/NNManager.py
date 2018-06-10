import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status
from NeuralNet.gan.gan import GAN

class NNManager():
	def __init__(self):
		self.status = Status("NNManager")
		self.datapath = None
	
	def buildGAN(self, epochs=30000000, batch_size=32, sample_interval=200):
		self.status.message(1, "buildGAN(self, epochs, batch_size, sample_interval")
		gan = GAN()
		gan.train(epochs, batch_size, sample_interval)

		self.status.message(0, "buildGAN(self, epochs, batch_size, sample_interval")
		return True

