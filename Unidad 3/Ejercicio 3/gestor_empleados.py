from clase_empleado import Empleado
import csv
class Empleados:
	__empleados: list

	def __init__ (self):
		self.__empleados=[]

	def carga_archivo(self):
		archivo=open("datosEmpleados.csv")
		reader=csv.reader(archivo, delimiter=';')
		next(reader)
		for fila in reader:
			un_empleado=Empleado(fila[0], int(fila[1]), fila[2])
			self.__empleados.append(un_empleado)
		archivo.close()

	def get_empleado(self, idd):
		if idd!=None:
			i=0
			band=False
			while i<len(self.__empleados) and band is False:
				if self.__empleados[i].get_id_emp()==idd:
					band=True
				else: i+=1
		else: return None
		if band: 
			return self.__empleados[i]

	def inciso_a(self, id2):
		i=0
		band=False
		while band is False and i<len(self.__empleados):
			if self.__empleados[i].get_id_emp()==id2:
				self.__empleados[i].obtener_duracion_total()
				band=True
			else: i+=1
		assert band is True

	def inciso_c(self):
		i=0
		band=False
		while i<len(self.__empleados) and band is False:
			if self.__empleados[i].cantidad_cursos()==0:
				print(self.__empleados[i])
				band=True
			else: i+=1
		assert band is True
