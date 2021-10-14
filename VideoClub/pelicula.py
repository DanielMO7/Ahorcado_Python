class Pelicula():

	def __init__(self, codigo, titulo, genero):
		self.codigo = codigo
		self.titulo = titulo
		self.genero = genero

	def mostrar_pelicula(self):
		print("Código: ", self.codigo)
		print("Título: ", self.titulo)
		print("Género: ", self.genero)

	# tarea realisar el listar, elimianar, etc, peliculas 	