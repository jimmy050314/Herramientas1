import serial
import tkinter as tk
from tkinter import ttk
puerto= serial.Serial('/dev/ttyACM0',9600,timeout=1)
line = puerto.readline()
prendido = False

def on_prender1():
        global puerto
#       puerto.open()
        puerto.write("b".encode())
pass

def on_prender():
        global puerto
#       puerto.open()
        global line
        if (line <= 10):
                boton1.configure(state='disable')

pass


win = tk.Tk()
win.title("Encender y apagar")
win.resizable(0,0)
log = tk.Text ( win, width=10, height=10, takefocus=0)
log.grid(row=1,column=0)

indice="0.0"

def readSerial():
	global puerto
	log.index(indice)
	line=puerto.readline()
	log.insert(indice,line)
	if "cm" in str(line):
		if len(line[:-6]) ==1:
			boton1.configure(state='enable')
		elif len(line[:-6]) != 1:
			boton1.configure(state='disable')

	win.after(10,readSerial)
pass

win.after(100, readSerial)

label=ttk.Label(win,text=" Bombillo 1:")
label.grid(row=1,column=2)
boton=ttk.Button(win,text=" ON - OFF ",command=on_prender1)
boton.grid(row=1,column=3)
label2=ttk.Label(win,text=" Bombillo 2 :")
label2.grid(row=3,column=2)
boton1=ttk.Button(win,text=" ON - OFF ",command=on_prender)
boton1.grid(row=3,column=3)
label3=ttk.Label(win,text=" Sensores :")
label3.grid(row=0,column=0)

win.mainloop()


