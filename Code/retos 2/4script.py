# Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso

list = []
isList = False
counter = int(input("Digite la cantidad de números ha agregar: ")) # Opcional, se puede indicar el número 20 en esta variable

while counter > 0:
    number = int(input("Digite un numero: "))
    list.append(number)
    counter-=1
    print(f"{list}\n")

while True:
    print(f"Lista: {list}\n")
    search = int(input("Digite un número para consultarlo en la lista: "))

    # 1 Forma
    for number in list:
        if number == search:
            isList = True
            break

    # 2 Forma
    isList = search in list

    if isList:
        print("Número encontrado, pertenece a la lista")
    else:
        print("El número indicado no pertenece a la lista")
