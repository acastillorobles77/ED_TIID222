#!/usr/bin/env python3

# Declarando un arreglo (lista, por ser Python)
numeros = [10, 20, 30, 40, 50]

# Imprimimos el elemento en la posición 2 de la lista (30)
print(numeros[2])

# Reasignar el elemento en la posición 3
numeros[3] = 35

# Imprimimos la lista
print(numeros)

# O bien, podemos usar un bloque for también
for num in numeros:
    print(num)

# Añadimos otro elemento al final de la lista
numeros.append(60)
print(numeros)

# Eliminamos el 35 usando remove
numeros.remove(35)
print(numeros)

# Eliminamos el elemento en la posición 4, usamos pop cuando conocemos la posición del elemento
print(f"Se eliminará el {numeros.pop(4)} de la lista")
print(numeros)

# Creamos una lista de frutas
frutas = ["manzana", "fresa", "sandia", "mango", "melon", "platano"]

# Eliminamos el elemento en la posición 4 en la lista de frutas
print(f"Se eliminará {frutas.pop(4)}")
print(frutas)

# Eliminamos el primer elemento usando remove
frutas.remove("manzana")
print(frutas)

# Declaramos un arreglo vacío
arreglo = []

try:
    n = int(input("Ingrese el tamaño del arreglo: "))
    for i in range(n):
        dato = int(input(f"Escribe el valor a guardar en la posición {i+1}: "))
        arreglo.append(dato)
    print(arreglo)

    n = int(input("Ingrese el tamaño del arreglo: "))
    arreglo = [0] * n;
    for i in range(n):
        arreglo[i] = int(input(f"Escribe el valor a guardar en la posición {i+1}: "))
    print(arreglo)
except ValueError:
    print("Error: Número inválido")

