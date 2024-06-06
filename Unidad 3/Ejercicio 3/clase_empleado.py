class Empleado:
	__nom_ap: str
	__id_emp: int
	__puesto: str
	__matriculas: list

	def __init__(self, nom_ap, id_emp, puesto):
		self.__nom_ap=nom_ap
		self.__id_emp=id_emp
		self.__puesto=puesto
		self.__matriculas=[]

	def get_nom_ap(self):
		return self.__nom_ap
	def get_id_emp(self):
		return self.__id_emp
	def get_puesto(self):
		return self.__puesto
	def __str__(self):
		return f"\nNombre: {self.__nom_ap}\nPuesto: {self.__puesto}\n"

	def matricular(self, una_matricula):
		self.__matriculas.append(una_matricula)

	def obtener_duracion_total(self):
		print(f"El/La empleado/a {self.__nom_ap} esta matriculado/a en: ")
		if len(self.__matriculas)>0:
			for matricula in self.__matriculas:
				curso=matricula.get_programa()
				print(f"Nombre de la capacitacion: {curso.get_nombre()}\n Duracion: {curso.get_duracion()}")
				print("------------------------------------------------------------------------------------")
		else: print("Ningun curso.")

	def cantidad_cursos(self):
		return len(self.__matriculas)