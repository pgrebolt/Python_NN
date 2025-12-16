# Importem els paquets
import numpy as np
import matplotlib.pyplot as plt

def posicio_x(t):
	# Aquesta funció calcula la posició en l'eix x per cada valor de temps
	x0 = 0
	v0x = 2 #m/s
	
	return x0 + v0x * t

def posicio_y(t):
	# Aquesta funció calcula la posició en l'eix y per cada valor de temps
	y0 = 5 # m
	v0y = 20 #m/s
	ay = -9.8 #m/s2
	
	# Calculem la posició
	y = y0 + v0y*t + 0.5*ay*t**2
	
	return y

# Generem els valors de temps (unitats: s)
temps = np.linspace(0, 4.5, 40)

# Calculem x i y
x = posicio_x(temps)
y = posicio_y(temps)

# Creem una matriu amb els resultats
resultats_xy = np.array([x, y])

# Gràfic dels resultats
plt.figure() # creem la figura
plt.plot(temps, resultats_xy[0,:]) # dibuixem la posició x
plt.plot(temps, resultats_xy[1,:]) #dibuixem la posició y
plt.ylim((0, 30)) # marquem els límits de l'eix y
#plt.savefig('figura.png') # desem la figura
#plt.show()
plt.clf() # per netejar l'objecte 'figura'

## Com que no són escales comparables, crearem una figura amb secondary axis (https://pythonguides.com/matplotlib-secondary-y-axis/)
fig, ax1 = plt.subplots()

# Plot de la posició y al primary y-axis
ax1.plot(temps, resultats_xy[1,:], color='blue', label='Posició y') # plot
ax1.set_ylabel('y (m)', color='blue') # etiqueta de l'eix y
ax1.set_ylim((0, 30)) # límit de l'eix y (la funció és diferent si fem servir plt o ax)
ax1.tick_params(axis='y', labelcolor='blue') # números de l'eix en color blau
ax1.set_xlabel('t (s)') # etiqueta de l'eix x

# Si volem marcar la posició del màxim amb línies verticals i horitzontals
x_max = - 20 / (2*(-9.8*0.5)) # de la fórmula d'una paràbola, el màxim es troba a x = -b/2a
y_max = posicio_y(x_max) # trobem la posició y quan x=x_max
ax1.hlines(y_max, 0, x_max, linestyle='--', color='gray', alpha = 0.6) # línia horitzontal
ax1.vlines(x_max, 0, y_max, linestyle='--', color='gray', alpha = 0.6) # línia vertical

# Plot de la posició x al secondary y-axis
ax2 = ax1.twinx()
ax2.plot(temps, resultats_xy[0,:], color='orange', label='Posició x')
ax2.set_ylabel('x (m)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

#plt.savefig('figura_secondaryaxis.png')
plt.show()

