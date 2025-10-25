
def eliminar_triplets(ltriplets):

	# Llista amb els triplets filtrats
	llista_tuples = []
	llista_descartades = [] # llista on hi desem les tuples descartades
	
	# Aquests "for" ens permeten agafar un element de la llista i mirar els que venen després
	# D'aquesta manera ens assegurem de no avaluar dues vegades dues tuples
	for index1 in range(len(ltriplets)):
		tupla1 = ltriplets[index1] # triem una de les tuples
		for index2 in range(len(ltriplets)):
			tupla2 = ltriplets[index2] # triem una altra tupla per comparar

			# si un és múltiple de l'altre, si en fem la divisió sortirà el mateix nombre per cada element de la tupla
			frac0 = tupla1[0] / tupla2[0]
			frac1 = tupla1[1] / tupla2[1]
			frac2 = tupla1[2] / tupla2[2]
	
			if frac0 == frac1 and frac0 == frac2: # si una tupla és múltiple de l'altra
				# Trobem la tupla original i la desem a tupla0 (la que no és múltiple de l'altra)
				if frac0 > 1:
					tupla0 = tupla2 # tupla original
					tupla_multiple = tupla1 # tupla que és múltiple de tupla0
					llista_descartades.append(tupla_multiple) # desem la tupla múltiple per saber quina NO hem d'afegir a la llista final
				elif frac0 < 1:
					tupla0 = tupla1 
					tupla_multiple = tupla2
					llista_descartades.append(tupla_multiple)
				elif frac0 == 1:
					continue # estem avaluant una tupla amb ella mateixa
			else: # si no hi ha cap relació entre les tuples
				tupla0 = tupla2 # desarem la segona tupla, ja que la primera la seguim comprovant en aquest "for"
				
			# Desem la tupla original si no l'hem desada abans. També comprovem que aquesta tupla0 no hagi estat abans comprovada de ser un múltiple d'una altra tupla
			if (tupla0 not in llista_tuples) and (tupla0 not in llista_descartades):
				llista_tuples.append(tupla0)

	return llista_tuples # tornem la llista de tuples


def buscar_triplets(limit, exponent=2):
	# creem la llista on hi guardarem les tuples
	llista_tuples = [] 
	
	for c in range(limit): # correm per tots els possibles valors c<limit (cal posar el +1 pel funcionament d'índexs en Python
		for b in range(c): # correm per tots els possible valors b<c
			
			# calculem a que satisfà la condició
			a = (c**exponent - b**exponent)**(1./exponent)
		
			if a < b: # comprovem que a<b (podria no ser-ho per qüestions matemàtiques)
				if a.is_integer() == True: # comprovem que "a" es pot expressar com a nombre natural (condició buscada a internet)
					# definim la tupla que volem desar		
					tupla = (int(a),b,c)
					
					# afegim la tupla a la llsita de resultats
					llista_tuples.append(tupla)

	return llista_tuples # tornem la llista de tuples

# Apartat a
triplets = [(1, 2, 3), (2, 3, 4), (2, 4, 6), (6, 9, 12), (3, 6, 9)]
llista_filtrada = eliminar_triplets(triplets)
print(llista_filtrada)

# Apartat b
# Aprofitem la funció a.is_integer() que hem utilitzat a l'exercici 1. Primer passem l'input a float (si es pot) i després mirem si és int
lim = input("Introdueix el límit: ")
exp = input("Introdueix l'exponent: ")

# Farem un try-except per veure si es pot convertir en float, primerament
try:
	# Convertim a float
	lim = float(lim)
	exp = float(exp)
	
	# Mirem si el float es pot escriure com un int. Si és així, seguim endavant. Sinó, fem saltar l'error
	if lim.is_integer():
		lim = int(lim) # passem a int per poder executar buscar_triplets() i seguir amb el codi
	else:
		raise ValueError("El valor que has introduït no es pot convertir a enter") # fem saltar l'error
	if exp.is_integer(): # igual per exp
		exp = int(exp)
	else:
		raise ValueError("El valor que has introduït no es pot convertir a enter")

except: # aquí hi entrem si "lim" o "exp" introduïts no es poden convertir a floats
	raise ValueError("El valor que has introduït no es pot convertir a enter")

triplets = buscar_triplets(lim, exp)
print("Triplets: ", triplets)

triplets_filtrats = eliminar_triplets(triplets)
print("Triplets filtrats: ", triplets_filtrats)


