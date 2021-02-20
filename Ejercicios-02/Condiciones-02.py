#Mejora el programa anterior haciendo que tenga en cuenta que no se puede
#dividir por cero.

dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if divisor == 0:
        print("Error no puede dividirse entre 0")
elif dividendo % divisor == 0:
        print(f"La división es exacta. Cociente: {dividendo // divisor}")
else:
        print(f"La división no es exacta. Cociente: {dividendo // divisor} "f" Resto: {dividendo % divisor}")
