class Matricula:
	__fecha: str
	__empleado: object
	__programa: object

	def __init__(self, fecha, empleado, programa):
		self.__fecha=fecha
		self.__empleado=empleado
		self.__programa=programa

	def get_fecha(self):
		return self.__fecha
	def get_empleado(self):
		return self.__empleado
	def get_programa(self):
		return self.__programa

	
