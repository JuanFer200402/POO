from clase import CajaDeAhorro
from contenedor import Contenedor

if __name__ == '__main__':
    #Ejercicio 1
    caja=CajaDeAhorro("34", "20-46331259-2", "Juan", "Fernandez", 40000)

    caja.MostrarDatos()

    if caja.Extraer(30000)<0:
        print("La extraccion no se pudo realizar por falta de saldo")
    else:
        print("La extraccion fue exitosa")

    if caja.Depositar(20000)<0:
        print("No se puede depositar un saldo negativo")
    else:
        print("El deposito fue exitoso")

    if caja.validarcui()==False:
        print("Cuil invalido")
    else:
        print("Cuil valido")

    #Ejerecicio 2
    
    unacaja=CajaDeAhorro("20", "20-46333222-2","Pablo", "Gomez", 30000)
    otracaja=CajaDeAhorro("22", "20-22444555-2", "Tito", "Perez", 150000)
    Contenedorr=Contenedor([unacaja,caja, otracaja])
    
    cuilabuscar=input("Ingrese el cuil asociado a la cuenta deseada: ")
    Contenedorr.Obtenerdatos(cuil=cuilabuscar)
    

    
