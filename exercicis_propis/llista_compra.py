# Llista on hi guardarem els elements de la llista de la compra
llista = []

# Volem que s'executi constantment el programa
while True:

    # Menú
    print("\n1. Afegir producte")
    print("2. Eliminar producte")
    print("3. Mostrar llista")
    print("4. Sortir")
    
    # Indicar l'opció escollida
    opcio = input("> ")

    # Condicional "if" per cada cas
    if opcio == "1":
        producte = input("Introdueix el producte a afegir: ")
        llista.append(producte) #afegir el producte a la llista
        print(f'"{producte}" afegit a la llista!')

    elif opcio == "2":
        producte = input("Introdueix el producte a eliminar: ")
        if producte in llista:# comprovar que l'element estigui a la llista de la compra
            llista.remove(producte) # eliminar el producte de la llista
            print(f'"{producte}" eliminat!')
        else:
            print(f'"{producte}" no és a la llista.')

    elif opcio == "3":
        if len(llista) == 0: # comprovar si la llista està buida
            print("La llista està buida.")
        else:
            print("Llista de compres:")
            for p in llista: # per mostrar la llista en forma de puntets
                print("-", p)

    elif opcio == "4": # sortir del programa
        print("Fins aviat!")
        break # trencar el while

    else: # si s'escull una opció que no contemplem
        print("Opció no vàlida. Torna-ho a provar.")

