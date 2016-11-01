import tkinter as tk
from tkinter import ttk
from tkinter import *

def on_button5Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+".")
pass

def on_button6Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"0")
pass

def on_button7Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"1")
pass

def on_button8Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"2")
pass

def on_button9Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"3")
pass

def on_button10Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"4")
pass

def on_button11Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"5")
pass

def on_button12Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"6")
pass

def on_button13Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"7")
pass

def on_button14Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"8")
pass

def on_button15Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"9")
pass

def on_button16Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"+")
pass

def on_button17Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"-")
pass

def on_button18Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"*")
pass
def on_button19Click():
   textoActual=label5Text.get()
   label5Text.set(textoActual+"/")
pass

def on_button20Click():
   textoActual=label5Text.get()
   label5Text.set(" ")
pass

def on_button21Click():
   textoActual=label5Text.get()
   calculo=0
   calculo=eval(label5Text.get())
   label5Text.set(str(calculo))
pass

win=tk.Tk()
win.title("Calculadora")
win.resizable(0,0)
Label1=ttk.Label(win,text="Bienvenido, ingrese a continuación los valores y la operación que desea realizar.")
Label1.grid(row=0,column=0)

boton1=ttk.Button(win,text="7",command=on_button13Click)
boton1.grid(row=3,column=2)

boton2=ttk.Button(win,text="8",command=on_button14Click)
boton2.grid(row=3,column=3)

boton3=ttk.Button(win,text="9",command=on_button15Click)
boton3.grid(row=3,column=4)

boton4=ttk.Button(win,text="4",command=on_button10Click)
boton4.grid(row=4,column=2)

boton5=ttk.Button(win,text="5",command=on_button11Click)
boton5.grid(row=4,column=3)

boton6=ttk.Button(win,text="6",command=on_button12Click)
boton6.grid(row=4,column=4)

boton7=ttk.Button(win,text="1",command=on_button7Click)
boton7.grid(row=5,column=2)

boton8=ttk.Button(win,text="2",command=on_button8Click)
boton8.grid(row=5,column=3)

boton9=ttk.Button(win,text="3",command=on_button9Click)
boton9.grid(row=5,column=4)

boton10=ttk.Button(win,text="0",command=on_button6Click)
boton10.grid(row=6,column=3)

boton11=ttk.Button(win,text=".",command=on_button5Click)
boton11.grid(row=6,column=4)

boton12=ttk.Button(win,text="+",command=on_button16Click)
boton12.grid(row=3,column=6)

boton13=ttk.Button(win,text="-",command=on_button17Click)
boton13.grid(row=3,column=7)

boton14=ttk.Button(win,text="*",command=on_button18Click)
boton14.grid(row=4,column=6)

boton15=ttk.Button(win,text="/",command=on_button19Click)
boton15.grid(row=4,column=7)

boton16=ttk.Button(win,text="=",command=on_button21Click)
boton16.grid(row=5,column=7)

boton17=ttk.Button(win,text="CE",command=on_button20Click)
boton17.grid(row=5,column=6)

Label4=ttk.Label(win,text="Resultado")
Label4.grid(row=7,column=0)
Res=tk.StringVar()
Label5=ttk.Label(win,text="")
label5Text=tk.StringVar()
Label5.configure(textvar=label5Text)
Label5.grid(row=7,column=1)

win.mainloop()
