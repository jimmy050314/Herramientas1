import serial
import tkinter as tk
from tkinter import ttk

def ButtonON():
	global arduinoPort
	arduinoPort.write("a".encode())
pass

def ButtonOFF():
	global arduinoPort
	arduinoPort.write("z".encode())
pass

win=tk.Tk()
win.title("ON/OFF")
win.resizable(0,0)
arduinoPort=serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

botonON=ttk.Button(win,text="ON",command=ButtonON)
botonON.grid(row=0,column=0)

botonOFF=ttk.Button(win,text="OFF",command=ButtonOFF)
botonOFF.grid(row=0,column=1)

win.mainloop()

