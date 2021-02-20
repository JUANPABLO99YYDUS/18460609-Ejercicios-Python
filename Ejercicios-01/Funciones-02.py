#Realiza una función llamada area_circulo(radio) que devuelva el área de un
#círculo a partir de un radio. Calcula el área de un círculo de 5 de radio.

print("Da el radio")
radio=float(input())

def area_circulo(radio):
    return 3.141592*(radio**2)

print( area_circulo(radio) )
