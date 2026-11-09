#!/usr/bin/env python3

from collections import deque

cola = deque()
pila = []

def menu_colas():
    op = None
    while op != "4":
        print("Elige una opcion")
        print("1. Insertar en la cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
        op = input("Opción: ")
        match op:
            case "1":
                num = None
                try:
                    num = int(input("Escribe el número a guardar en la cola: "))
                    cola.append(num)
                    print("Número añadido a la cola.")
                except ValueError:
                    print("Número inválido.")
            case "2":
                print(f"Se ha quitado el primer elemento de la cola: {cola.popleft()}")
            case "3":
                print("Elementos guardados actualmente en la cola: ")
                for item in cola:
                    print(item)
                print()
            case "4":
                pass
            case _:
                print("Opción inválida, intentar de nuevo.")

def menu_pilas():
    op = None
    while op != "4":
        print("Elige una opción")
        print("1. Agregar a la pila")
        print("2. Eliminar de la pila")
        print("3. Listar pila")
        print("4. Salir")
        op = input("Opción: ")
        match op:
            case "1":
                num = None
                try:
                    num = int(input("Escribe el número a agregar en la pila: "))
                    pila.append(num)
                    print("Número añadido a la pila.")
                except ValueError:
                    print("Número inválido.")
            case "2":
                print(f"Se ha quitado el último elemento de la pila: {pila.pop()}")
            case "3":
                print("Elementos guardados actualmente en la pila: ")
                for item in pila:
                    print(item)
                print()
            case "4":
                pass
            case _:
                print("Opción inválida, intentar de nuevo.")

if __name__ == "__main__":
    op = None
    while op != "3":
        print("Elige una opción")
        print("1. Menú colas")
        print("2. Menú pilas")
        print("3. Salir")
        op = input("Opción: ")
        match op:
            case "1":
                menu_colas()
            case "2":
                menu_pilas()
            case "3":
                pass
            case _:
                print("Opción inválida, intentar de nuevo.")

