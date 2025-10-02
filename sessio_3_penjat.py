# Demanar paraula
paraula = input("Escriu la paraula amagada: ") # això és str

# Separem cada lletra
paraula_llista = list(paraula)

# Llista buida on hi ha les lletres trobades
lletres_trobades = []

# Llista buida on hi haurà les lletres intentades
lletres_intentades = []

# Paraula clau que ens indica si s'acaba el joc
victoria = False

# Comptador d'intents
intents = 0

# Córrer el programa sempre que no s'hagi endevinat la paraula sencera
while victoria == False:
	# Demanar una lletra nova
	nova_lletra = input("Escriu una lletra: ")
	
	# Comprovar si hi ha més d'una lletra a l'input
	if len(nova_lletra) > 1:
		print("Has de posar només una lletra. Torna-ho a provar")
		# Imprimim l'estat del joc
		for lletra in paraula: #AIXÒ ES POT POSAR COM UNA FUNCIÓ
			if lletra in lletres_trobades:
				encerts += 1
				print(lletra, end='')
			else:
				print("*", end='')
		print("\nIntents restants: ", 10-intents)
		print()
		
		continue
	
	# Comprovar si la lletra ja s'ha provat
	if nova_lletra in lletres_intentades:
		print("Ja has provat aquesta lletra. Prova'n una altra")
		
		# Imprimim l'estat del joc
		for lletra in paraula:
			if lletra in lletres_trobades:
				encerts += 1
				print(lletra, end='')
			else:
				print("*", end='')
		print("\nIntents restants: ", 10-intents)
		print()
		
		continue # torna a començar el while des del principi

	# Actualitzem el nombre d'intents
	intents += 1
	
	# Desar la nova lletra a la llista d'intents
	lletres_intentades.append(nova_lletra)
		
	# Comprovar si la lletra es troba a la paraula amagada
	if nova_lletra in paraula_llista:
		# Desem la nova lletra a la llista de lletres trobades
		lletres_trobades.append(nova_lletra)

	encerts = 0 # comptador d'encerts
	# Imprimim l'estat del joc (i fem el recompte d'encerts)
	for lletra in paraula:
		if lletra in lletres_trobades:
			encerts += 1
			print(lletra, end='')
		else:
			print("*", end='')
	print() # per afegir un salt a la terminal

	# Comprovem si s'ha acabat el joc
	if encerts == len(paraula):
		# S'han encertat totes les lletres		
		print("Has trobat la paraula amagada :)")
		print("Has necessitat ", intents, " intents.")
		print("La paraula amagada era: ", paraula)
		
		victoria = True # amb aquesta condició sortim del while
	else:
		print("Encara et falten ", len(paraula) - encerts, " lletres per trobar")

	print("\nIntents restants: ", 10-intents)
	
	# Sortim del joc si hem exhaurit el nombre d'intents
	if intents == 10:
		# Sortir
		print("Has exhaurit el nombre d'intents.")
		print("La paraula amagada era: ", paraula)
		break
		
print("Finalitzem el joc.")
		
			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
					
	
