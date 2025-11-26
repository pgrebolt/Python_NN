
"""
EXAMEN PARCIAL 1
"""

# Exercici 2:

nom_estudiant = input("Escriu el nom d'un estudiant: ")


def demanar_nota(nota):
    print("La nota ha d'estar entre 0 i 10! Torna-la a escriure a continuació.")
    nota= float(input("Escriu una nota: ")) 

nota1= float(input("Escriu una nota: ")) 

if nota1 not in range(0,11):
    demanar_nota(nota1)
    
nota2= float(input("Escriu una nota: "))

if nota2 not in range(0,11):
    demanar_nota(nota2)

nota3= float(input("Escriu una nota: "))

if nota3 not in range(0,11):
    demanar_nota(nota3)

# estic convertint directament els inputs (que per defecte són ints) a floats, per tal que tinguin decimals

#fins aquí el que he fet és bàsicament fer una funció que cada vegada que la cridi, que serà cada vegada que la nota introduïda
# per l'usuari no estigui entre 0 i 10, que torni a demanar per pantalla una nota i l'assigni a la variable corresponent.


def calcul_nota(n1, n2, n3):
    mitjana= (n1+n2+n3)/3
    return mitjana
# he decidit fer una funció que hem calculi la nota mitjana amb l'operació indicada.

# ara, cridaré la funció i assignaré als paràmetres n1, n2 i n3 els valors floats que s'han escrit en l'input, d'aquesta 
# manera, es calcularà la nota i com la funció retorna la "mitjana", retornarà aquesta nota calculada.


nota_mitjana = calcul_nota(nota1, nota2, nota3)

nota_mitjana_2decimals = round(nota_mitjana, 2) #aqui indico que vull 2 decimals a la resposta

print(f"L'estudiant {nom_estudiant} té una mitjana de {nota_mitjana_2decimals}.")
# finalment faig el print amb totes les variables correctes.

print()

# Exercici 3:
#APARTAT A)
def calcula_mitjana(notes):
    suma_de_notes = sum(notes)
    # sumo totes les variables de la meva llista.
    nota_mitjana_ambdecimals = suma_de_notes/len(notes)
    nota_mitjana = round(nota_mitjana_ambdecimals, 2) #arrodoneixo a 2 decimals.
    #aqui divideixo la suma de totes les notes per la llargada de la llista per tal de fer la mitjana.
    return nota_mitjana
        
#fem la prova amb una llista que m'invento.

notes_meves = [9.6, 7.6, 3.5, 8.4]

resultat = calcula_mitjana(notes_meves)

print(f"El resultat de la meva llista de notes és una mitjana de {resultat}.")



print()
#APARTAT B) i exercici 5 a):

try:
    fitxer_notes = open('notes.txt', 'r') #aqui intentarà obrir el fitxer.
except Exception: #poso Exception ja que no sé quina excepció concreta em saltaria si no existís el fitxer.
    print("No s'ha pogut obrir el fitxer, ja que no existeix o no està guardat a la mateixa carpeta. El programa s'ha aturat.")
    quit() # aquesta funció serveix per aturar el programa si la excepció es compleix.
    

# si no es compleix la excepció, el programa segueix amb lo que hi ha a continuació, que és del 3b).
linies = fitxer_notes.readlines() # creo una llista on cada element és una linía del fitxer.
for linia in linies:
    print(linia)


fitxer_notes.close() #tanquem el fitxer quan el programa acabi..

# No sé ben bé com calcular la mitjana treballant amb el fitxer, així que el que faré serà escriure-ho manualment.
Anna_Alsina=[4.4, 1.4, 9.7]
Bernat_Bonjorn=[8.4, 5.6, 5.2]
Carla_Castell=[1.9, 3.6, 2.8]
David_Diaz=[3.6, 8.8, 1.1]
Emma_Estrada=[0.9, 9.7, 6.4]
Francesc_Figols=[9.4, 7.3, 3.4]
Gemma_Garcia=[9.9,9.2,8.5]
Hugo_Hernandez=[5.5,8.0,6.1]
Irene_Ingla=[5.8,7.7,8.1]
Joan_Jimenez=[1.3,1.4,6.2]

#crido la funció per calcular les mitjanes i ho guardo en noves variables
anna = calcula_mitjana(Anna_Alsina)
bernat= calcula_mitjana(Bernat_Bonjorn)
carla = calcula_mitjana(Carla_Castell)
david= calcula_mitjana(David_Diaz)
emma= calcula_mitjana(Emma_Estrada)
francesc= calcula_mitjana(Francesc_Figols)
gemma= calcula_mitjana(Gemma_Garcia)
hugo= calcula_mitjana(Hugo_Hernandez)
irene = calcula_mitjana(Irene_Ingla)
joan=calcula_mitjana(Joan_Jimenez)


print(f"Les mitjanes han quedat: {anna}, {bernat}, {carla}, {david}, {emma}, {francesc}, {gemma}, {hugo}, {irene} i {joan}.")



print()
#Exercici 4:

noms_i_notes = {"Anna_Alsina": anna, "Bernat_Bonjorn": bernat, "Carla_Castell": carla, "David_Diaz": david, "Emma_Estrada": emma,
                "Francesc_Figols": francesc, "Gemma_Garcia": gemma, "Hugo_Hernandez": hugo, "Irene_Ingla":irene, "Joan_Jimenez": joan}

# L'anterior diccionari té cada nom amb la seva respectiva nota mitjana que he calculat anteriorment i l'he assignat una variable.

# Ordre de menor a major mitjana:
llista=[]

for clau, valor in noms_i_notes.items():
    llista.append( (clau, valor) )

print(llista)

# ara ordeno de menor a major amb la següent funció:

llista_ordenada= llista.sort()

































