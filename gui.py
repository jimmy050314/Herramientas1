import tkinter as tk
from tkinter import ttk
def on_click():
	Label1.configure(text="Te dije que no "+name.get())
	Label1.configure(foreground='blue')
	Label1.configure(background='green')
	boton.configure(state='disable')
#	print("click")
pass
win=tk.Tk()
win.title("Hola Gui")
win.resizable(0,0)
#ttk.Label(win,text="Hola etiqueta").grid(row=0,column=0)
#ttk.Button(win,text="click me", comman=on_click).grid(row=1,column=1)
Label1=ttk.Label(win,text="Hola Label")
Label1.grid(row=0,column=0)
boton=ttk.Button(win,text="Dont click me",command=on_click)
boton.grid(row=1,column=1)
name=tk.StringVar()
txtEntry=ttk.Entry(win,textvariable=name)
txtEntry.grid(row=1,column=0)

win.mainloop()
