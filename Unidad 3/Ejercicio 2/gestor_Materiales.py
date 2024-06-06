from clase_Material import Material
import csv
class Materiales:
	__materiales: list

	def __init__(self):
		self.__materiales=[]

	def carga_archivo(self):
		archivo = open("materiales.csv")
		reader=csv.reader(archivo, delimiter=';')
		next(reader)
		for fila in reader:
			un_mat=Material(int(fila[0]), fila[1], float(fila[2]), float(fila[3]))
			self.__materiales.append(un_mat)
		archivo.close()

	def get_total_material(self):
		return len(self.__materiales)

	def get_material(self, posicion):
		return self.__materiales[posicion]