# Paquet per poder generar números aleatoris
import random

# Generem el número aleatori
num_secret = random.randint(1, 10)

# Llista on hi desarem els números intentats
intents = []

print("Endevina el número (entre 1 i 10)!")

endevinat = False # condició pel while
while not endevinat:
    # Menú
    intent = int(input("Introdueix un número: ")) # passem l'input a int
    if intent in intents:
        print("Ja has provat aquest número. Prova'n un altre.")
        continue # per tornar al princippi del while
        
    # Afegim l'intent a la llista. Només arribem aquí si hem superat l'if anterior
    intents.append(intent) 

    # Imprimim un missatge o un altre en funció de si el número és més gran o més petit que el número secret
    if intent < num_secret:
        print("Massa baix!")
    elif intent > num_secret:
        print("Massa alt!")
    else:
        nombre_intents = len(intents) # nombre d'intents
        print(f"Correcte! Has encertat en {nombre_intents} intents.")

        print("Els teus intents:") # mostrar els números que s'han intentat
        for i in intents:
            print("-", i)
        endevinat = True # amb aquesta definició sortirem del while

print("Joc finalitzat!") # missatge per veure que hem sortit del while

