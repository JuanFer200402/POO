class Ladrillo:
	__alto=7
	__largo=25
	__ancho=15
	__cantidad: int
	__ident: int
	__materia_prima:float
	__costo:float
	__material: list

	def __init__(self, cantidad, ident, materia_prima, costo):
		self.__cantidad=cantidad
		self.__ident=ident
		self.__materia_prima=materia_prima
		self.__costo=costo
		self.__material=[]

	@classmethod
	def get_alto(cls):
		return cls.__alto

	@classmethod
	def get_largo(cls):
		return cls.__largo

	@classmethod
	def get_ancho(cls):
		return cls.__ancho

	def get_cantidad(self):
		return self.__cantidad

	def get_ident(self):
		return self.__ident

	def get_materia_prima(self):
		return self.__materia_prima

	def get_costo(self):
		return self.__costo

	def agregar_material(self, un_material):
		if un_material not in self.__material:
			self.__material.append(un_material)
			print(f"Al ladrillo {self.__ident} se le agrego el material {un_material.get_material()}.")
		else: print(f"Al ladrillo {self.__ident} no se le agrego el material {un_material.get_material()} porque ya lo tiene.")

	def listar_datos_materiales(self):
		if len(self.__material)!=0:
			for material in self.__material:
				print(f"Material: {material.get_material()}\n Caracteristicas: {material.get_caracteristicas()}\n Costo adicional: {material.get_costo_adicional()}")
		else: print("El ladrillo correspondiente a esa ID no utiliza material refractario. ")

	def get_costo_total(self):
		acum=self.__costo
		for material in self.__material:
			acum+=material.get_costo_adicional()
		return acum

	def get_materiales(self):
		materiales:str=""
		if len(self.__material)>0:
			for material in self.__material:
				materiales+=str(material.get_material())+", "
		return materiales

	def get_costo_total_adicional(self):
		costo:str=""
		if len(self.__material)>0:
			for material in self.__material:
				costo+=str(material.get_costo_adicional())+", "
		return costo