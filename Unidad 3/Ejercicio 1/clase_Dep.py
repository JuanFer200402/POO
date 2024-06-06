class Depto: 
	__Id: int
	__nya_prop: str
	__piso: int
	__nro_dep: int
	__cant_habt: int
	__cant_banos: int
	__superficie: float

	def __init__ (self, Id, nya_prop, piso, nro_dep, cant_habt, cant_banos, superficie):
		self.__Id=Id
		self.__nya_prop=nya_prop
		self.__piso=piso
		self.__nro_dep=nro_dep
		self.__cant_habt=cant_habt
		self.__cant_banos=cant_banos
		self.__superficie=superficie

	def get_id(self):
		return self.__Id

	def get_nya_prop(self):
		return self.__nya_prop

	def get_piso(self):
		return self.__piso

	def get_nro_dep(self):
		return self.__nro_dep

	def get_cant_habt(self):
		return self.__cant_habt

	def get_cant_banos(self):
		return self.__cant_banos

	def get_superficie(self):
		return self.__superficie
