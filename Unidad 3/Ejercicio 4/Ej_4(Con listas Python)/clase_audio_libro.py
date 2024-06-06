from clase_publicacion import Publicacion

class Audio_Libro(Publicacion):
    __tiempo_rep: int
    __nombre_narra: str

    def __init__(self, **kwargs):
        super().__init__(kwargs['titulo'], kwargs['categoria'], kwargs['precio_base'])
        self.__tiempo_rep = kwargs['tiempo_rep']
        self.__nombre_narra = kwargs['nombre_narra']

    def get_tiempo_rep(self):
        return self.__tiempo_rep

    def get_nombre_narra(self):
        return self.__nombre_narra

    def __str__(self):
        return f'Titulo: {super().get_titulo()}\nTiempo de reproduccion: {self.__tiempo_rep}'

    def get_importe_venta(self):
        importe = self.get_precio_base() + ((10 * self.get_precio_base()) / 100)
        return importe