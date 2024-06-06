class pedido:
	__patente:str
	__id_pedido:int
	__com_pedido:int
	__tiempo_entrega:int
	__tiempo_real:int
	__precio:float
	def __init__(self, patente, id_pedido, com_pedido, tiempo_entrega, tiempo_real, precio):
		self.__patente=patente
		self.__id_pedido=id_pedido
		self.__com_pedido=com_pedido
		self.__tiempo_entrega=tiempo_entrega
		self.__tiempo_real=tiempo_real
		self.__precio=precio

	def getpatente(self):
		return self.__patente

	def getidpedido(self):
		return self.__id_pedido

	def getcom_pedido(self):
		return self.__com_pedido

	def gettiempoentrega(self):
		return self.__tiempo_entrega

	def gettiemporeal(self):
		return self.__tiempo_real

	def settiemporeal(self, nuevovalor):
		self.__tiempo_real=nuevovalor

	def getprecio(self):
		return self.__precio

	def __lt__(self, otro):
		return self.__patente < otro.__patente