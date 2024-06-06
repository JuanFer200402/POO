from clase_Dep import Depto
class Edificio:
	__Id: int
	__nombre: str
	__direccion: str
	__nomb_construc: str
	__cant_pisos:int
	__cant_dep: int
	__deptos:list

	def __init__ (self,Id, nombre, direccion, nomb_construc, cant_pisos, cant_dep):
		self.__Id=Id
		self.__nombre=nombre
		self.__direccion=direccion
		self.__nomb_construc=nomb_construc
		self.__cant_pisos=cant_pisos
		self.__cant_dep=cant_dep
		self.__deptos=[]

	def get_id(self):
		return self.__Id

	def get_nombre(self):
		return self.__nombre

	def get_direccion(self):
		return self.__direccion

	def get_nomb_construct(self):
		return self.__nomb_construc

	def get_cant_pisos(self):
		return self.__cant_pisos

	def get_cant_dep(self):
		return self.__cant_dep

	def get_deptos(self):
		return self.__deptos

	def __lt__(self, otro):
		return self.__Id<otro.get_id()

	def agregar_depto(self, depto):
		self.__deptos.append(depto)

	def __del__(self):
		del self.__deptos
		print("Se eliminaron los departamentos")