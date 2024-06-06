from clase_Ladrillo import Ladrillo
import csv
import random
class Ladrillos:
	__ladrillos: list

	def __init__(self):
		self.__ladrillos=[]

	def carga_archivo(self):
		archivo=open("ladrillos.csv")
		reader=csv.reader(archivo, delimiter=';')
		next(reader)
		for fila in reader:
			un_lad=Ladrillo(int(fila[0]), int(fila[1]), float(fila[2]), float(fila[3]))
			self.__ladrillos.append(un_lad)
		archivo.close()

	def asignacion(self, materiales):
		indice_lad=list(range(len(self.__ladrillos)))
		indice_mat=list(range(materiales.get_total_material()))
		for i in range(10):
			ladrillo=random.choice(indice_lad)
			material=random.choice(indice_mat)
			self.__ladrillos[ladrillo].agregar_material(materiales.get_material(material))

	def inciso_a(self, id_lad):
		band=False
		i=0
		while band is False and i<len(self.__ladrillos):
			if self.__ladrillos[i].get_ident()==id_lad:
				self.__ladrillos[i].listar_datos_materiales()
				band=True
			else: i+=1
		assert band is True

	def inciso_b(self):
		for ladrillo in self.__ladrillos:
			costo_total=ladrillo.get_costo_total()
			print(f"El costo total de fabricacion del ladrillo {ladrillo.get_ident()} es: ${costo_total:.2f}")

	def inciso_c(self):
		for ladrillo in self.__ladrillos:
			id_lad=ladrillo.get_ident()
			mater=ladrillo.get_materiales()
			print(f"Nro. de identificacion: {id_lad}")
			if mater!="":
				costo=ladrillo.get_costo_total_adicional()
				print("Material 						Costo Asociado")
				print(f"{mater} 							 {costo}")
				print("-------------------------------------------------------")
			else: 
				print("---									--- ")