from gestor_empleados import Empleados
from gestor_capacitaciones import Capacitaciones
from gestor_matriculas import Matriculas
def menu():
	op=None
	try:
		op=int(input("""	
					Menú de Opciones
	[1] Ingrese ID de empleado para conocer duracion de cursos en que esta matriculados
	[2] Ingresa nombre de programa para conocer empleados matriculados en el mismo
	[3] Listar empleados que no estan matriculados a programas
	[0] Salir
		
	Seleccione una opcion: """))
	except ValueError:
		pass
	return op

if __name__ == '__main__':
	empleados=Empleados()
	cursos=Capacitaciones()
	matriculas=Matriculas()
	empleados.carga_archivo()
	cursos.carga_archivo()
	matriculas.crear_matriculas(empleados,cursos)
	opcion=menu()
	while opcion!=0:
		if opcion==1:
			try:
				idd=int(input("Ingresa el id del empleado: "))
				empleados.inciso_a(idd)
			except ValueError:
				print("Error de tipo: Ingreso un dato no correspondiente.")
			except AssertionError:
				print("Error: El id ingresdo no corresponde a ningun empleado.")
		elif opcion==2:
			try: 
				nomb=input("Ingrese el nombre del programa: ")
				cursos.inciso_b(nomb)
			except ValueError:
				print("Error de tipo: Ingreso un dato no correspondiente.")
			except AssertionError:
				print("Error: No existe ese programa.")
		elif opcion==3:
			try: 
				empleados.inciso_c()
			except AssertionError:
				print("Todos los empleados se encuentran matriculados a programas")
		else: print("Opcion invalida.")
		opcion=menu()