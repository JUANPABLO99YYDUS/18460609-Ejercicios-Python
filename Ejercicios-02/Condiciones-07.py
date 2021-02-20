#Escribe un programa que contenga una función que reciba los coeficientes de
#una ecuación de segundo grado (a x2 + b x + c = 0) y retorne la solución.
import math
x1=0
x2=0

a= int(input("Da el valor de A: "))
b= int(input("Da el valor de B: "))
c= int(input("Da el valor de C: "))

if ((b**2)-4*a*c) < 0:
  print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
  x2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)

