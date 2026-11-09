#!/usr/bin/env python3

# Generamos la clase del Nodo
class Nodo:
    def __init__(self, numero):
        # Estructura de un nodo [numero][referencia]
        self.numero = numero
        self.siguiente = None # siguiente nodo de la lista

# Aquí generamos tal cual la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza=None # Por defecto, la cabeza estará vacía

    def InsertarAlInicio(self, numero):
        nuevo_nodo = Nodo(numero) # generamos un nodo nuevo
        if (self.cabeza == None): # si la cabeza está vacía,
            self.cabeza=nuevo_nodo # hacemos entonces que la cabeza de la lista sea el nuevo nodo
            return # y aquí terminamos
        # Supongamos que la lista sí tenía una cabeza, entonces el siguiente nodo será la cabeza actual
        nuevo_nodo.siguiente=self.cabeza
        # Y entonces hacemos que la cabeza de la lista sea el nuevo nodo
        self.cabeza = nuevo_nodo

    # Usamos esta función para insertar un nodo al final de la lista
    def InsertarAlFinal(self, numero):
        # Generamos otro nodo
        nuevo_nodo=Nodo(numero)
        # Comprobamos si la lista está vacía
        if(self.cabeza == None):
            # Si la cabeza está vacía, el nodo será el primero (cabeza)
            self.cabeza=nuevo_nodo
            return
        # Creamos una referencia temporal al primer nodo (la cabeza)
        actual=self.cabeza
        #Cambiamos referncias de manera secuancial al agregar un nodo

        #avanzas mientras exista un nodo siguiente actual.siguiente
        while actual.siguiente: # Repetimos el bucle hasta llegar al final de la lista (es decir, hasta que siguiente sea None, entonces el bucle se rompe)
            # Mientras el bucle se repita, avanzar al siguiete nodo
            actual=actual.siguiente
        # Y cuando el bucle se termina (siguiente es None), entonces sabemos que ya llegamos al final de la lista, por lo cual tomamos el nodo nuevo y lo guardamos al final
        actual.siguiente=nuevo_nodo
    
    # Usamos esta función para imprimir cada uno de los elementos de la lista enlazada
    def ImprimirLista(self):
        # Guardamos el nodo actual (la cabeza)
        actual = self.cabeza
        # Mientras que el nodo actual no sea None (es decir, hay otro nodo más)
        while actual:
            print(actual.numero) # imprimimos el número que tiene guardado el nodo actual
            actual=actual.siguiente # y el siguiente pasa a ser el actual
        print("None")

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.InsertarAlInicio(2)
    lista.InsertarAlInicio(1)
    lista.InsertarAlFinal(3)
    lista.ImprimirLista()

