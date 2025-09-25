temperatures = [25, 25.5, 26.2, 24.8, 20]
temperatures_dobles = []

print(1%2, 2%2, 3%2)

for numero in range(5):
	print(2*numero)

for temperatura in temperatures:
	nova_temperatura = temperatura*2
	temperatures_dobles.append(nova_temperatura)

print(temperatures)
print(temperatures_dobles)

# Bucles dobles (nested)
for i in range(5):
	for j in range(3):
		print(i, j)
	print("S'acaba j")
	
# Combinar for i if
# Volem treure els valors parells
for valor in range(10):
	# % indica residu de la divisió. Mirem si el residu és 0 per confirmar que és un nombre parell
	if valor % 2 == 0:
		print(valor)
		
	if valor == 4:
		print("Hem arribat al 4")
	
print("")	
# if, elif, else
llista = [3, 4., 'hola', 6, True]
for element in llista:
	if type(element) == int:
		print("int: ", element)
	elif type(element) == float:
		print("float: ", element)
	elif type(element) == str:
		print("string: ", element) 
	else:
		print("No és cap dels esmentats.")
	
	print("Següent element")
		
		
		
		
		
		
		
		
		
		
		
		
		
		

