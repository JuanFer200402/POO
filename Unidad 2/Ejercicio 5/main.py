from GestordeEquipo import GestorEquipo
from GestordeFecha import GestorFecha

if __name__ == '__main__':
	Equipo=GestorEquipo()
	Fecha=GestorFecha()

	while True:
		print("__Menu de Opciones__")
		print("[a]-Cargar los equipos del archivo")
		print("[b]-Cargar las fechas del archivo")
		print("[c]-Actualizar")
		print("[d]-Ingrese el nombre para obtener una lista del equipo")
		print("[e]- Ordenar")
		print("[f]- Guardar tabla ordenada en un archivo csv")

		opcion=input("Ingrese una opcion: ")
		if opcion=="a":
			Equipo.cargararchivoEquipo()

		elif opcion=="b":
			Fecha.cargararchivoFecha()

		elif opcion=="c":
			Equipo.actualizar(Fecha)

		elif opcion =="d":
			equipo1= input("Ingrese el nombre de un equipo: ")
			Equipo.verificarequipo(equipo1, Fecha)
		elif opcion == "e":
			Equipo.ordenar()

		elif opcion=="f":
			Equipo.almacenartabla()



				

