class Fila_Pilha:
	def __init__(self):
		self.pilha = []
		self.fila = []
	def insere_fila(self, elemento_fila):
		self.fila.append(elemento_fila)
	def remove_fila(self):
		c = self.fila.pop(0)
	def insere_pilha(self, elemento_pilha):
		self.pilha.append(elemento_pilha)
	def remove_pilha(self):
		k = self.pilha.pop(-1)
	def mostra_fila(self):
		return self.fila
	def inverte(self):
		for i in self.fila:
			h = self.fila.pop(0)
			self.pilha.append(h)
			k = self.pilha.pop(-1)
			self.fila.append(k)
			return self.fila

fila = Fila_Pilha()
fila.insere_fila(5)
fila.insere_fila(20)
fila.insere_fila(3)
fila.insere_fila(15)

print(fila.mostra_fila())

print(fila.inverte())