#Escriba un programa que pregunte cuántos números se van a introducir, pida
#esos números, y escriba el mayor, el menor y la media aritmética.

numero = int(input("¿Cuántos valores va a introducir? "))
valor = float(input("Escriba el número 1: "))
minimo = maximo = suma = valor
for i in range(2, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            suma = suma + valor
            if valor < minimo:
                minimo = valor
            if valor > maximo:
                maximo = valor
print(f"El número más pequeño es {minimo}")
print(f"El número más grande es {maximo}")
print(f"La media de los números introducidos es {suma / numero}")
