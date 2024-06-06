from clase_capacitacion import Capacitacion
import csv
class Capacitaciones:
	__capacitaciones: list

	def __init__(self):
		self.__capacitaciones=[]

	def carga_archivo(self):
		archivo=open("datosCursos.csv")
		reader=csv.reader(archivo, delimiter=';')
		next(reader)
		for fila in reader:
			un_curso=Capacitacion(fila[0], fila[1], int(fila[2]))
			self.__capacitaciones.append(un_curso)
		archivo.close()

	def get_capacitacion(self, un_id):
		if un_id!=None:
			i=0
			band=False
			while i<len(self.__capacitaciones) and band is False:
				if self.__capacitaciones[i].get_codigo()==un_id:
					band=True
				else: i+=1
		else: return None
		if band:
			return self.__capacitaciones[i]

	def inciso_b(self, nomb):
		i=0
		band=False
		while i<len(self.__capacitaciones) and band is False:
			if self.__capacitaciones[i].get_nombre()==nomb:
				band=True
				self.__capacitaciones[i].listar_empleados()
			else: i+=1
		assert band is True