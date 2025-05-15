# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

totalAcumulado = 0

while True:
    numero = int(input("Ingresa un número entero (0 para detener): "))
    if numero == 0:
        break
       
    totalAcumulado += numero

print(f"La suma total acumulada es: {totalAcumulado}")
