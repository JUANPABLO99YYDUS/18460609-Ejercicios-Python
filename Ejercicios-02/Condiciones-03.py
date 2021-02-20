#Escribe un programa que pida dos números y que conteste cuál es el menor y
#cuál el mayor o que escriba que son iguales.

n1= int(input("Da el primer numero: "))
n2= int(input("Da el segundo numero: "))

if n1>n2:
    print("Mayor: ",n1, "Menor: ", n2)
elif n1<n2:
     print("Mayor: ",n2, "Menor: ", n1)
else:
    print("Los dos son iguales")
