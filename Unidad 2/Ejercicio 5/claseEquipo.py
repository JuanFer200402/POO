class Equipo():
	__idequipo : int
	__NombEquipo : str
	__golesfavor: int
	__golescontra : int
	__diferenciagoles : int
	__puntos : int

	def __init__(self, idequipo, nomequipo, golesfavor, golescontra, diferenciagoles, puntos):
		self.__idequipo = idequipo
		self.__NombEquipo = nomequipo
		self.__golesfavor = golesfavor
		self.__golescontra = golescontra
		self.__diferenciagoles = diferenciagoles
		self.__puntos = puntos

	def getidequipo(self):
		return self.__idequipo

	def getNombre(self):
		return self.__NombEquipo

	def getgolesfavor(self):
		return self.__golesfavor
	def setgolesfavor(self, valor):
		self.__golesfavor = self.__golesfavor + valor

	def getgolescontra(self):
		return self.__golescontra
	def setgolescontra(self, valor):
		self.__golescontra = self.__golescontra + valor

	def getdiferenciagoles(self):
		return self.__diferenciagoles
	def setdiferenciagoles(self, valor):
		self.__diferenciagoles = self.__diferenciagoles + valor

	def getpunto(self):
		return self.__puntos
	def setpuntos(self, puntoss):
		self.__puntos += puntoss

	def __gt__(self, otro):
		
		if self.getpunto() != otro.getpunto():
			return self.getpunto() > otro.getpunto()
		elif self.getpunto() == otro.getpunto():
			return self.getgolesfavor() > otro.getgolesfavor()