#Escribe un programa que pida los coeficientes de una ecuación de primer grado
#(a x + b = 0) y escriba la solución.

a= int(input("Da el valor de A: "))
b= int(input("Da el valor de B: "))

if a== 0 and b!=0:
    print("Esta no tiene solución")
elif a==0 and b==0:
    print("Multiple solución")
else:
    incog= -b/a
    print("El valor de x es: %s" %str(incog))
