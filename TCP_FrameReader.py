
class TCPFrame:
	def __init__(self):
		self.sourcePort
		self.destPort
		self.sequenceNum
		self.ackNum
		self.dataOffset
		self.reserved
		self.NS
		self.CWR
		self.ECE
		self.URG
		self.ACK
		self.PSH
		self.RST
		self.SYN
		self.FIN
		self.windowSize
		self.checksum
		self.urgentPtr
		self.payload

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

def writeFrame(frame)
	yield frame.


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
