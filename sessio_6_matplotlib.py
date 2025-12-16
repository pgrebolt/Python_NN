import numpy as np
import matplotlib.pyplot as plt

# Generar números
x = np.linspace(-10, 10, 5) # valors x

# Calculem els quadrats
y = x **2

# Dibuixem amb línies
#plt.plot(x, y, label='Dades', color='red', linestyle='--', linewidth = 3)

# Dibuixem amb punts
plt.scatter(x, y, label ='Dades punts', color='green', s=200)

# Afegim llegenda
plt.legend()

# Afegim noms dels eixos
plt.xlabel('X')
plt.ylabel('X**2', fontsize = 20)



#plt.savefig('figura.png')
plt.show()

