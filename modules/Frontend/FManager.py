import os
import sys
import socket
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status

class FManager():
	def __init__(self):
		self.status = Status("FManager")
		self.sitestatus = False

	def isRunning(self):
		self.status.message(1, "isRunning(self)")
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(('0.0.0.0',3000))
		sock.close()

		if result == 0:
			self.sitestatus = True
			self.status.message(9)
		else:
			self.sitestatus = False
			self.status.message(8)
		
		self.status.message(0, "isRunning(self)")
				
		return self.sitestatus
