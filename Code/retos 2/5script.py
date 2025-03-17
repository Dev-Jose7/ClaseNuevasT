# Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40

list = []
tuple = (50,45,20,30,40,87)

for number in tuple:
    if number > 40:
        list.append(number)

print(tuple)
print(list)
