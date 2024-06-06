from clase_matricula import Matricula
import csv
class Matriculas:
	__matriculas: list

	def __init__(self):
		self.__matriculas=[]

	def crear_matriculas(self, empleados, cursos):
		archivo=open("matriculas.csv")
		reader=csv.reader(archivo,delimiter=';')
		next(reader)
		for fila in reader:
			una_matricula=Matricula(fila[0], empleados.get_empleado(int(fila[1])), cursos.get_capacitacion(fila[2]))
			una_matricula.get_empleado().matricular(una_matricula)
			una_matricula.get_programa().matriculado(una_matricula)
			self.__matriculas.append(una_matricula)
		archivo.close()