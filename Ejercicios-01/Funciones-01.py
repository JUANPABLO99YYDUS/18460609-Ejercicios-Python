#1.Realiza una función llamada area_rectangulo(base, altura) que devuelva el área
#del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de
#15 de base y 10 de altura.

print("Da la base")
base=int(input())
print("Da la altura")
altura=int(input())

def a_rectangulo(base, altura):
    return base*altura

print(a_rectangulo(base,altura) )
