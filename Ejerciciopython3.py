import math
def calculadora():
	Operacion=int(input("Bienvenido, elija la operación que desea realizar \n1.Suma. \n2.Resta. \n3.Multiplicacion. \n4.Division. \n5.Factorial. \n6.Canversión Grados a radianes. \n10.Salir. \n:  "))
	if(Operacion==1):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea sumarlo: "))
		suma=Valor1+Valor2
		print("El resultado de la suma es "+str(suma))
	elif(Operacion==2):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea restarlo: "))
		resta=Valor1-Valor2
		print("El resultado de la suma es "+str(resta))
	elif(Operacion==3):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea multiplicarlo: "))
		multiplicacion=Valor1*Valor2
		print("El resultado de la multiplicacion es "+str(multiplicacion))
	elif(Operacion==4):
		Valor1=int(input("Ingrese un valor: "))
		Valor2=int(input("Ingrese el valor con el que desea dividirlo: "))
		if(Valor2!=0):
			division=Valor1/Valor2
			print("El resultado de la division es "+str(division))
		else:
			print("La division por 0 no es válida")
	elif(Operacion==5):
		Valor1=int(input("Ingrese el valor que desea que desea su factorial: "))
		fact=math.factorial(Valor1)
		print("el resultado de "+str(Valor1)+"! es "+str(fact))
	elif(Operacion==6):
		Valor1=int(input("Ingrese el valor que desea pasar de grados a radianes: "))
		Rad
	elif(Operacion==10):
		return Operacion;
	else:
		print("El número ingresado no es válido")
	return Operacion
pass

while calculadora()!=10:
	pass
