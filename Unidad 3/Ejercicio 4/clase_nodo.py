from clase_publicacion import Publicacion
class Nodo:
	__publicacion: Publicacion
	__siguiente: object

	def __init__(self, publicacion):
		self.__publicacion=publicacion
		self.__siguiente=None

	def set_siguiente(self, siguiente):
		self.__siguiente=siguiente

	def get_dato(self):
		return self.__publicacion

	def get_siguiente(self):
		return self.__siguiente
"""
Eliminar (se utiliza en la clase lista)
 def eliminarPorDNI(self, dni):
 	aux=self.__comienzo
 	encontrado = False
 	if aux.getDato().getDNI()==dni:
 		encontrado=True
 		print('Encontrado:'+str(aux.getDato()))
 		self.__comienzo = aux.getSiguiente()
 		self.__tope-=1
 		del aux
 	else:
 		ant = aux
 		aux = aux.getSiguiente()
 		while not encontrado and aux != None:
 			if aux.getDato().getDNI()==dni:
 				encontrado=True
 			else:
 				ant = aux
 				aux=aux.getSiguiente()
 		if encontrado:
 			print('Encontrado:'+str(aux.getDato()))
 			ant.setSiguiente(aux.getSiguiente())
 			self.__tope-=1
 			del aux
 		else:
 			print('El DNI {}, no está en la lista'.format(dni))
"""