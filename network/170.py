import json
import numpy as numpy
from pprint import pprint

with open('output.json') as f:
    data = json.load(f)
    dataLength = len(data)
    print dataLength
    playerOneMatrix = []
    playerOneResult = []
    playerTwoMatrix = []
    playerTwoResult = []
    for x in range(0, dataLength-1):
		armyBuiltPlayerOne = data[str(x)]['1']['armyBuilt']
		armyKilledPlayerOne = data[str(x)]['1']['armyKilled']
		buildingBuiltPlayerOne = data[str(x)]['1']['buildingBuilt']
		buildingKilledPlayerOne = data[str(x)]['1']['buildingKilled']
		workerKilledPlayerOne = data[str(x)]['1']['workerKilled']
		workerBuiltPlayerOne = data[str(x)]['1']['workerBuilt']
		pidPlayerOne = data[str(x)]['1']['pid']
		resultPlayerOne = data[str(x)]['1']['result']
		resultPlayerOne = resultPlayerOne.encode('ascii','ignore')
		if resultPlayerOne == "Win":
			resultPlayerOne = 1
			print resultPlayerOne
		if resultPlayerOne == "Loss":
			resultPlayerOne = 0
			print resultPlayerOne

		armyBuiltPlayerTwo = data[str(x)]['0']['armyBuilt']
		armyKilledPlayerTwo = data[str(x)]['0']['armyKilled']
		buildingBuiltPlayerTwo = data[str(x)]['0']['buildingBuilt']
		buildingKilledPlayerTwo = data[str(x)]['0']['buildingKilled']
		workerKilledPlayerTwo = data[str(x)]['1']['workerKilled']
		workerBuiltPlayerTwo = data[str(x)]['1']['workerBuilt']
		pidPlayerTwo = data[str(x)]['0']['pid']
		resultPlayerTwo = data[str(x)]['0']['result']
		resultPlayerTwo = resultPlayerTwo.encode('ascii','ignore')
		if resultPlayerTwo == "Loss":
			resultPlayerTwo = 0
			print resultPlayerTwo
		if resultPlayerTwo == "Win":
			resultPlayerTwo = 1
			print resultPlayerTwo


		armyDestroyedPlayerOne = armyKilledPlayerTwo
		buildingDestroyedPlayerOne = buildingKilledPlayerTwo
		workerDestroyedPlayerOne = workerKilledPlayerTwo
		armyDestroyedPlayerTwo = armyKilledPlayerOne
		buildingDestroyedPlayerTwo = buildingKilledPlayerOne
		workerDestroyedPlayerTwo = workerKilledPlayerOne
		rowP1 = []
		rowP2 = []
		rowP1.append(armyBuiltPlayerOne)
		rowP1.append(armyKilledPlayerOne)
		rowP1.append(armyDestroyedPlayerOne)
		rowP2.append(armyBuiltPlayerTwo)
		rowP2.append(armyKilledPlayerTwo)
		rowP2.append(armyDestroyedPlayerTwo)

		playerOneMatrix.append(rowP1)
		playerTwoMatrix.append(rowP2)
		playerTwoResult.append(resultPlayerTwo)
		playerOneResult.append(resultPlayerOne)

pprint(playerOneMatrix)
pprint(playerOneResult)
pprint(playerTwoResult)
pprint(playerTwoMatrix)

		





















