#Escribe una función que reciba una lista de 6 números enteros ingresados por
#teclado e imprima cuales son pares, impares y a su vez si son primos o no.
pares = 0

for i in range(1,6):
          numero = int(input(f"Escriba el valor {i}: "))
          if numero % 2 == 0:
              pares =pares + 1
          else:
              print("Es primo")
          
              
print(f"Ha escrito {pares} números pares y {6 - pares} números impares.")

