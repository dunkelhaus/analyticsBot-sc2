import os
import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status
from NeuralNet.gan.gan import GAN

class NNManager():
	def __init__(self):
		self.status = Status("NNManager")
		self.datapath = None
	
	def buildGAN(self, trainset, epochs=30000, batch_size=25, sample_interval=200):
		self.status.message(1, "buildGAN(self, trainset, epochs, batch_size, sample_interval")
		gan = GAN()
		gan.train(trainset, epochs, batch_size, sample_interval)

		self.status.message(0, "buildGAN(self, trainset, epochs, batch_size, sample_interval")
		return True

