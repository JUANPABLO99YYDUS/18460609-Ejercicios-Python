#Escriba un programa que pregunte cuántos números se van a introducir, pida
#esos números y escriba cuántos negativos ha introducido.
cont=0
n= int (input("Cuantos valores vas a agregar: "))
for i in range(1,n+1):
    valor=int(input("Da el valor %s: " %(i)))
    if valor<0:
        cont=cont+1

if cont==0:
     print("No hay negativos")
else:
     print("Hay: ",cont ,"numeros negativos")
    
