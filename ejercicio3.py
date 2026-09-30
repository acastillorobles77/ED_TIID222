#!/usr/bin/env python3

# Arreglo inicial
numeros = [10, 20, 30, 40]

# Modificamos la lista
numeros.insert(2, 95)
numeros.extend([50, 67])

# Imprimir el arreglo completo
print(numeros)

# Imprimir el 95 y 67
for i in range(0, len(numeros)):
    if numeros[i] == 95 or numeros[i] == 67:
        print(f"El {numeros[i]} ocupa la posición {i}.")
