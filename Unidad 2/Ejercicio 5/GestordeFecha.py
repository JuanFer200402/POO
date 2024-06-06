from claseFecha import Fecha
import csv

class GestorFecha():
	__gestorFecha : list

	def __init__ (self):
		self.__gestorFecha = []

	def cargararchivoFecha(self):
		archivo = open('fechasFutbol.csv')
		reader=csv.reader(archivo, delimiter= ';')

		for Fila in reader:
			unafecha = Fecha(Fila[0], int(Fila[1]), int(Fila[2]), int(Fila[3]), int(Fila[4]))
			self.nuevafecha(unafecha)
		archivo.close()

	def nuevafecha(self, unafecha):
		self.__gestorFecha.append(unafecha)

	def longitud(self):
		return self.__gestorFecha

