def calculadora():
	Operacion=int(input("Bienvenido, elija la operación que desea realizar \n1.Suma. \n2.Resta. \n3.Multiplicacion. \n4.Division. \n:  "))
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
	else:
		print("El número ingresado no es válido")
pass
calculadora()

