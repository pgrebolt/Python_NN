def calcula_mitjana(notes):
    suma_de_notes = sum(notes)
    # sumo totes les variables de la meva llista.
    nota_mitjana_ambdecimals = suma_de_notes/len(notes)
    nota_mitjana = round(nota_mitjana_ambdecimals, 2) #arrodoneixo a 2 decimals.
    #aqui divideixo la suma de totes les notes per la llargada de la llista per tal de fer la mitjana.
    return nota_mitjana
   
# Creem un diccionari on hi guardarem les mitjanes
mitjanes = {}

# Obrim el fitxer amb les notes
notes_file = open('notes.txt', 'r') # read

linies = notes_file.readlines() # llegim cada línia

for linia in linies: # accedim al contingut de cada línia
	elements = linia.split(';') # separem cada element per cada ;
#	print(linia, elements)
	nom, nota1, nota2, nota3 = elements[0], float(elements[1]), float(elements[2]), float(elements[3]) # assignem elements a variables. Passem a float si cal
	notes = [nota1, nota2, nota3] # llista amb les notes per passar a la funció
	mitjana = calcula_mitjana(notes) # calculem la mitjana amb la funció
	#nom, nota1, nota2, nota3 = elements
	# nota1 = float(nota1)
	#print("Nom: ", nom) # imprimim resultats
	#print("Nota 1: ", nota1)
	#print("Nota 2: ", nota2)
	#print("Nota 3: ", nota3)
	#print("Mitjana: ", mitjana)
	#print('-')

	# Afegim al diccionari
	mitjanes[nom] = mitjana

notes_file.close() # tanquem el fitxer

print(mitjanes)

## Apartat b

# Llista buida
llista = []
for key, value in mitjanes.items():
	llista.append( (key, value) )

#def funcio(tup):
#	return tup[1]
	
llista_ordenada = sorted(llista, key=lambda tup: tup[1])
print(llista)
print(llista_ordenada)	
