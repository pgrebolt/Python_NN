# Alguns tipus de variables
string_prova = "Hola, com anem?"
enter = -6
real = 4.3
booleans = True

# Proves amb print
#print("Hola, com va?")
#print()
#print("Hola,\ncom va?\n")
#print("Va bé!")

# Prova amb input
edat = input("Quants anys tens? ")
print("Type de edat: ", type(edat))
int_edat = int(edat)
print("Type de int_edat: ", type(int_edat))
print("Tens ", int_edat, " anys.")
print(f"Tens {int_edat} anys.")

## Exercici 1
print("Benvingudes i benvinguts a la classe de problemes d'informàtica")
print("-------")
nom = input("Com et dius? ") # per defecte sempre és string
edat = input("Quants anys tens? ")
alcada = input("Quina és la teva alçada? ")
print(f"Et dius {nom}, tens {edat} anys i fas {alcada} m d'alçada.\nAdéu!")
