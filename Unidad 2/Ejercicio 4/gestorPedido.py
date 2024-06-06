from clasePedido import pedido
from gestorMoto import GestorMoto
import csv

class GestorPedido:
	__gestor_pedido:list
	def __init__(self):
		self.__gestor_pedido= []

	def cargar_pedido(self):
		archivo=open("datosPedidos.csv")
		reader=csv.reader(archivo, delimiter=";")
		bandera=True

		for fila in reader:
			patente=fila[0]
			id_pedido=int(fila[1])
			com_pedido=int(fila[2])
			tiempo_entrega=int(fila[3])
			tiempo_real=int(fila[4])
			precio=float(fila[5])

			un_pedido=pedido(patente, id_pedido, com_pedido, tiempo_entrega, tiempo_real, precio)
			self.cargar_datos(un_pedido)
		self.ordenar()

	def cargar_datos(self, unpedido):
		self.__gestor_pedido.append(unpedido)

	def ordenar(self):
		self.__gestor_pedido.sort()
		return

	def nuevosPedidos(self, pt, idpat, comped, tpped, trped, precioped, motos):
		p=motos.buscarpatente(pt)
		if p != None:
			otropedido=pedido(pt, idpat, comped, tpped, trped, precioped)
			self.cargar_datos(otropedido)
			self.ordenar()
			return True
		else:
			return False

	def modificarTiempoR(self, numpatente, idenPedido, tiemporeal):
		a=0
		while a < len(self.__gestor_pedido):
			if (numpatente == self.__gestor_pedido[a].getpatente()):
				if (idenPedido == self.__gestor_pedido[a].getidpedido()):
					self.__gestor_pedido[a].settiemporeal(tiemporeal)
					break
			a+=1
		if (a< len(self.__gestor_pedido)):
			return True
		else: return False

	def mostrar_por_patente(self, patentex, moto):
		moto_buscada= moto.buscarpatente(patentex)
		cont=0
		acum=0
		if (moto_buscada != None):
			c=0
			while c<len(self.__gestor_pedido):
				if (self.__gestor_pedido[c].getpatente() == moto_buscada.getpatente()):
					acum+=self.__gestor_pedido[c].gettiemporeal()
					cont+=1
				cont+=1
			moto_buscada.mostrardatos()
			promedio=acum//cont
			return promedio
		else: return False

	def listarmotos(self, moto):
		motos=moto.get_lista()
		for moto in motos:
			print(f"Patente de moto: {moto.getPatente()}")
			print(f"Conductor: {moto.getNombre()} {moto.getApellido()}")
			print(" Identificador de pedido   | Tiempo Estimado | Tiempo Real | Precio")
			pat3=moto.getPatente()
			totalpedidos=0.0
			for pedido in self.__gestor_pedido:
				if pat3==pedido.getpatente():
					print(f"{pedido.getidpedido()}  {pedido.gettiempoentrega()}  {pedido.gettiemporeal()}  ${pedido.getprecio()}")
					totalpedidos+=float(pedido.getprecio())
			print(f"Total: ${totalpedidos: }")
			print("")