# Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas

print("***Nómina***")
list = []
option = True
income = float(3500000)
sellIncome = float(1500000)

while option:
    employee = input("Digite el nombre del empleado: ")
    sells = int(input(f"Digite la cantidad licencia de software vendida del empleado {employee}: "))
    fee = float(input("Ingrese comisiones por deducción: "))

    total = income + (sellIncome * sells) - fee

    #list.append((employee, total)) # Se añade tuple a la lista
    list.append({"Empleado": employee, "Salario": total})  # Se añade diccionario a la lista
    print(f"Salario a pagar al empleado {employee} es de {total}")

    next = input("Presione cualquier tecla para agregar calcular otro salario o [N] para salir")
    if next == "N" or next == "n": option = False

print(list)

