class CajaDeAhorro:
    def __init__(self, nroCuenta:str, cuil:str, nombre:str, apellido:str, saldo:int) -> None:
        self.__nrocuenta= nroCuenta
        self.__cuil= cuil
        self.__nombre= nombre
        self.__apellido= apellido
        self.__saldo= saldo

    def MostrarDatos(self):
        print(f"Numero de cuenta: {self.__nrocuenta}")
        print(f"Cuit: {self.__cuil}")
        print(f"Nombre: {self.__nombre}")
        print(f"Apellido: {self.__apellido}")
        print(f"Saldo: {self.__saldo}")

    def Extraer (self, importe):
        valorRetorno=-1
        if self.__saldo>= importe:
            self.__saldo-=importe
            valorRetorno=self.__saldo
        return valorRetorno
    def Depositar (self, importe):
        valorRetorno=-1
        if importe>=0:
            self.__saldo+=importe
            valorRetorno=1
            
        return valorRetorno
    
    def obtenercuil(self):
        return self.__cuil

    def validarcui(self):
        valorretorno= False
        cuil=1
        if len(self.__cuil)==13 and self.__cuil[2]=='-' and self.__cuil[11]=='-':
            cuil= self.__cuil.replace('-', '')
            peso=[5,4,3,2,7,6,5,4,3,2]
            suma=0

            for i in range (len(cuil)-1):
                suma+=peso[i] * int(cuil[i])
            
            calculo= suma // 11
            resto= suma - (11*calculo)
            digito= 11 - resto
            print(f"{resto}")
            if cuil[10] == str(digito):
                valorretorno=True
            
            return valorretorno
            