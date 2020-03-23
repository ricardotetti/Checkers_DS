class Fila:
	def __init__(self):
		self.fila = []
	def insere(self, elemento):
		self.fila.append(elemento)
	def remove(self):
		c = self.fila.pop(0)
		return c
	def retorna_fila(self):
		return self.fila


fila = Fila()
fila.insere(5)
fila.insere(20)
fila.insere(3)
fila.insere(15)

print(fila.remove())

print(fila.retorna_fila())