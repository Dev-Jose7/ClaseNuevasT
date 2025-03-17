# Recibir dos números y determinar cual es mayor
number1 = int(input("Digite el primer número: "))
number2 = int(input("Digite el segundo número: "))

if number1 > number2:
    print(f"El número {number1} es mayor que {number2}")
elif number2 > number1:
    print(f"El número {number2} es mayor que {number1}")