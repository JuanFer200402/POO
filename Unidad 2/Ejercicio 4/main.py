from gestorMoto import GestorMoto
from gestorPedido import GestorPedido
import csv

if __name__ == '__main__':
    #Inciso 1 y 2
    moto=GestorMoto()
    moto.cargar_moto()
    pedido=GestorPedido()
    pedido.cargar_pedido()
	
    while True:
        print("_____MENU DE OPCIONES_____")
        print("Seleccione una opcion:")
        print("[a]- Cargar nuevo pedido ")
        print("[b]- Modificar timpo real de un pedido")
        print("[c]- Mostrar datos del conductor y el tiempo promedio de sus entregas")
        print("[d]- Listar Motos")
        print("[e]- Ordenar")
        print("[f]- Salir")

        opcion= input("Ingrese la opcion deseada: ")
        
        if opcion=="a":
            print("Ingrese los siguientes datos para cargar un pedido:")
            pat=input("Ingrese una patente: ")
            idped=int(input("Ingrese id del pedido: "))
            comped=int(input("Ingrese la cantidad de comida: "))
            tpped=int(input("Ingrese el tiempo del pedido: "))
            trped=float(input("Ingrese el tiempo real del pedido: "))
            precioped=float(input("Ingrese el precio del pedido: "))
            resultado=pedido.nuevosPedidos(pat, idped, comped, tpped,trped, precioped, moto)
            if resultado:
                    print("El pedido se cargo correctamente")
            else:
                    print("El pedido no se completo")
            pedido.ordenar()
        else:
            if opcion=="b":
                numpatente=int(input("Ingrese numero de patente: "))
                idenpedido=int(input("Ingrese el identificador del pedido: "))
                tiemporeal=int(input("Ingrese el timpo real del pedido: "))
                resul=pedido.modificarTiempoR(numpatente, idenpedido, tiemporeal)
                if resul==True:
                    print("Se cambie el valor de tiempo real con exito")
                else: print("No se pudo completar la operacion algun dato que ingreso es incorrecto")
            else:
                if opcion=="c":
                    patente1=int (input("Ingrese la patente de la moto de la cual quiere saber los datos: "))
                    print("Datos del conductor:")
                    resul2= pedido.mostrar_por_patente(patente1, moto)
                    print("")
                    if resul2 != False:
                        print(f"El promedio de entrega de este conductor es: {resul2}")
                    else: print("La patente ingresada es incorrecta")
                else:
                    if opcion == "d":
                        print("Listado de las motos:")
                        pedido.listarmotos(moto)
                    else:
                    	if opcion=="e":
                    		pedido.ordenar()
                    	else:
                    		if opcion=="f":
                    			print("Chauuu")
                    			break    