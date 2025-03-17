# Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números PARES

list = []
tuple = (50,45,20,30,40,87)

for number in tuple:
    if number % 2 == 0:
        list.append(number)

print(tuple)
print(list)

# Diccionario
dic = {
    "nombre": "Jose",
    "edad": 24,
    "Ocupación": "Programador"
}

print(dic.items())