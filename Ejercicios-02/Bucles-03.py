#Escribe una función que reciba una lista de 6 números enteros ingresados por
#teclado e imprima cuales son pares, impares y a su vez si son primos o no.

n= int (input("Cuantos valores vas a agregar: "))
n1=int(input("Da el numero a comparar: "))
for i in range(n-1):
    valor=int(input(f"Escriba un número más grande que {n1}: "))
    if valor<n1:
        print(valor, "no es mayor que", n1)
             
     
     
