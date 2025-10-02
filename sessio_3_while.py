numero_secret = 9 # ha de ser int

check = False

while check == False:
	numero = int(input("Numero: "))
	
	if numero == numero_secret: # parell
		print("Has endevinat el número! Sortim del bucle")
		check = True
	else:
		print("Prova un altre número.")

print("Hem sortit del while")
