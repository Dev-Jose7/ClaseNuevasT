# Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7


list = []
size = int(input("Indique el tamaño que tendra la lista: "))
counter = 0

#1 Forma
while size > 0:
    if counter % 7 == 0:
        list.append(counter)
        size-=1

    counter+=1

print(f"Forma #1: {list}")

#2 Forma Range genera un rango de valores iterables, estableciendo un inicio, final y pasos
for number in range(0, size, 7):
    list.append(number)

print(f"Forma #2: {list}")
