# Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados

list = []

for c in range(0, 8):
    city = input(f"{c} Digite una ciudad: ")
    list.append(city)

print(f"Lista: {list}")
print(f"Inverso: {list[::-1]}")