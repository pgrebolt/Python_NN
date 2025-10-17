## Definim les diferents funcions

# Afegir un estudiant al diccionari
def afegir_estudiant(estudiants):
    nom = input("Nom de l’estudiant: ")
    nota = float(input("Nota: "))
    estudiants[nom] = nota
    print(f"{nom} afegit/da amb nota {nota}!")

# Mostrar totes les notes
def mostrar_notes(estudiants):
    if not estudiants:
        print("No hi ha estudiants registrats.")
    else:
        print("Llista d’estudiants:")
        for nom, nota in estudiants.items():
            print(f"- {nom}: {nota}")

# Imprimir la mitjana
def mostrar_mitjana(estudiants):
    if not estudiants:
        print("No hi ha dades per calcular la mitjana.")
    else:
        mitjana = sum(estudiants.values()) / len(estudiants)
        print(f"Mitjana de la classe: {mitjana:.2f}")

estudiants = {}
while True:
	print("\n1. Afegir estudiant")
	print("2. Mostrar notes")
	print("3. Mostrar mitjana")
	print("4. Sortir")
	opcio = input("> ")

	if opcio == "1":
		afegir_estudiant(estudiants)
	elif opcio == "2":
		mostrar_notes(estudiants)
	elif opcio == "3":
		mostrar_mitjana(estudiants)
	elif opcio == "4":
		print("Fins aviat!")
		break
	else:
		print("Opció no vàlida.")

