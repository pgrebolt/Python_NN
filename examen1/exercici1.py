
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


resultat = buscar_triplets(12)

print(resultat)


lim, exp = 100, 2
print(f"\nEl resultat amb limit={lim} i exponent={exp} és {buscar_triplets(lim, exp)}")

lim, exp = 100, 3
print(f"\nEl resultat amb limit={lim} i exponent={exp} és {buscar_triplets(lim, exp)}")
