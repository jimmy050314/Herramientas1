def modulo():
	print("Bienvenido, a continuacion se le pedirán 3 valores, el módulo y la operación que desea realizar para que el resultado mostrado sea la operación elegida de las 3 operaciones.")
	e=int(input("Ingrese el número de la operación que desea realizar: \n1.Suma. \n2.Resta. \n3.Multiplicación. \n" ))
	if(0<e<4):
		a=int(input("Ingrese el primer valor: "))
		b=int(input("Ingrese el segundo valor: "))
		c=int(input("Ingrese el tercer valor: "))
		d=int(input("Ingrese el módulo: "))
		if(e==1):
			res=(a%d)+(b%d)+(c%d)
			print("Resultado="+str(res))
		elif(e==2):
			res=(a%d)-(b%d)-(c%d)
			print("Resultado="+str(res))
		elif(e==3):
			res=(a%d)*(b%d)*(c%d)
			print("Resultado="+str(res))
	else:
		print("El valor ingresado no es válido.")
pass
modulo()
