class Capacitacion:
	__nombre: str
	__codigo: str
	__duracion: int
	__matriculas: list

	def __init__(self, nombre, codigo, duracion):
		self.__nombre=nombre
		self.__codigo=codigo
		self.__duracion=duracion
		self.__matriculas=[]

	def get_nombre(self):
		return self.__nombre
	def get_codigo(self):
		return self.__codigo
	def get_duracion(self):
		return self.__duracion

	def matriculado(self, una_matricula):
		self.__matriculas.append(una_matricula)

	def listar_empleados(self):
		print("Empleados matriculados:")
		if len(self.__matriculas)>0:
			for matricula in self.__matriculas:
				print(f"{matricula.get_empleado()}")
		else: print("Ninguno.")