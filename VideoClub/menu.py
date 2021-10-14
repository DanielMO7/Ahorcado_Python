from os import system
from socio import Socio
from videoclub import VideoClub
from pelicula import Pelicula

class Menu:

	# Constructo:
	def __init__(self, videoclub):
		self.videoclub = videoclub

	def adicionar_socio(self):
		system("cls")
		print("********************************************")
		print("***		ADICIONAR SOCIO		****")
		print("********************************************")
		codigo = input("Digite el código del socio: ")
		nombre = input("Digite el nombre del socio: ")
		telefono = input("Digite el teléfono del socio: ")
		domicilio = input("Digite el domicilio del socio: ")
		# Instancia de la clase socio: 
		socio = Socio(codigo, nombre, telefono, domicilio)

		if self.videoclub.adicionar_socio(socio):
			print("********************************************")
			print("Info - El socio fué adicionado correctamente")
			print("********************************************")
			input()	
		else:
			print("********************************************")
			print("Info - El socio no se pudo adicionar	   ")
			print("********************************************")
			input()

	def listar_socio(self):
		system("cls")
		print("*" * 16)
		print("* LISTAR SOCIO *")
		print("*" * 16)
		self.videoclub.listar_socio()
		input()

	def eliminar_socio(self):
		system("cls")
		print("*" * 10)
		print("* ELIMINAR *")
		print("*" * 10)
		codigo = input("Digite el código del socio que desea eliminar: ")

		if self.videoclub.eliminar_socio(codigo):
			print("********************************************")
			print("Info - El socio fué eliminado correctamente")
			print("********************************************")
			input()	
		else:
			print("********************************************")
			print("Info - El socio no se pudo eliminar	   ")
			print("********************************************")
			input()

	def adicionar_pelicula(self):
		system("cls")
		print("*" * 17)
		print("* ADICIONAR PELÍCULA *")
		print("*" * 17)
		codigo = input("Digite el código de la película: ")
		titulo = input("Digite el título de la película: ")
		genero = input("Digite el género de la película: ")
		pelicula = Pelicula(codigo, titulo, genero)

		if self.videoclub.adicionar_pelicula(pelicula):
			print("********************************************")
			print("Info - La película fue adicionada correctamente.")
			print("********************************************")
			input()	
		else:
			print("********************************************")
			print("Info - La película no se puede adicionar.   ")
			print("********************************************")
			input()

	def listar_pelicula(self):
		system("cls")
		print("*" * 16)
		print("* LISTAR PELÍCULA *")
		print("*" * 16)
		self.videoclub.listar_pelicula()
		input()

	def eliminar_pelicula(self):
		system("cls")
		print("*" * 10)
		print("* ELIMINAR *")
		print("*" * 10)
		codigo = input("Digite el código de la película que desea eliminar: ")

		if self.videoclub.eliminar_pelicula(codigo):
			print("********************************************")
			print("Info - La película fué eliminada correctamente")
			print("********************************************")
			input()	
		else:
			print("********************************************")
			print("Info - La película no se pudo eliminar	   ")
			print("********************************************")
			input()		
		

	def mostrar_menu_principal(self):
		while  True:
			system("cls")
			print("********************************************")
			print("********************************************")
			print("***		VIDEOCLUB		****")
			print("********************************************")
			print("********************************************")
			print("***		MENÚ PRINCIPAL		****")
			print("********************************************")
			print("********************************************")
			print(" 1 = Crear Socio ")
			print(" 2 = Listar Socios ")
			print(" 3 = Eliminar Socio ")
			print("--------------------")
			print(" 4 = Crear Película")
			print(" 5 = Listar Película")
			print(" 6 = Eliminar Película")
			print("--------------------")
			print(" 7 = Salir ")
			print("********************************************")

			try:
				print("--------------------------------------------")
				op = int(input("Digite su opción: "))

				if op == 1:
					self.adicionar_socio()

				elif op == 2:
					self.listar_socio()

				elif op == 3:
					self.eliminar_socio()

				elif op == 4:
					self.adicionar_pelicula()

				elif op == 5:
					self.listar_pelicula()

				elif op == 6:
					self.eliminar_pelicula()
			
				elif op == 7:
					break

				else:
					print("*******************************")
					print("Error - Opción de menú invalida")
					print("*******************************")
					input()


			except ValueError:
				print("******************************************")
				print("Error - El valor debe ser un número entero")
				print("******************************************")
				input()

if __name__ == '__main__':
	videoclub = VideoClub("ABC")
	menu = Menu (videoclub)
	menu.mostrar_menu_principal()	