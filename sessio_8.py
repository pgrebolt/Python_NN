# Importem els paquets necessaris
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit # de scipy.optimize només importem una funció

def generar_tirades(mu_x=0, mu_y=0, sigma_x=1, sigma_y=1, N=1000):
	# Cridem np.random.normal per generar N valors aleatoris en cada coordenada seguint una distribució gaussiana amb la mitjana i desviació estàndard especificades.
	# Hem assignat valors per defecte a cada paràmetre
	valors_x = np.random.normal(loc = mu_x, scale = sigma_x, size = N)
	valors_y = np.random.normal(loc = mu_y, scale = sigma_y, size = N)

	# Generem la matriu de dues columnes amb els valors generats
	matriu_valors = np.vstack((valors_x, valors_y))
	
	# Retornem la matriu
	return matriu_valors

def funcio_gaussiana(x, a, b, c):
	# Aquesta funció defineix la funció gaussiana
	return a * np.exp(-(x-b)**2/(2*c**2))

def ajust_gaussia(x, y):
	# Fem l'ajustament amb curve_fit
	parametres, covarianca = curve_fit(funcio_gaussiana, x, y)
	
	# Extraiem els paràmetres. Tenim 3 paràmetres perquè funcio_gaussiana té 3 paràmetres (a,b,c)
	return parametres[0], parametres[1], parametres[2]
	
	
# Generem les coordenades. Si no especifiquem cap valor, es prendran els valors per defecte
# La variable 'valors' és una matriu
valors = generar_tirades(N=1000)

## Pintem els punts amb un scatter plot. Cal seleccionar els punts x i y de dins la matriu
plt.figure(1) # definim que treballarem amb la figura 1 a partir d'ara
plt.scatter(valors[0,:], valors[1,:])

#Afegim els noms de les coordenades
plt.xlabel('Coordenada x')
plt.ylabel('Coordenada y')

# Desem la imatge
#plt.show()
#plt.savefig('scatter_plot.png')

## Pintem els punts amb un histograma
plt.figure(2) # definim que treballarem amb la figura 2 a partir d'ara
histx = plt.hist(valors[0,:], histtype='step', label = 'Valors x') # pintem l'histograma. També desem la sortida en variables. Posem histtype='step' per poder observar histogrames sobreposats
histy = plt.hist(valors[1,:], histtype='step', label = 'Valors y')

plt.legend() # llegenda
plt.xlabel('Valor')
plt.ylabel('Freqüència')

# Desem la imatge
#plt.show()
#plt.savefig('histogram.png')


## Ajustament a funció gaussiana (per escurçar el codi ho fem només amb la coodenada x, però per la y seria fer el mateix)
# Les variables histx contenen l'alçada de cada barra de l'histograma (coordenada 0) i també la posició dels 'edges' de les barres

# Calculem la posició central de les barres
bar_edges_x = histx[1]
bar_centers_x = [bar_edges_x[i] + (bar_edges_x[i+1] - bar_edges_x[i])/2 for i in range(len(bar_edges_x)-1)]
# Hem fet servir una llista incloent un for. Haguéssim pogut fer un 'for' més 'convencional': crear una llista buida i a cada iteració del loop afegir el valor a la llista. D'aquesta manera ho hem fet tot compacte

# Extraiem els valors de l'ajustament. Els valors x són bar_centers_x i els valors y seran les alçades de les barres de l'histograma
scale, mu, sigma = ajust_gaussia(bar_centers_x, histx[0])


## Representem l'histograma novament, ara amb l'ajustament
# Valors de l'eix x que farem servir per representar la funció ajustada
sample_x = np.linspace(-3, 3, 100)

# Valors y de la funció ajustada són, precisament, la funció ajustada. Li passem els paràmetres obtinguts amb curve_fit
valors_ajustats_y = funcio_gaussiana(sample_x, scale, mu, sigma)

# Gràfic
plt.figure(3)
plt.hist(valors[0, :])
plt.plot(sample_x, valors_ajustats_y)
plt.xlabel('Coordenada x')
plt.ylabel('Freqüència')
plt.show()

