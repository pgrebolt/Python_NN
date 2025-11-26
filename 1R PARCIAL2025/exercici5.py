def calcula_mitjana(notes):
    suma_de_notes = sum(notes)
    # sumo totes les variables de la meva llista.
    nota_mitjana_ambdecimals = suma_de_notes/len(notes)
    nota_mitjana = round(nota_mitjana_ambdecimals, 2) #arrodoneixo a 2 decimals.
    #aqui divideixo la suma de totes les notes per la llargada de la llista per tal de fer la mitjana.
    return nota_mitjana
   
# Obrim el fitxer amb les notes
try:
	notes_file = open('notes.txt', 'r') # read
except FileNotFoundError:
	print('No he trobat el fitxer. Parem el programa.')
	quit()

linies = notes_file.readlines() # llegim cada línia

for linia in linies: # accedim al contingut de cada línia
	elements = linia.split(';') # separem cada element per cada ;
	#print(linia, elements)
	notes = []
	print(elements, elements[1:])
	for el in elements[1:]:
		if (el == '\n') or (el == ''):
			print("No hi ha nota desada per a " + elements[0])
		else:
			notes.append(float(el))
	print(notes)
	mitjana = calcula_mitjana(notes) # calculem la mitjana amb la funció
	

notes_file.close() # tanquem el fitxer


