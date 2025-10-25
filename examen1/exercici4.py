# Funció per comprovar que un nombre és primer
def es_primer(n):  # funció extreta de https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/
    if n < 1: # nombres més petits que 1 no són primers
        return False # aquí s'acaba la funció, que retorna False
    elif n == 1: # 1 és primer
        return True
    else: # comprovem qualsevol altre nombre
        is_prime = True  # Flag variable
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: # si n és divisible entre i
                is_prime = False # n ja no és primer
                break
    return is_prime


# Funció per comprovar si un nombre és parell
def es_parell(n):
    if n % 2 == 0:  # s'ha de comprovar el mòdul, no la divisió sencera
        parell_bool = True
    else:
        parell_bool = False
    return parell_bool


# Creem un diccionari buit
propietats = {}

# Per cada valor de l'1 al 100, afegim una clau i un valor (que serà una llista)
for value in range(100):
    # Llista de les propietats (es sobreescriu per cada value)
    llista_props = []

    # Mirem si el nombre és parell i/o primer
    parell = es_parell(value)
    primer = es_primer(value)

    # Afegim elements a la llista segons els resultats
    if parell == True:
        llista_props.append('parell')
    elif parell == False:
        llista_props.append('senar')
        
    if primer == True:
        llista_props.append('primer')
        
    # Afegim la clau i el valor (llista) al diccionari
    propietats[value] = llista_props

print(propietats[1])
print(propietats[4])

