#!/usr/bin/env python3

arreglo = []
arreglo_original = []
for i in range(15):
    num = -1
    while num < 0 or num > 500:
        try:
            num = int(input(f"Escribe el número a guardar en la posición {i}: "))
        except ValueError:
            print("Número inválido, intentar de nuevo")
    arreglo_original.append(num)
    while num % 5 != 0: # mientras no sea divisible por 5
        num = num + 1
    arreglo.append(num)
print("El arreglo original es: ", arreglo_original)
print("El arreglo resultante es: ", arreglo)

