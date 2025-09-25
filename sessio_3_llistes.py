temperatures = [25, 25.5, 26.2, 24.8, 20]

print(temperatures)

# Per accedir als diferents elements
#print(temperatures[0])
#print(temperatures[-1])
#print(temperatures[-2], temperatures[3])

# Afegim una nova temperatura a la llista
temperatures.append(25.1)

print(temperatures)

# Si volem combinar dues llistes
temperatures2 = [24.9, 25.1, 29.0, 26]
temperatures_total = temperatures + temperatures2

print(temperatures_total, len(temperatures_total))

print(temperatures_total[-1], temperatures_total[len(temperatures_total)-1])
