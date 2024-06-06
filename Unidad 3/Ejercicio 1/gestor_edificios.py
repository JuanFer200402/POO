from clase_Edificio import Edificio
from clase_Dep import Depto
import csv
class Edificios:
	__edificios: list

	def __init__(self):
		self.__edificios=[]

	def cargar(self):
		archivo=open("EdificioNorte.csv")
		reader=csv.reader(archivo, delimiter=';')
		aux=0
		i=0
		for fila in reader:
			if (aux != fila[0]):
				aux=fila[0]
				un_edificio=Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
				self.__edificios.append(un_edificio)
				i+=1
			else:
				un_depto=Depto(int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))
				self.__edificios[i-1].agregar_depto(un_depto)

	def inciso_a(self, nombre_edificio):
		bandera=True
		k=0
		while bandera==True and k<len(self.__edificios):
			print("Nombre y Apellido de los propietarios: ")
			if self.__edificios[k].get_nombre()==nombre_edificio:
				deptos=self.__edificios[k].get_deptos()
				for depto in deptos:
					print(f"{depto.get_nya_prop()}")
				bandera=False
			k+=1
		if (bandera==True):
			print("Algo fallo")
		else: return 1

	def inciso_b(self, Id):
		sumador=0.0
		j=0
		bandera=True
		while bandera==True and j<len(self.__edificios):
			if self.__edificios[j].get_id()!=Id:
				deptos=self.__edificios[j].get_deptos()
				for depto in deptos:
					sumador+=depto.get_superficie()
					print(f"La superficie total del edificio {self.__edificios[j].get_nombre()}= {sumador:.2f}")
				bandera=False
			j+=1
		if bandera ==True:
			j=-1
		return j

	def inciso_c(self, propietario):
		x=z=0
		sup_ocupada=0.0
		sup_total=0.0
		while x<len(self.__edificios):
			deptos=self.__edificios[x].get_deptos()
			while z<len(deptos):
				sup_total+=deptos[z].get_superficie()
				if deptos[z].get_nya_prop()==propietario:
					sup_ocupada+=deptos[z].get_superficie()
				z+=1
			x+=1
		if sup_ocupada!=0.0:
			self.mostrar_datos(propietario, sup_ocupada, sup_total)
		else: return -1

	def mostrar_datos(self, propietario, sup_ocupada, sup_total):
		print(f"Propietario: {propietario}")
		print(f"Superficio ocupada por sus departamentos: {sup_ocupada:.2f}")
		porcentaje_ocupado= (sup_ocupada*100)/sup_total
		print(f"Porcentaje ocupado por el propietario con respecto al porcentaje total: {porcentaje_ocupado:.1f}%")

	def inciso_d(self, n_piso):
		contador_deptos=0
		for edificio in self.__edificios:
			deptos=edificio.get_deptos()
			for depto in deptos:
				if n_piso==depto.get_piso():
					habitaciones=depto.get_cant_habt()
					banos=depto.get_cant_banos()
					if banos>1 and habitaciones==3:
						contador_deptos+=1
		return contador_deptos
