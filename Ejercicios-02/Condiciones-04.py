#Escribe un programa que pida dos números enteros y que escriba si el mayor es
#múltiplo del menor.


n1= int(input("Da el primer numero: "))
n2= int(input("Da el segundo numero: "))

if n1>n2:
	multi=n1%n2
	if multi==0:
		print("Mayor: ",n1, "Menor: ", n2, "y es multiplo")
	else:
		print("Mayor: ",n1, "Menor: ", n2, "y no es multiplo")
elif n1<n2:
	multi=n2%n1
	if multi==0:
		print("Mayor: ",n2, "Menor: ", n1, "y es multiplo")
	else:
		print("Mayor: ",n2, "Menor: ", n1, "y no es multiplo")
else:
	print("Los numeros son iguales") 
