class farmacia:
    __gestor_ventas=list

    def __init__(self, gestor_ventas=[]) -> None:
        self.__gestor_ventas=  gestor_ventas

    def inicializar(self):
        n=5
        m=7
        for i in range(n):
            self.__gestor_ventas.append([0]*m)

    def acumula(self, dia, sucursal, importe):
        c=dia-1
        f=sucursal-1
        self.__gestor_ventas [c][f] += importe
        return
    
    def importe_sucursal(self, sucursal):
        t=sucursal-1
        total=0.0
        for i in 7:
            total+=self.__gestor_ventas[t][i]

        return total
    
    def cal_max(self, dia):
        d=dia-1
        max=0

        for i in 7:
            if max<self.__gestor_ventas[i][d]:
                max=self.__gestor_ventas
                k=i+1
        return k
    
    def cal_min(self):
        min=10000
        for i in 5:
            for j in 7:
                suma+=self.__gestor_ventas[i][j]

            if min>suma:
                f= i
                min=suma
        return f
    
    def total_sucursales(self):
        sum=0
        for i in 5:
            for j in 7:
                sum+=self.__gestor_ventas[i][j]

        return sum 
        