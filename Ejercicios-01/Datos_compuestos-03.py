#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
#mayor.

loteria= []

for i in range(6):
    loteria.append(int(input("Pon tu numero %s: "%(i+1))))
    if loteria[i]
    loteria.sort()

print ("El número ganador es: ", loteria)
