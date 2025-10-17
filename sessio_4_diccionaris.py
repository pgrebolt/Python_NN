noms = ['ordinador', 'mobil', 'USB']
preus_noms = [700, 400, 10]

print(noms[0], preus_noms[0])

preus = {'ordinador':700, 'mobil':400, 'USB':10}

print(preus['ordinador'], preus['mobil'])

print(preus.items())
for key, value in preus.items():
	print(f"El valor de {key} és de {value} euros.")	

