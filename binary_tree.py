#!/usr/bin/env python3

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def setleft(self, data):
        if self.left is None:
            self.left = TreeNode(data)
        else:
            self.left.data = data
        self.left.parent = self

    def setright(self, data):
        if self.right is None:
            self.right = TreeNode(data)
        else:
            self.right.data = data
        self.right.parent = self

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.data))
        print_tree(node.left, level + 1, "Left: ")
        print_tree(node.right, level + 1, "Right: ")

if __name__ == '__main__':

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(8)
    root.left.right.left = TreeNode(9)

    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(10)
    root.right.right.right.left = TreeNode(11)
    root.right.right.right.right = TreeNode(12)


    # Imprimir árbol
    # print_tree(root)

    root = TreeNode(input("Escribe qué habrá en la raiz: "))
    current = root
    while True:
        print("---- Mostrando nodo actual ----")
        print_tree(current)
        print("\nElige una opción:")
        print("1. Imprimir árbol completo")
        print("2. Agregar hijo a la izquierda")
        print("3. Agregar hijo a la derecha")
        print("4. Regresar al padre del nodo actual")
        print("5. Salir")
        op = input("Opción:")
        match op:
            case "1":
                print("---- Mostrando árbol completo ----")
                print_tree(root)
            case "2":
                datos = input("Escribe lo que se guardará en el nodo izquierdo: ")
                current.setleft(datos)
                current = current.getleft()
            case "3":
                datos = input("Escribe lo que se guardará en el nodo derecho: ")
                current.setright(datos)
                current = current.getright()
            case "4":
                print("Regresando al nodo padre. . .")
                if current.parent is not None:
                    current = current.parent
            case "5":
                break
            case _:
                print("Opción inválida")


