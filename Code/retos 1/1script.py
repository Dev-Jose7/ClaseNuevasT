# Recibir un numero en teclado y determinar si este es múltiplo de 5

number = int(input("Ingrese un número: "))

if number % 5 == 0:
    print(f"{number} es multiplo de 5")
else:
    print(f"{number} no es multiplo de 5")