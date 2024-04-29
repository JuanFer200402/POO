from clase1 import farmacia

if __name__=='__main__':
    farmacias=farmacia()
    farmacias.inicializar()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("Seleccione una opcion:")
        print("[a]- Ingrese una factura")
        print("[b]- Total de Facturacion para una sucursal")
        print("[c]- Calcular la Sucursal con mayor facturacion en un dia ingresado")
        print("[d]- Calcular Sucursal con menor facturacion en toda la semana")
        print("[e]- Calcular el total facturado por todas las Sucursales en toda la semana")

        opcion= input("Ingrese la opcion deseada: ")
        
        if opcion=="a":
            print("Ingrese los siguientes datos para cargar la factura:")
            diaa=int(input("Ingrese el dia: "))
            sucursall=int(input("Ingrese la sucursal: "))
            importee=int(input("Ingrese el importe: "))
            if (diaa>=1 and diaa<=7)and(sucursall>=1 and sucursall<=7):
                farmacias.acumula(diaa, sucursall, importee)
            else:
                print("Los valores que as ingresado son incorrectos")
        else:
            if opcion=="b":
                print("Ingrese el siguiente dato:")
                sucursall=int(input("Ingrese la sucursal: "))
                if (sucursall>=1 and sucursall<=7):
                    print(f"El total de la sucursal seleccionada: {farmacias.importe_sucursal(sucursall)}")
                else:
                    print("El dato es invalido")
            else:
                if opcion=="c":
                    print("Ingrese el siguiente dato:")
                    diaa=int(input("Ingrese el dia: "))
                    farmacias.cal_max(diaa)
                    print(f"La sucursal con mayor facturacion es: {farmacias.cal_max(diaa)}")
                else:
                    if opcion=="d":
                        print(f"La sucursal con menor facturacion es: {farmacias.cal_min()}")
                    else:
                        if opcion=="e":
                            print(f"El total de todas las facturas de todas las sucursales es: {farmacias.total_sucursales()}")




