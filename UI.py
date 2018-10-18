
import tkinter
import datetime
import TCP_FrameReader

from tkinter import *
from datetime import datetime
from TCP_FrameReader import *

frameList = []
frameButtonList = []

root = tkinter.Tk()
mainFrame = Frame(root)
mainFrame.pack()

def RmFrameButton(frame, button):
	frameList.remove(frame)
	frameButtonList.remove(button)
	button.destroy()

def AddFrameButton(container, frame, title):
	frame.time = datetime.now().time()
	frameList.append(frame)
	frameButtonList.append(Button(container, height=30, width=150,\
		text=str(frame.time.hour)+":"+str(frame.time.minute)+" - " + title))
		
	#frameButtonList(len(frameButtonList)).config(command=lambda: RmFrameButton(frame,\
	#	frameButtonList(len(frameButtonList))))
	#frameButtonList(len(frameButtonList)).pack(side=BOTTOM)

def FWRead():
	return None
def FWSendNew():
	return None
def SendFrame(frame, title):
	return None

# MENU
menu = Menu(root)
menu.add_command(label="Read", command=FWRead)
menu.add_command(label="Send New", command=FWSendNew)
menu.add_separator()
opMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Operations", menu=opMenu)

# I/O LISTS
ioFrame = Frame(mainFrame)
ioFrame.pack(side=LEFT)
ioLabelFrame = Frame(ioFrame)
ioLabelFrame.pack(side=TOP)
inLabel = Label(ioLabelFrame, text="In", padx=90)
inLabel.pack(side=LEFT)
outLabel = Label(ioLabelFrame, text="Out", padx=90)
outLabel.pack(side=RIGHT)
inLF = LabelFrame(ioFrame, height=400, width=200)
inLF.pack(side=LEFT)
outLF = LabelFrame(ioFrame, height=400, width=200)
outLF.pack(side=RIGHT)
inFrame = Frame(inLF)
outFrame = Frame(outLF)

AddFrameButton(outFrame, TCPFrame(), "Test")
print(frameList[0].time)

# FRAME READ/WRITE PANEL
tcpRWFrame = Frame(mainFrame)
tcpRWFrame.pack(side=RIGHT)

srclbl = Label(tcpRWFrame, text=" Source Port : ")
srclbl.grid(row=0, column=0)
src = Entry(tcpRWFrame, bd=3, width=16)
src.grid(row=0, column=1)
dstlbl = Label(tcpRWFrame, text=" Destination Port : ")
dstlbl.grid(row=0, column=2)
dst = Entry(tcpRWFrame, bd=3, width=16)
dst.grid(row=0, column=3)

seqnlbl = Label(tcpRWFrame, text=" Sequence Number : ")
seqnlbl.grid(row=1, column=0)
seqn = Entry(tcpRWFrame, bd=3, width=32)
seqn.grid(row=1, column=1, columnspan=2)

acknlbl = Label(tcpRWFrame, text=" ACK Number : ")
acknlbl.grid(row=2, column=0)
ackn = Entry(tcpRWFrame, bd=3, width=32)
ackn.grid(row=2, column=1, columnspan=2)

dataofflbl = Label(tcpRWFrame, text=" Data Offset : ")
dataofflbl.grid(row=3, column=0)
dataoff = Entry(tcpRWFrame, bd=3, width=4)
dataoff.grid(row=3, column=1)
reserlbl = Label(tcpRWFrame, text=" Reserved : ")
reserlbl.grid(row=3, column=2)
reser = Entry(tcpRWFrame, bd=3, width=3)
reser.grid(row=3, column=3)

flagFrame = Frame(tcpRWFrame)
flagFrame.grid(row=4, column=0, columnspan=4)
NS = IntVar()
NScb = Checkbutton(flagFrame, text="NS", variable=NS, onvalue=1, offvalue=0)
NScb.grid(row=0, column=0)
CWR = IntVar()
CWRcb = Checkbutton(flagFrame, text="CWR", variable=CWR, onvalue=1, offvalue=0)
CWRcb.grid(row=0, column=1)
ECE = IntVar()
ECEcb = Checkbutton(flagFrame, text="ECE", variable=ECE, onvalue=1, offvalue=0)
ECEcb.grid(row=0, column=2)
URG = IntVar()
URGcb = Checkbutton(flagFrame, text="URG", variable=URG, onvalue=1, offvalue=0)
URGcb.grid(row=1, column=0)
ACK = IntVar()
ACKcb = Checkbutton(flagFrame, text="ACK", variable=ACK, onvalue=1, offvalue=0)
ACKcb.grid(row=1, column=1)
PSH = IntVar()
PSHcb = Checkbutton(flagFrame, text="PSH", variable=PSH, onvalue=1, offvalue=0)
PSHcb.grid(row=1, column=2)
RST = IntVar()
RSTcb = Checkbutton(flagFrame, text="RST", variable=RST, onvalue=1, offvalue=0)
RSTcb.grid(row=2, column=0)
SYN = IntVar()
SYNcb = Checkbutton(flagFrame, text="SYN", variable=SYN, onvalue=1, offvalue=0)
SYNcb.grid(row=2, column=1)
FIN = IntVar()
FINcb = Checkbutton(flagFrame, text="FIN", variable=FIN, onvalue=1, offvalue=0)
FINcb.grid(row=2, column=2)

winszlbl = Label(tcpRWFrame, text=" Window Size : ")
winszlbl.grid(row=5, column=0)
winsz = Entry(tcpRWFrame, bd=3, width=16)
winsz.grid(row=5, column=1)

chksumlbl = Label(tcpRWFrame, text=" Cheksum : ")
chksumlbl.grid(row=6, column=0)
chksum = Entry(tcpRWFrame, bd=3, width=16)
chksum.grid(row=6, column=1)
urgptrlbl = Label(tcpRWFrame, text=" Urgent Pointer : ")
urgptrlbl.grid(row=6, column=2)
urgptr = Entry(tcpRWFrame, bd=3, width=16)
urgptr.grid(row=6, column=3)

PLlbl = Label(tcpRWFrame, text=" Payload : ")
PLlbl.grid(row=7, column=0)
PL = Text(tcpRWFrame, bd=3, width=48, height=5)
PL.grid(row=7, column=1, columnspan=3)

class DisplayFrame:
	def __init__(self):
		self.tcpframe = TCPFrame()

	def GetTCPFrame(self):
		return self.tcpframe

	def GetFrame(self):
		self.tcpframe = TCPFrame()
		self.tcpframe.sourcePort = src.get()
		self.tcpframe.destPort = dst.get()
		self.tcpframe.sequenceNum = seqn.get()
		self.tcpframe.ackNum = ackn.get()
		self.tcpframe.dataOffset = dataoff.get()
		self.tcpframe.reserved = reser.get()
		self.tcpframe.NS = NS.get()
		self.tcpframe.CWR = CWR.get()
		self.tcpframe.ECE = ECE.get()
		self.tcpframe.URG = URG.get()
		self.tcpframe.ACK = ACK.get()
		self.tcpframe.PSH = PSH.get()
		self.tcpframe.RST = RST.get()
		self.tcpframe.SYN = SYN.get()
		self.tcpframe.FIN = FIN.get()
		self.tcpframe.windowSize = winsz.get()
		self.tcpframe.checksum = chksum.get()
		self.tcpframe.urgentPtr = urgptr.get()
		self.tcpframe.payload = PL.get(1.0, END)
		#testFrame = frame
		return self.tcpframe


	def SetFrame(self, frame):
		src.delete(0, END)
		src.insert(0, frame.sourcePort)
		dst.delete(0, END)
		dst.insert(0, frame.destPort)
		seqn.delete(0, END)
		seqn.insert(0, frame.sequenceNum)
		ackn.delete(0, END)
		ackn.insert(0, frame.ackNum)
		dataoff.delete(0, END)
		dataoff.insert(0, frame.dataOffset)
		reser.delete(0, END)
		reser.insert(0, frame.reserved)
		NScb.deselect()
		if (frame.NS == 1): NScb.select()
		CWRcb.deselect()
		if (frame.CWR == 1): CWRcb.select()
		ECEcb.deselect()
		if (frame.ECE == 1): ECEcb.select()
		URGcb.deselect()
		if (frame.URG == 1): URGcb.select()
		ACKcb.deselect()
		if (frame.ACK == 1): ACKcb.select()
		PSHcb.deselect()
		if (frame.PSH == 1): PSHcb.select()
		RSTcb.deselect()
		if (frame.RST == 1): RSTcb.select()
		SYNcb.deselect()
		if (frame.SYN == 1): SYNcb.select()
		FINcb.deselect()
		if (frame.FIN == 1): FINcb.select()
		winsz.delete(0, END)
		winsz.insert(0, frame.windowSize)
		chksum.delete(0, END)
		chksum.insert(0, frame.checksum)
		urgptr.delete(0, END)
		urgptr.insert(0, frame.urgentPtr)
		PL.delete(1.0, END)
		PL.insert(1.0, frame.payload)


displayFrame = DisplayFrame()

sendButton = Button(tcpRWFrame, text="Send", command=lambda: displayFrame.GetFrame())#command=SendFrame)
sendButton.grid(row=8, column=3)
setButton = Button(tcpRWFrame, text="Set", command=lambda: displayFrame.SetFrame(displayFrame.GetTCPFrame()))
setButton.grid(row=9, column=3)


root.config(menu=menu)
root.mainloop()