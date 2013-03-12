import os
from conferror import ConfError
class ConfManager:
	def __init__(self,conf=None):
		if conf is None:
			if os.environ.has_key('HOME'):
				try:
					self.conf_path = os.environ['HOME'] + '/.pybotrc'
					self.conf_file = open(self.conf_path)
				except IOError:
					raise ConfError("could not open conf file")
		else: # lines of with os.environ.has_key
			try:
				#self.conf_path = os.environ['HOME'] + conf
				self.conf_file = open(conf)
			except IOError:
				raise ConfError("could not open conf file")

		for line in self.conf_file:
			if line.startswith("network"):
				if len(line.split("=")[-1].split()) > 1: # more than one entry
					self.network = line.split("=")[-1].split()
				else:
					self.network = line.rstrip().split()[-1]

			elif line.startswith("port"):
				self.port = line.rstrip().split()[-1] # port = 6667

			elif line.startswith("owner"):
				self.owner = line.rstrip().split()[-1] # owner = username

			elif line.startswith("ircpass"):
				self.ircpass = line.rstrip().split()[-1] # ircpass = pass

			elif line.startswith("dbpass"):
				self.dbpass = line.rstrip().split()[-1] # dbpass = pass

			elif line.startswith("channels"): # channels = chan1 chan2 chan3
				c = line.rstrip().split("=")[-1]
				self.channels = c.split()

		if self.network is None or self.port is None or self.channels is None:
				raise ConfError("conf file incorrect")

	def getOwner(self):
		return self.owner

	def getIRCPass(self):
		return self.ircpass

	def getDBPass(self):
		return self.dbpass

	def getChannels(self):
		return self.channels

	def getNetworks(self):
		return self.networks
	
	def getNumNets(self):
		if type(self.network) is str:
			return 1
		else:
			return len(self.network)

	def getNetwork(self):
		return self.network

	def getPort(self):
		return self.port
