from __future__ import division
from sys import argv
import json
import numpy as np

class NeuralNetwork:
	def __init__(self):
		self.x = []
		self.y = []

	def predict(self, input):
		"""
		"""

		return self.w * input + self.b


	def train(self, x, y):
		"""
		Function is responsible for finding linear regression line and modifying w,b 
		to model function y(x) = x * w + b
		Called only once 

		:param x: input set of vals from game
		:param y: output set of val from game
		:return:  no return val
		"""

		#define the input domain
		self.x = x

		#input mapped vals 
		self.y = y 

		#define slope 
		self.w = 0

		#define intercept
		self.b = 0

		#define set of all possible 
		self.model = []

		#define set of errors for each model value which is defined by error function ( model - y )^2
		self.error = []

		self.b, self.w = self.regressionFit(x, y)

	def regressionFit(self, X, Y):
		xbar = sum(X)/len(X)
		ybar = sum(Y)/len(Y)
		n = len(X) # or len(Y)

    		numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    		denum = sum([xi**2 for xi in X]) - n * xbar**2

    		b = numer / denum
    		a = ybar - b * xbar

		return a, b

def main():

	with open('output.json') as data_file:
		data = json.load(data_file)
		length = len(data)
		networks = [None] * 6
		for i in range(0, 6):
			networks[i] = NeuralNetwork()

		x = []
		y = []

		# determine y fields
		for i in range(0, length): 
			if data[str(i)]['0']['result'] == 'Win':
				y.append(1)
				y.append(0)
			else:
				y.append(0)
				y.append(1)

		# determine buildings built
                x = []
		for i in range(0, length):
			x.append(data[str(i)]['0']['buildingBuilt'])
			x.append(data[str(i)]['1']['buildingBuilt'])
		networks[0].train(x, y)

		# determine buildings killed
                x = []
		for i in range(0, length): 
			x.append(data[str(i)]['0']['buildingKilled'])
			x.append(data[str(i)]['1']['buildingKilled'])
		networks[1].train(x, y)

		# determine army built
                x = []
		for i in range(0, length): 
			x.append(data[str(i)]['0']['armyBuilt'])
			x.append(data[str(i)]['1']['armyBuilt'])
		networks[2].train(x, y)

		# determine army killed
                x = []
		for i in range(0, length): 
			x.append(data[str(i)]['0']['armyKilled'])
			x.append(data[str(i)]['1']['armyKilled'])
		networks[3].train(x, y)

		# determine worker built
                x = []
		for i in range(0, length): 
			x.append(data[str(i)]['0']['workerBuilt'])
			x.append(data[str(i)]['1']['workerBuilt'])
		networks[4].train(x, y)

		# determine worker killed
                x = []
		for i in range(0, length): 
			x.append(data[str(i)]['0']['workerKilled'])
			x.append(data[str(i)]['1']['workerKilled'])
		networks[5].train(x, y)
		

		x = []
		x.append(networks[0].predict(int(argv[1])))
		x.append(networks[1].predict(int(argv[2])))
		x.append(networks[2].predict(int(argv[3])))
		x.append(networks[3].predict(int(argv[4])))
		x.append(networks[4].predict(int(argv[5])))
		x.append(networks[5].predict(int(argv[6])))

		#print x
		#print("Min index: ", x.index(min(x)))

		ind = x.index(min(x))
		strc = "Focus more on _INSERT_HERE_"
		
		if ind == 0:
			strc = strc.replace("_INSERT_HERE_", "building buildings")
		elif ind == 1:
			strc = strc.replace("_INSERT_HERE_", "destroying enemy buildings")
		elif ind == 2:
			strc = strc.replace("_INSERT_HERE_", "building your army")
		elif ind == 3:
			strc = strc.replace("_INSERT_HERE_", "destroying enemy army")
		elif ind == 4:
			strc = strc.replace("_INSERT_HERE_", "building more workers")
		elif ind == 5:
			strc = strc.replace("_INSERT_HERE_", "destroying enemy workers")
		
		print strc



if __name__ == '__main__':
	main()
