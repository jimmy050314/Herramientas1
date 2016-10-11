import math
def calculadora():
	Operacion=int(input("Bienvenido, elija la operación que desea realizar: \n1.Suma. \n2.Resta. \n3.Multiplicacion. \n4.Division. \n5.Factorial. \n6.Conversión Grados a radianes. \n7.Conversión radianes a grados. \n8.Área de una esfera. \n9.Logaritmo. \n10.Salir. \n: "))
	if(Operacion==1):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea sumarlo: "))
		suma=Valor1+Valor2
		print("El resultado de la suma es "+str(suma)+"\n")
	elif(Operacion==2):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea restarlo: "))
		resta=Valor1-Valor2
		print("El resultado de la suma es "+str(resta)+"\n")
	elif(Operacion==3):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea multiplicarlo: "))
		multiplicacion=Valor1*Valor2
		print("El resultado de la multiplicacion es "+str(multiplicacion)+"\n")
	elif(Operacion==4):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea dividirlo: "))
		if(Valor2!=0):
			division=Valor1/Valor2
			print("El resultado de la division es "+str(division)+"\n")
		else:
			print("La division por 0 no es válida \n")
	elif(Operacion==5):
		Valor1=int(input("Ingrese el valor que desea que desea su factorial: "))
		fact=math.factorial(Valor1)
		print("El resultado de "+str(Valor1)+"! es "+str(fact)+"\n")
	elif(Operacion==6):
		Valor1=float(input("Ingrese el valor que desea pasar de grados a radianes: "))
		Rad=math.degrees(Valor1)
		print("El valor de "+str(Valor1)+" en radianes es "+str(Rad)+"\n")
	elif(Operacion==7):
		Valor1=float(input("Ingrese el valor que desea pasar de radianes a grados: "))
		Grad=math.radians(Valor1)
		print("El valor de "+str(Valor1)+" en grados es "+str(Grad)+"\n")
	elif(Operacion==8):
		Valor1=float(input("Ingrese el radio de la esfera: "))
		area=4*math.pi*(Valor1*Valor1)
		print("El area de la esfera es "+str(area)+"\n")
	elif(Operacion==9):
		Valor1=float(input("Ingrese el número que le quiere aplicar el logaritmo: "))
		base=float(input("Ingrese la base del logaritmo: "))
		log=math.log(Valor1,base)
		print("El valor de Log("+str(Valor1)+") en base "+str(base)+" es "+str(log)+"\n")
	elif(Operacion==10):
		print("Hasta pronto!")
		return Operacion;
	else:
		print("El número ingresado no es válido.")
	return Operacion
pass

while calculadora()!=10:
	pass
