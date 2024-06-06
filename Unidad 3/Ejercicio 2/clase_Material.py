class Material:
	__material: int
	__caracteristicas: str
	__cantidad: float
	__costo_adicional: float

	def __init__(self, material, caracteristicas, cantidad, costo_adicional):
		self.__material=material
		self.__caracteristicas=caracteristicas
		self.__cantidad=cantidad
		self.__costo_adicional=costo_adicional

	def get_material(self):
		return self.__material

	def get_caracteristicas(self):
		return self.__caracteristicas

	def get_cantidad(self):
		return self.__cantidad

	def get_costo_adicional(self):
		return self.__costo_adicional