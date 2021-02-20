#Escribe un programa que pregunte primero si se quiere calcular el área de un
#triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un
#triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura
#y escribir el área. Si se contesta que se quiere calcular el área de un círculo
#(escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

op = ""
while op != "3":
    print("1.Area de triangulo\n2.Area de circulo \n3.- Salir")
    op = input("Ingresa una opcion con t o T para triangulo o c o C para la del circulo o el 3 para salir: ")
    if(op == "t") or (op=="T"):
        print("Triangulo")
        print("Da la base")
        base=int(input())
        print("Da la altura")
        altura=int(input())
        res= base*altura
        print("El area es: ", res)
        
    elif(op=="c") or (op=="C"):
        print("Circulo")
        print("Da el radio")
        radio=float(input())
        al=3.141592*(radio**2)
        print("El area es: ", al)
else:
    print("Has Salido")
