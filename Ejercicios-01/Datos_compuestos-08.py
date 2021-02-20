#Escribir una función dia_siguiente_t que dada una fecha expresada como la terna
#(Día, Mes, Año) (donde Día y Año son números enteros, y Mes es el texto Ene, Feb, ...,
#Dic, según corresponda) calcule el día siguiente al dado, en el mismo formato.

def valores():
	d = int(input ("Ingrese un dia del mes: "))
	m = input ("Ingrese un mes (enero a diciembre): ")
	a = int(input ("Ingrese un año: "))
	
	dia_siguiente = diaSiguiente (d, m, a)
	print (dia_siguiente)

def diaSiguiente(dia, mes, ano):
	de31 = ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre")
	de30 = ("abril", "junio", "septiembre", "noviembre")
	de28 = ("febrero", )
	
	
	if (mes == "diciembre") and (dia == 31):
		return (dia - 30), de31[0], (ano + 1)
	
	elif mes in de31 and dia == 31:
		return (dia - 30), mes, ano
	
	elif mes in de30 and dia == 30:
		return (dia - 29), mes, ano
	
	elif mes in de28 and dia == 28:
		return (dia - 27), "marzo", ano
	
	else:
		return (dia + 1), mes, ano
	
	
valores()
