import numpy as np

llista = [1, 2, 5]
llista2 = [4, 3, 8]
vector = np.array([1 ,2 ,5]) # vector 1x3
vector2 = np.array(llista2)

matriu = np.array([[3,4,2], [2, 6, 9]]) # matriu 2x3

matriu_multi = np.array([[[3, 4, 5], [4, 6, 5]], [[3, 1, 2], [9, 0, 7]]])

print(llista*2)
print(vector*2)

print(llista + llista2)
print(vector + vector2)


# Llargada
print(vector.shape)
print(matriu.shape)
print(matriu_multi.shape)

# Accedir a elements
print(vector[0])
print(vector[:2])
print(matriu[0, 0]) # [fila, columna]
print(matriu[1, 0])
print(matriu[0, :])
print(matriu[:, 2])

###
# Generar números
random_number = np.random.rand(5) # números aleatoris entre 0 i 1
print(random_number)
linear_space = np.linspace(1, 10, 30)
print(linear_space)
arange = np.arange(1, 10)
print(arange)

