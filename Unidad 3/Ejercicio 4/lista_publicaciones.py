from clase_nodo import Nodo
from clase_audio_libro import Audio_Libro
from clase_libro import Libro
import csv
class Lista:
	__comienzo: Nodo
	__actual: Nodo
	__indice: int
	__tope: int

	def __init__(self):
		self.__comienzo=None
		self.__actual=None
		self.__indice=0
		self.__tope=0

	def __iter__(self):
		return self

	def get_tope(self):
		return self.__tope

	def __next__(self):
		if self.__indice==self.__tope:
			self.__actual=self.__comienzo
			self.__indice=0
			raise StopIteration
		else:
			self.__indice+=1
			dato=self.__actual.get_dato()
			self.__actual=self.__actual.get_siguiente()
			return dato

	def cargar_archivo(self):
		archivo1=open("libros.csv")
		reader1=csv.reader(archivo1,delimiter=';')
		next(reader1)
		for fila1 in reader1:
			un_libro=Libro(titulo=fila1[0], categoria=fila1[1], precio_base=float(fila1[2]), autor=fila1[3], edicion=fila1[4], pag=int(fila1[5]))
			self.agregar_publicacion(un_libro)
		archivo1.close()

		archivo2=open("cd.csv")
		reader2=csv.reader(archivo2, delimiter=';')
		next(reader2)
		for fila2 in reader2:
			un_audio=Audio_Libro(titulo=fila2[0], categoria=fila2[1], precio_base=float(fila2[2]), tiempo_rep=int(fila2[3]), nombre_narra=fila2[4])
			self.agregar_publicacion(un_audio)
		archivo2.close()

	def agregar_publicacion(self, una_publicacion):
		#Carga al principio de la lista
		nodo=Nodo(una_publicacion)
		nodo.set_siguiente(self.__comienzo)
		self.__comienzo=nodo
		self.__actual=nodo
		self.__tope+=1

	def get_tipo_publi(self, indice):
		if indice <self.get_tope():
			aux=self.__comienzo
			for i in range(indice):
				aux=aux.get_siguiente()
			if isinstance(aux.get_dato(),Libro) is True:
				print(f"La publicacion '{aux.get_dato().get_titulo()}' es una publicacion del tipo Libro.")
			elif isinstance(aux.get_dato(),Audio_Libro) is True:
				print(f"La publicacion '{aux.get_dato().get_titulo()}' es una publicacion del tipo Audio libro.")
		else: 
			print(f"Ingreso una posicion no valida. Debe ser entre 0 y {self.get_tope()-1}")

	def cant_tipos(self):
		cont1=0
		cont2=0
		aux=self.__comienzo
		while aux != None:
			if isinstance(aux.get_dato(),Libro) is True:
				cont1+=1
			elif isinstance(aux.get_dato(),Audio_Libro) is True:
				cont2+=1
			aux=aux.get_siguiente()
		return (cont1,cont2)

	def mostrar_lista(self):
		for publicacion in self:
			importe=publicacion.get_importe_venta()
			print(f"Titulo: {publicacion.get_titulo()}\nCategoria: {publicacion.get_categoria()}\nImporte de venta: ${importe:.2f}")
			print("---------------------------------")

