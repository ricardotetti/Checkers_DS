class Fila:
	def __init__(self):
		self.fila = []
	def insere(self, elemento):
		self.fila.append(elemento)
	def remove(self):
		self.fila.pop(0)

	def verifica_impares(self):
		c = 0
		for n in self.fila:
			if n%2 != 0:
				c += 1
			else:
				None
		return c


fila = Fila()
fila.insere(5)
fila.insere(20)
fila.insere(3)
fila.insere(15)

print(fila.verifica_impares())