from lista_publicaciones import Lista
from clase_audio_libro import Audio_Libro
from clase_libro import Libro
def menu():
	op=None
	try:
		op= int(input("""
			                            Menú de Opciones
            [1] Agregar una publicacion
            [2] Conocer tipo de publicacion a partir de su posicion
            [3] Mostrar cantidad de publicaciones de cada tipo
            [4] Mostrar datos de las publicaciones
            [0] SALIR
		Seleccione una opcion: """))
	except ValueError:
		pass
	return op

if __name__ == '__main__':
	lista=Lista()
	lista.cargar_archivo()
	opcion=menu()
	while opcion!=0:
		if opcion==1:
			tit=input("Ingrese el titulo de la publicacion: ")
			cat=input("Ingrese la categoria de la publicacion: ")
			precio_b=input("Ingrese el precio base de la publicacion: ")
			try:
				tipo=int(input("Ingrese el tipo de publicacion que quiere agregar: \n[1] Libro\n[2]Audio libro\nIngrese la opcion: "))
				if tipo==1:
					print("Selecciono Libro.")
					autor1=input("Ingrese el autor: ")
					edicion1=input("Ingrese el año de edicion: ")
					pag1=int(input("Ingrese la cantidad de paginas del libro: "))
					publicacion=Libro(titulo=tit, categoria=cat, precio_base=precio_b, autor=autor1, edicion=edicion1, pag=pag1)
				else:
					print("Selecciono Audio libro")
					tr=int(input("Ingrese el tiempo de reproduccion: "))
					narra=input("Ingrese el nombre del narrador: ")
					publicacion=Audio_Libro(titulo=tit, categoria=cat, precio_base=precio_b, tiempo_rep=tr, nombre_narra=narra)
				lista.agregar_publicacion(publicacion)
			except ValueError:
				print("Error. Se esperaba un numero.")
		elif opcion==2:
			try:
				indice=int(input("Ingrese una posicion: "))
				lista.get_tipo_publi(indice)
			except ValueError:
				print("Error. Se esperaba un numero.")
		elif opcion==3:
			libros, audios= lista.cant_tipos()
			print(f"Hay {libros} publicaciones de tipo Libro.")
			print(f"Hay {audios} publicaciones del tipo Audio libro.")

		elif opcion==4:
			lista.mostrar_lista()
		else: print("Opcion invalida.")
		opcion=menu()