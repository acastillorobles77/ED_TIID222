#!/usr/bin/env python3

"""
numeros = [10, 20, 30, 40, 50]

print(numeros[2])

numeros[2] = 100

print(numeros)
"""
"""
numeros = [10, 20, 30, 40, 50]

numeros.append(60)

print(numeros)

print(numeros[5])
"""

"""
numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros[5][1])
"""

"""
numeros = [10, 20, 30, 40, 50]

numeros.append(60)
numeros.append(70)

print(numeros)
"""
"""
numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros[5][0])
"""
"""
numeros = [10, 20, 30, 40, 50]

numeros.insert(2, 25)

print(numeros)
"""
"""
numeros = [10, 20, 30, 40]
numeros += [50, 60, 70]
print(numeros)
"""
"""
numeros = [10, 20, 30]
otros_numeros = [40, 50, 60]
numeros.extend(otros_numeros)
print(numeros)
"""
numeros = [10, 20, 30]
numeros[len(numeros):] = [40]
print(numeros)
