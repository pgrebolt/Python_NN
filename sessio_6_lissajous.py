# Importem els paquets
import numpy as np
import matplotlib.pyplot as plt

# Definim les funcions que retornen x i y
def posicio_x(t, wx = 2, A=1):
	# Aquesta funció calcula la posició en l'eix x per cada valor de temps
	# Hem definit wx=2, A=1 com a paràmetres per defecte, però es pot canviar quan es cridi la funció
	
	x = A * np.sin(wx*t)
	
	return x
	
def posicio_y(t, wy = 2, B=1, delta = np.pi/2):
# Aquesta funció calcula la posició en l'eix x per cada valor de temps
	# Hem definit wy=2, B=1, delta = pi/2 com a paràmetres per defecte, però es pot canviar quan es cridi la funció
	
	y = B*np.sin(wy*t + delta)
	
	return y

# Generem els valors de temps (unitats: rad)
temps = np.linspace(0, 2*np.pi, 200) # baixar el número de punts perquè el codi vagi més ràpid (però els plots no queden tan bé)

# Per exemple, per calcular les posicions s'ha d'executar
# posicio_y(temps, wy = 5, B=1, delta=np.pi/2)

# Gràfic dels resultats. Ho farem amb subplots (https://www.geeksforgeeks.org/python/matplotlib-pyplot-subplots-in-python/)
fig, ax = plt.subplots(ncols=3, nrows=2, figsize = (6, 2)) # hem especificat la mida de la imatge 
# l'objecte 'ax' és una "matriu de figures". Podem accedir al subplot corresponent si especifiquem la seva posició amb [][]
fig.subplots_adjust(hspace=0, wspace=0) # treiem els espais entre subplots


ax[0][0].plot(posicio_x(temps, wx=2), posicio_y(temps, wy=5, delta=np.pi/2)) # primera fila, primera columna; plot
ax[0][0].set_title('delta = pi/2') # títol
ax[0][0].set_ylabel('wx=2, wy=5') # nom eix y

ax[0][1].plot(posicio_x(temps, wx=2), posicio_y(temps, wy=5, delta=np.pi/3)) # primera fila, segona columna
ax[0][1].set_title('delta = pi/3')
ax[0][1].set_yticks([]) # treiem els ticks a l'eix y

ax[0][2].plot(posicio_x(temps, wx=2), posicio_y(temps, wy=5, delta=np.pi/4)) # primera fila, tercera columna
ax[0][2].set_title('delta = pi/4')
ax[0][2].set_yticks([]) # treiem els ticks a l'eix y

ax[1][0].plot(posicio_x(temps, wx=3), posicio_y(temps, wy=7, delta=np.pi/2)) # segona fila, primera columna
ax[1][0].set_ylabel('wx=3, wy=7')

ax[1][1].plot(posicio_x(temps, wx=3), posicio_y(temps, wy=7, delta=np.pi/3)) # segona fila, segona columna
ax[1][1].set_yticks([]) # treiem els ticks a l'eix y

ax[1][2].plot(posicio_x(temps, wx=3), posicio_y(temps, wy=7, delta=np.pi/4)) # segona fila, tercera columna
ax[1][2].set_yticks([]) # treiem els ticks a l'eix y

#plt.savefig('figure_lissajous.png')
plt.show()

# tota aquesta secció de plots es pot intentar automatitzar amb un únic loop
