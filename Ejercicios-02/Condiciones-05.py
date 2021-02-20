#Escribe un programa que pida tres números y que escriba si son los tres iguales,
#si hay dos iguales o si son los tres distintos.

n1= int(input("Da el primer numero: "))
n2= int(input("Da el segundo numero: "))
n3= int(input("Da el tercer numero: "))

if n1==n2 and n2==n3 and n3==n1:
    print("Los tres son iguales")
elif n1==n2 or n1==3 or n2==n3:
    print("Dos son iguales")
else:
    print("Los tres son diferentes")
