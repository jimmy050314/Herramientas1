def pys():
	print("Bienvenido, ingrese los 5 valores para obtener su sumatoria y promedio")
	V1=float(input("Ingrese el primer valor: "))
	V2=float(input("Ingrese el segundo valor: "))
	V3=float(input("Ingrese el tercer valor: "))
	V4=float(input("Ingrese el cuarto valor: "))
	V5=float(input("Ingrese el último valor: "))
	sum=V1+V2+V3+V4+V5
	prom=sum/5
	print("Sumatoria= "+str(sum))
	print("Promedio= "+str(prom))
pass

pys()
