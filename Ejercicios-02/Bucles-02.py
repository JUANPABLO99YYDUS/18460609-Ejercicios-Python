#Escriba un programa que pida un número entero mayor que cero y que escriba
#sus divisores.

num= int(input("Pon un numero entero mayor que 0: "))
if num<=0:
    print("No se puede sacar por que el numero es menor o igual a 0")
else:
        print(f"Los divisores de:", num, "son: ", end=" ")
        for i in range(1,num+1):
            if num%i==0:
                print(i,end=" ")
