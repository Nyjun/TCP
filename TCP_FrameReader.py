
import datetime
from datetime import datetime


class TCPFrame:
	def __init__(self):
		self.sourcePort = ""
		self.destPort = ""
		self.sequenceNum = ""
		self.ackNum = ""
		self.dataOffset = 0
		self.reserved = 0
		self.NS = 0
		self.CWR = 0
		self.ECE = 0
		self.URG = 0
		self.ACK = 0
		self.PSH = 0
		self.RST = 0
		self.SYN = 0
		self.FIN = 0
		self.windowSize = ""
		self.checksum = ""
		self.urgentPtr = ""
		self.payload = ""

		self.time

	def sourcePort(self):
		return self.sourcePort
	def sourcePort(self, val):
		self.sourcePort = val
	def destPort(self):
		return self.destPort
	def destPort(self, val):
		self.destPort = val
	def sequenceNum(self):
		return self.sequenceNum
	def sequenceNum(self, val):
		self.sequenceNum = val
	def ackNum(self):
		return self.ackNum
	def ackNum(self, val):
		self.ackNum = val
	def dataOffset(self):
		return self.dataOffset
	def dataOffset(self, val):
		self.dataOffset = val
	def reserved(self):
		return self.reserved
	def reserved(self, val):
		self.reserved = val
	def NS(self):
		return self.NS
	def NS(self, val):
		self.NS = val
	def CWR(self):
		return self.CWR
	def CWR(self, val):
		self.CWR = val
	def ECE(self):
		return self.ECE
	def ECE(self, val):
		self.ECE = val
	def URG(self):
		return self.URG
	def URG(self, val):
		self.URG = val
	def ACK(self):
		return self.ACK
	def ACK(self, val):
		self.ACK = val
	def PSH(self):
		return self.PSH
	def PSH(self, val):
		self.PSH = val
	def RST(self):
		return self.RST
	def RST(self, val):
		self.RST = val
	def SYN(self):
		return self.SYN
	def SYN(self, val):
		self.SYN = val
	def FIN(self):
		return self.FIN
	def FIN(self, val):
		self.FIN = val
	def windowSize(self):
		return self.windowSize
	def windowSize(self, val):
		self.windowSize = val
	def checksum(self):
		return self.checksum
	def checksum(self, val):
		self.checksum = val
	def urgentPtr(self):
		return self.urgentPtr
	def urgentPtr(self, val):
		self.urgentPtr = val
	def payload(self):
		return self.payload
	def payload(self, val):
		self.payload = val
	def time(self):
		return self.time
	def time(self, val):
		self.time = val
	

def checkFrame(frame):
	return True

def readFrame(input):
	frame = TCPFrame()
	frame.sourcePort = f.read() + f.read()
	frame.destPort = f.read() + f.read()
	frame.sequenceNum = f.read() + f.read() + f.read() + f.read()
	frame.ackNum = f.read() + f.read() + f.read() + f.read()

	tmp = ord(f.read())
	frame.dataOffset = tmp >> 4
	frame.reserved = (tmp - frame.dataOffset << 4) >> 1
	frame.NS = tmp & 1

	tmp = ord(f.read())
	frame.CWR = (tmp >> 7) & 1
	frame.ECE = (tmp >> 6) & 1
	frame.URG = (tmp >> 5) & 1
	frame.ACK = (tmp >> 4) & 1
	frame.PSH = (tmp >> 3) & 1
	frame.RST = (tmp >> 2) & 1
	frame.SYN = (tmp >> 1) & 1
	frame.FIN = tmp & 1

	frame.windowSize = f.read() + f.read()
	frame.checksum = f.read() + f.read()
	frame.urgentPtr = f.read() + f.read()
	for byte in f.read():
		frame.payload = frame.payload + byte
	if checkFrame:
		return frame
	else:
		return None

def writeFrame(frame):
	return None


def bytes():
	f = open("myfile", "rb")
	try:
		byte = f.read(1)
		while byte != "":
			# Do stuff with byte.
			byte = f.read(1)
	finally:
		f.close()

def bits(f):
    bytes = (ord(b) for b in f.read())
    for b in bytes:
        for i in xrange(8):
            yield (b >> i) & 1

#for b in bits(open('binary-file.bin', 'r')):
#    print b
