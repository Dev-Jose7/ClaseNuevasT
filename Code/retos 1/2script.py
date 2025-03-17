# Recibir un numero en teclado y determinar si este es múltiplo de 3

number = int(input("Ingrese un número: "))

if number % 3 == 0:
    print(f"{number} es multiplo de 3")
else:
    print(f"{number} no es multiplo de 3")