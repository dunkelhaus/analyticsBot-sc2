import os
import sys
import json
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status

def loadJSON(path):
	status = Status("Extraction")
	status.message(1, "loadJSON(path)")
	with open(path) as f:
		datadict = json.load(f)

	listings = []
	for match in datadict:
                        for player in datadict[match]:
                                listings.append(datadict[match][player])

	status.message(0, "loadJSON(path)")
	return listings

