def calcula_mitjana(notes):
    suma_de_notes = sum(notes)
    # sumo totes les variables de la meva llista.
    nota_mitjana_ambdecimals = suma_de_notes/len(notes)
    nota_mitjana = round(nota_mitjana_ambdecimals, 2) #arrodoneixo a 2 decimals.
    #aqui divideixo la suma de totes les notes per la llargada de la llista per tal de fer la mitjana.
    return nota_mitjana
   
# Obrim el fitxer amb les notes
notes_file = open('notes.txt', 'r') # read

# Creem el fitxer amb les notes + mitjana
notes_mitjana_file = open('notes_mitjana.txt', 'w') # write
notes_mitjana_file.write("Nom;Nota1;Nota2;Nota3;Mitjana\n")

linies = notes_file.readlines() # llegim cada línia

for linia in linies: # accedim al contingut de cada línia
	elements = linia.split(';') # separem cada element per cada ;
#	print(linia, elements)
	nom, nota1, nota2, nota3 = elements[0], float(elements[1]), float(elements[2]), float(elements[3]) # assignem elements a variables. Passem a float si cal
	notes = [nota1, nota2, nota3] # llista amb les notes per passar a la funció
	mitjana = calcula_mitjana(notes) # calculem la mitjana amb la funció
	#nom, nota1, nota2, nota3 = elements
	# nota1 = float(nota1)
	print("Nom: ", nom) # imprimim resultats
	print("Nota 1: ", nota1)
	print("Nota 2: ", nota2)
	print("Nota 3: ", nota3)
	print("Mitjana: ", mitjana)
	print('-')
	
	# Escrivim els resultats al fitxer
	linia_mitjana = nom + ";" + str(nota1) + ";" + str(nota2) + ";" + str(nota3) + ";" + str(mitjana) +"\n"
	print(linia_mitjana)
	notes_mitjana_file.write(linia_mitjana)
#	notes_mitjana_file.write(nom + ";" + str(nota1) + ";" + str(nota2) + ";" + str(nota3) + ";" + str(mitjana) +"\n")


notes_file.close() # tanquem el fitxer
notes_mitjana_file.close()
#print(linies)

## Afegim uns resultats manualment (segurament això aniria a un altre fitxer py)
notes_mitjana_file = open('notes_mitjana.txt', 'a') # append
notes_mitjana_file.write("Manel;4.0;4.0;4.0;4.0\n")
notes_mitjana_file.close()



