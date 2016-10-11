import math
def circulo():
	print("Bienvenido, ingrese el radio de un circulo para obtener el área, diámetro y la circunferencia.")
	r=float(input("Ingrese el valor de radio: "))
	area=math.pi*r*r
	diam=2*r
	circ=math.pi*diam
	print("Área="+str(area))
	print("Diámetro="+str(diam))
	print("Circunferencia="+str(circ))
pass
circulo()


