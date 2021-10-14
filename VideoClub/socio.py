class Socio():

	def __init__(self, codigo, nombre, telefono, domicilio):
		self.codigo = codigo
		self.nombre = nombre
		self.telefono = telefono
		self.domicilio = domicilio
		
	def mostrar_socio(self):
		print("Código: ", self.codigo)
		print("Nombre: ", self.nombre)
		print("Teléfono: ", self.telefono)
		print("Domicilio: ", self.domicilio)
		