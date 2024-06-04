from claseMoto import moto
import csv

class GestorMoto:
	__gestor_moto: list
	def __init__(self):
		self.__gestor_moto= []

	def cargar_moto(self):
		archivo=open('datosMotos.csv')
		reader=csv.reader(archivo, delimiter=";")

		for fila in reader:
			patente=fila[0]
			marca=fila[1]
			apellido=fila[2]
			nombre=fila[3]
			kilometraje=fila[4]

			unaMoto=moto(patente, marca, apellido, nombre, kilometraje)
			self.cargar_datos(unaMoto)

		archivo.close()

	def cargar_datos(self, unamoto):
		self.__gestor_moto.append(unamoto)

	def buscarpatente(self, patente):
		i=0
		while i<len(self.__gestor_moto):
			print(f"{self.__gestor_moto[i].getPatente()}")
			if (patente==self.__gestor_moto[i].getPatente()):
				return self.__gestor_moto[i].getPatente()
			else:
				i+=1
		return None

	def get_lista(self):
		return self.__gestor_moto