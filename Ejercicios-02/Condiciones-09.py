#Escribe un programa que pida una distancia en centímetros y que escriba esa
#distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).

valor = int(input("Escriba el valor a convertir en centímetros (CM): "))

m=valor*(1/100)
km=m*(1/1000)

print("Valor en centimetros(cm) : ",valor)
print("Valor en metros(m) :",m)
print("Valor en kilometros(km) :",km)
