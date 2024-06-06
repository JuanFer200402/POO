from clase_audio_libro import Audio_Libro
from clase_libro import Libro
import csv
class Gestor:
	__gestor: list

	def __init__(self):
		self.__gestor=[]

	def cargar_archivo (self):
		archivo1=open("libros.csv")
		reader1=csv.reader(archivo1, delimiter=';')
		next(reader1)
		for fila1 in reader1:
			una_publi=Libro(titulo=fila1[0], categoria=fila1[1], precio_base=float(fila1[2]), autor=fila1[3], edicion=fila1[4], pag=int(fila1[5]))
			self.__gestor.append(una_publi)
		archivo1.close()

		archivo2=open("cd.csv")
		reader2=csv.reader(archivo2, delimiter=';')
		next(reader2)
		for fila in reader2:
			otra_publi=Audio_Libro(titulo=fila[0], categoria=fila[1], precio_base=float(fila[2]), tiempo_rep=int(fila[3]), nombre_narra=fila[4])
			self.__gestor.append(otra_publi)
		archivo2.close()

	def agregar_publicacion(self, una_publi):
		self.__gestor.append(una_publi)
		print("Publicacion cargada.")

	def inciso_b(self, indice):
		indice-=1
		if isinstance(self.__gestor[indice],Libro) is True:
			print("La publicacion seleccionada es de tipo 'Libro'.")
		elif isinstance(self.__gestor[indice],Audio_Libro) is True:
			print("La publicacion seleccionada es de tipo 'Audio libro'.")

	def inciso_c(self):
		cont1=0
		cont2=0
		for publicacion in self.__gestor:
			if isinstance(publicacion,Libro):
				cont1+=1
			elif isinstance(publicacion,Audio_Libro):
				cont2+=1
		return cont1, cont2

	def mostrar_lista(self):
		for publicacion in self.__gestor:
			print(f"Titulo: {publicacion.get_titulo()}\nCategoria: {publicacion.get_categoria()}\nImporte de venta: ${publicacion.get_importe_venta()}")
			print("--------------------------------------")
