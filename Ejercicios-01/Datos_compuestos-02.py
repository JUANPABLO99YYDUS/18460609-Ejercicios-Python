#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla.

n= int (input("Cuantos materias vas a agregar: "))
materia=[]
for i in range(n):
    materia.append(input("Materia %s: "%(i+1)))

print(materia)
