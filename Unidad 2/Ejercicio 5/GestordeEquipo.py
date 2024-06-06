from claseEquipo import Equipo
from GestordeFecha import GestorFecha
import csv

class GestorEquipo():
	__gestorequipo : list

	def __init__(self):
		self.__gestorequipo = []

	def cargararchivoEquipo(self):
		archivo=open('equipo2024.csv')
		reader=csv.reader(archivo, delimiter=";")

		for Fila in reader:
			unequipo=Equipo(int(Fila[0]), Fila[1], int(Fila[2]), int(Fila[3]), int(Fila[4]), int(Fila[5]))
			self.nuevoequipo(unequipo)
		archivo.close()

	def nuevoequipo(self, equipo):
		self.__gestorequipo.append(equipo)

	def actualizar (self, fecha):
		equipos= self.__gestorequipo
		fechas=fecha.longitud()
		for equipo in equipos:
			for fechasss in fechas:
				if equipo.getidequipo()==fechasss.getIdEquipolocal():
					valor1 = fechasss.getcantGoleslocal()
					valor2 = fechasss.getcantGolesvisitante()
					valordif= valor1 - valor2
					equipo.setgolesfavor(valor1)
					equipo.setgolescontra(valor2)
					equipo.setdiferenciagoles(valordif)

					if fechasss.getcantGoleslocal() > fechasss.getcantGolesvisitante():
						val1=3
						equipo.setpuntos(val1)
					elif fechasss.getcantGoleslocal() == fechasss.getcantGolesvisitante():
						val2=1
						equipo.setpuntos(val2)
					elif fechasss.getcantGoleslocal() < fechasss.getcantGolesvisitante():
						val3=0
						equipo.setpuntos(val3)

				elif equipo.getidequipo()== fechasss.getIdEquipovisitante():
					valor1 = fechasss.getcantGolesvisitante()
					valor2 = fechasss.getcantGoleslocal()
					valordif = valor1 - valor2
					equipo.setgolesfavor(valor1)
					equipo.setgolescontra(valor2)
					equipo.setdiferenciagoles(valordif)
					if fechasss.getcantGolesvisitante() > fechasss.getcantGoleslocal():
						val1= 3
						equipo.setpuntos(val1)
					elif fechasss.getcantGolesvisitante == fechasss.getcantGoleslocal():
						val2=1
						equipo.setpuntos(val2)
					elif fechasss.getcantGolesvisitante() < fechasss.getcantGoleslocal():
						val3=0
						equipo.setpuntos(val3)

	def verificarequipo(self, nombre, fecha):
		nombrebuscado=self.buscarequipo(nombre)
		fechas=fecha.longitud()
		puntosss=0
		print(f"EQUIPO: {nombrebuscado.getNombre()}")
		print("FECHAS  |  GOLESAFAVOR  |  GOLESENCONTRA  |  DIFERENCIAGOLES  |  PUNTOS")
		for fechasss in fechas:
			if nombrebuscado.getidequipo() == fechasss.getIdEquipolocal():
				diferenciagoles=fechasss.getcantGoleslocal() - fechasss.getcantGolesvisitante()
				if fechasss.getcantGoleslocal() > fechasss.getcantGolesvisitante():
					puntosss=3
				elif fechasss.getcantGoleslocal() == fechasss.getcantGolesvisitante():
					puntosss=1
				elif fechasss.getcantGoleslocal() < fechasss.getcantGolesvisitante():
					puntosss=0
				print(f"{fechasss.getFecha()}  |  {fechasss.getcantGoleslocal()}  |  {fechasss.getcantGolesvisitante()}  |  {diferenciagoles}  |  {puntosss}")  
			elif nombrebuscado.getidequipo() == fechasss.getIdEquipovisitante():
				diferenciagoles = fechasss.getcantGolesvisitante() - fechasss.getcantGoleslocal()
				if fechasss.getcantGolesvisitante() > fechasss.getcantGolesvisitante():
					puntosss=3
				elif fechasss.getcantGolesvisitante() == fechasss.getcantGolesvisitante():
					puntosss=1
				elif fechasss.getcantGolesvisitante() < fechasss.getcantGoleslocal():
					puntosss=0
				print(f"{fechasss.getFecha()}  |  {fechasss.getcantGolesvisitante()}  |  {fechasss.getcantGoleslocal()}  |  {diferenciagoles}  |  {puntosss}")
		print("------------------------------------------------------------------------------------")
		print(f"TOTALES:   {nombrebuscado.getgolesfavor()}  |  {nombrebuscado.getgolescontra()}  |  {nombrebuscado.getdiferenciagoles()}|  {nombrebuscado.getpunto()}")
	
	def buscarequipo(self, nombre):
		i=0
		nombre2=None
		while i<len(self.__gestorequipo):
			if (self.__gestorequipo[i].getNombre() == nombre):
				nombre2=self.__gestorequipo[i]
				break
			else:
				i+=1
		print(f"{nombre2}")
		return nombre2

	def ordenar(self):
		self.__gestorequipo.sort(reverse=True)

	def almacenartabla(self):
		with open('NuevoArchivo.csv', mode='w', newline='') as archivo:
			writer=csv.writer(archivo,delimiter=';')
			for fila in self.__gestorequipo:
				writer.writerow([fila.getidequipo(), fila.getNombre(), fila.getgolesfavor(), fila.getgolescontra(), fila.getdiferenciagoles(), fila.getpunto()])
	