
import tkinter
import TCP_FrameReader

from tkinter import *


root = tkinter.Tk()

def FWRead():
	return None
def FWSendNew():
	return None
def SendFrame():
	return None

mainFrame = Frame(root)
mainFrame.pack()
menu = Menu(root)
menu.add_command(label="Read", command=FWRead)
menu.add_command(label="Send New", command=FWSendNew)
menu.add_separator()
opMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Operations", menu=opMenu)


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

sendButton = Button(tcpRWFrame, text="Send", command=SendFrame)
sendButton.grid(row=8, column=3)

root.config(menu=menu)
root.mainloop()