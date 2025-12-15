## Carreguem els paquets necessaris ##
import random

## Definim les funcions necessàries ##
def init_joc():
	# Demanem quants jugadors participaran
	njugadors_funcio = int(input("Quants jugadors participaran? "))
	
	# Per cada jugador, en desem el nom
	noms_jugadors_funcio = []
	for n in range(njugadors_funcio):
		nom_jugador = input(f"Nom jugador {n+1}: ")
		noms_jugadors_funcio.append(nom_jugador)
	
	# Nombre de rondes
	nrondes_funcio = int(input("Quantes rondes voleu fer? "))
	
	return njugadors_funcio, noms_jugadors_funcio, nrondes_funcio

def recompte_gen(njugadors, noms_jugadors, nrondes):
	# Aquesta funció inicialitza la llista on hi desarem les puntuacions de cada jugador. Ha de ser una llista de llistes
	
	recompte_llista = [] # llista on hi desarem les puntuacions
	for ronda in range(nrondes): # per cada ronda
		puntuacions_ronda = [] # llista on hi desem les puntuacions de cada jugador en aquesta ronda
		for jugador in range(njugadors):
			
			# Triem el nom del jugador
			nom_jugador = noms_jugadors[jugador]
			
			# Fem que aposti
			puntuacio = aposta(nom_jugador)
			
			# Desem la puntuació i passem al següent jugador
			puntuacions_ronda.append(puntuacio) # afegim un 0 per cada jugador
			
		recompte_llista.append(puntuacions_ronda) # afegim a la llista de totes les puntuacions
		
	return recompte_llista
		
def tirada2daus(puntuacio_min=1, puntuacio_max=6):
	# Aquesta funció simula la tirada de dos daus. De cada tirada, pot sortir-ne un número en l'interval (puntuacio_min, puntuacio_max)
	
	# Per si l'usuari passés com a arguments uns floats, els passem a int. Si ja són int no passa res
	puntuacio_min = int(puntuacio_min)
	puntuacio_max = int(puntuacio_max)
	
	# Simulem el número que surt del primer dau
	dau1 = random.randint(puntuacio_min, puntuacio_max)

	# Simulem el número que surt del segon dau
	dau2 = random.randint(puntuacio_min, puntuacio_max)
	
	# Puntuació total
	punts = dau1 + dau2
	
	return punts
	
def aposta(nom_jugador):
	# Aquesta funció simula que es llencen daus i va sumant-ne les puntuacions. Si s'arriba a més de 21, s'ha perdut
	
	joc_actiu = True # si la puntuació és menor de 21
	
	puntuacio = 0 # puntuacio inicial
	
	print("\n----------")
	print(f"Aposta de {nom_jugador}")
	
	while joc_actiu:
		# Sumem els punts de llençar 2 daus
		puntuacio = puntuacio + tirada2daus()
	
		print(f"La teva puntuació actual és {puntuacio}")
		# Condicions
		if puntuacio > 21:
			print("Has perdut!")
			puntuacio = 0 # reescrivim la puntuació
			joc_actiu = False # sortim del joc
		elif puntuacio == 21:
			print("Has guanyat!")
			joc_actiu = False # sortim del joc
		else:
			tornar_a_jugar = input("\nVols tornar a tirar? (S/N) ")
			if tornar_a_jugar == 'S':
				continue # seguim el joc. Torna a començar el while
			elif tornar_a_jugar == 'N':
				joc_actiu = False # sortim del joc
				
	print(f"Puntuació final: {puntuacio}")
	
	return puntuacio
	
def pos_max(llista):
	
	# Trobem l'índex de la posició de l'element màxim de la llista (buscat a internet: https://www.geeksforgeeks.org/python/python-find-index-of-maximum-item-in-list/)
	res = max(llista)
	max_index = llista.index(res)
	
	return max_index
		
		
## Codi ##	

# Inicialitzem el joc
nombre_jugadors, noms_jugadors, nombre_rondes = init_joc()

# Joc
puntuacions = recompte_gen(nombre_jugadors, noms_jugadors, nombre_rondes)

# Resultats
comptador = 1
for ronda in puntuacions: 
	# Cada 'ronda' és una llista
	
	# Trobem la posició de l'element amb més valor de la llista
	index_guanyador = pos_max(ronda)
	
	# Trobem el nom del guanyador 
	nom_guanyador = noms_jugadors[index_guanyador]
	
	# Trobem els punts que ha fet el guanyador
	punts_guanyador = ronda[index_guanyador]
	
	# Imprimim el guanyador
	print(f"La ronda {comptador} l'ha guanyada {nom_guanyador} amb {punts_guanyador} punts.")
	
	comptador += 1 # incrementem el comptador de rondes
		
