# Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario

list = []
size = int(input("Indique el tamaño que tendra la lista: "))

# Forma 1
while size > 0:
    number = int(input("Indique un número: "))
    list.append(number)
    size-=1

print(f"Forma #1: {list}")

# Forma 2
for n in range(0, size):
    number = int(input("Indique un número: "))
    list.append(number)

print(f"Forma #2: {list}")