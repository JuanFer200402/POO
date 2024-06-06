class Fecha():
	__fecha : str
	__idequipolocal : int
	__idequipovisitante : int
	__cantgoleslocal : int
	__cantgolesvisitantes : int

	def __init__ (self, fecha, idequipolocal, idequipovisitante, cantgoleslocal, cantgolesvisitantes):
		self.__fecha = fecha
		self.__idequipolocal = idequipolocal
		self.__idequipovisitante = idequipovisitante
		self.__cantgoleslocal = cantgoleslocal
		self.__cantgolesvisitantes = cantgolesvisitantes

	def getFecha(self):
		return self.__fecha

	def getIdEquipolocal(self):
		return self.__idequipolocal

	def getIdEquipovisitante(self):
		return self.__idequipovisitante

	def getcantGoleslocal(self):
		return self.__cantgoleslocal

	def getcantGolesvisitante(self):
		return self.__cantgolesvisitantes

	def __sub__(self, otro):
		return self.getcantGoleslocal() - otro.getcantGolesvisitante()