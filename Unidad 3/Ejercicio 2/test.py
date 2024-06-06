from gestor_Ladrillos import Ladrillos
from gestor_Materiales import Materiales
def menu():
	op=None
	try: 
		op=int(input(""" 
						Menu de opciones

	[1] Ingresa ID de ladrillo para conocer costo y característica del material
	[2] Listar costo total de fabricacion de todos los ladrillos
	[3] Mostar detalles de ladrillos
	[0] SALIR
	
	Seleccione una opcion: """))
	except ValueError:
		pass
	return op

if __name__ == '__main__':
	ladrillos=Ladrillos()
	materiales=Materiales()
	ladrillos.carga_archivo()
	materiales.carga_archivo()

	ladrillos.asignacion(materiales)

	opcion=menu()
	while opcion!=0:
		if opcion==1:
			try:
				ide=int(input("Ingrese el id del ladrillo: "))
				ladrillos.inciso_a(ide)
			except ValueError:
				print("Error, ingrese un dato numerico.")
			except AssertionError:
				print("El id no corresponde a ningun ladrillo.")
		elif opcion==2:
			ladrillos.inciso_b()
		elif opcion==3:
			ladrillos.inciso_c()
		else: print("Opcion invalida.")
		opcion=menu()