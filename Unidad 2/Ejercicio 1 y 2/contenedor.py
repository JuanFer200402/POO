from clase import CajaDeAhorro

class Contenedor():
    __lista: list[CajaDeAhorro]

    def __init__(self, lista) -> None:
        self.__lista= lista

    def agregar(self, nuevo):
        self.__lista.append(nuevo)

    def Obtenerdatos(self, cuil):
        indicecaja=self.buscar_caja(cuil)
        Caja_encontrada= self.__lista[indicecaja]
        if Caja_encontrada!=-1:
            Caja_encontrada.MostrarDatos()

    def buscar_caja(self, cuil) -> CajaDeAhorro:
        retorno=-1
        bandera=False
        i=0
        while i<(len(self.__lista)) and bandera == False:
            if self.__lista[i].obtenercuil() == cuil:
                retorno=i
                bandera=True
            i+=1
        
        return retorno
