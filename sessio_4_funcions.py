# Definim les funcions
def calcul_hipotenusa(a, b):
	h = (a**2 + b**2)**(1./2.)
	print('funcio', a)
	return h
	
def demanar_catets():
	a = float(input("Catet 1: "))
	b = float(input("Catet 2: "))
	
	return a, b

### Codi principal
for i in range(3):
	c1, c2 = demanar_catets()

	hipo = calcul_hipotenusa(c1, c2)

	print(calcul_hipotenusa(c1, c2))

