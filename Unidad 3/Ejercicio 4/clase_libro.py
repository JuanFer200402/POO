from clase_publicacion import Publicacion
class Libro(Publicacion):
	__autor: str
	__edicion: str
	__pag: int

	def __init__(self, **kwargs):
		super().__init__(kwargs['titulo'], kwargs['categoria'], kwargs['precio_base'])
		self.__autor=kwargs['autor']
		self.__edicion=kwargs['edicion']
		self.__pag=kwargs['pag']

	def get_autor(self):
		return self.__autor

	def get_edicion(self):
		return self.__edicion

	def get_pag(self):
		return self.__pag

	def __str__(self):
		return f'Titulo: {super().get_titulo()}\n Autor: {self.__autor}'

	def get_importe_venta(self):
		anio=int(self.get_edicion()[6:10])
		importe=self.get_precio_base()+((2024-anio)*self.get_precio_base())/100
		return importe