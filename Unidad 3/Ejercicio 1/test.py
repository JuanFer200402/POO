from gestor_edificios import Edificios
def test():
	edificios=Edificios()
	edificios.cargar()
	bandera=True
	while bandera:
		print("")
		print("----------Menu de opciones------")
		print("a) Mostrar propietarios de los departamentos de un edificio.")
		print("b) Mostrar la superficie total cubierta de un edificio.")
		print("c) Mostrar el porcentaje de superifice ocupado por un propietario.")
		print("d) Mediante un numero de piso mostrar la cantidad de deptos con 3 dormitorios y mas de un sanitario.")
		print("x) Salir del menu.")
		print("")
		opcion=input("Seleccione una opcion: ")
		opcion=opcion.lower()
		print("")
		if(opcion=='a'):
			nombre_edificio=input("Ingrese el nombre del edificio: ")
			if edificios.inciso_a(nombre_edificio)==1:
				print("Operacion realizada")
		elif(opcion=='b'):
			Id_ingresado=int(input("Ingrese el ID del edificio: "))
			if edificios.inciso_b(Id_ingresado)==-1:
				print("Algo fallo.")
		elif(opcion=='c'):
			nombre_propietario=input("Ingrese el nombre del propietario: ")
			if edificios.inciso_c(nombre_propietario)==-1:
				print("Algo fallo.")
		elif(opcion=='d'):
			piso_ingresado=int(input("Ingrese un numero de piso: "))
			cantidad=edificios.inciso_d(piso_ingresado)
			print(f"La cantidad de deptos que cumplen con el requisito son {cantidad}")
		elif(opcion=='x'):
			bandera=False
			print("Adios!")
		else: print("Seleccione una opcion valida.")

if __name__ == '__main__':
	test()