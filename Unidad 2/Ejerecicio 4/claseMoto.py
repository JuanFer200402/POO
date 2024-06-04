class moto:
	__patente:str
	__marca:str
	__apellido:str
	__nombre: str
	__kilometraje:int
	def __init__(self, patente, marca, apellido, nombre, kilometraje):
		self.__patente=patente
		self.__marca=marca
		self.__apellido=apellido
		self.__nombre=nombre
		self.__kilometraje=kilometraje

	def mostrardatos(self):
		print(f"Nombre y apellido del conductor: {self.__nombre} {self.__apellido}")
		print(f"Patente de la moto: {self.__patente}")
		print(f"Marca de la moto: {self.__marca}")
		print(f"Patente de la moto: {self.__patente}")
		print(f"Kilometraje de la moto: {self.__kilometraje}")

	def getPatente(self):
		return self.__patente

	def getMarca(self):
		return self.__marca

	def getApellido(self):
		return self.__apellido

	def getNombre(self):
		return self.__nombre

	def getKm(self):
		return self.__kilometraje