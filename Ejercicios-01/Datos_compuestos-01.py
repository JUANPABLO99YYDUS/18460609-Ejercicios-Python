#Realiza una función separar(lista) que tome una lista de números enteros
#desordenados y devuelva dos listas ordenadas. La primera con los números pares y la
#segunda con los números impares.
import random

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
num = [random.randint(0,1000) for _ in range(n)]
print(num)

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(num)
print("Lista completa: ", num)
print("Pares: ", pares)
print("Impares: ", impares)
