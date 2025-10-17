## Definim les funcions que inclourà la calculadora

def sumar(a, b):
    return a + b
    
def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0: # comprovació de si es podrà fer el càlcul o no
        return "Error: no es pot dividir per zero."
    else:
        return a / b

def demanar_numeros():
    a = float(input("Introdueix el primer número: "))
    b = float(input("Introdueix el segon número: "))
    return a, b

while True:
	print("\nCalculadora")
	print("1. Sumar")
	print("2. Restar")
	print("3. Multiplicar")
	print("4. Dividir")
	print("5. Sortir")
	opcio = input("> ")

	if opcio == "5": # parem el programa
		print("Adéu!")
		break
	else: # farem un càlcul
		a, b = demanar_numeros() # demanem els números	
		if opcio == "1": # operem en funció de l'opció escollida
			print("Resultat:", sumar(a, b))

		elif opcio == "2":
			print("Resultat:", restar(a, b))

		elif opcio == "3":
			print("Resultat:", multiplicar(a, b))

		elif opcio == "4":
			print("Resultat:", dividir(a, b))

		else:
			print("Opció no vàlida.")

