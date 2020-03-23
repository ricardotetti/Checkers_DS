class Pilha:
	def __init__(self):
		self.pilha = []
	def insere(self, elemento):
		self.pilha.append(elemento)
	def remove(self):
		c = self.pilha.pop(-1)
		return c
	def mostra_pilha(self):
		return self.pilha

pilha = Pilha()
pilha.insere(5)
pilha.insere(20)
pilha.insere(23)
pilha.insere(24)
pilha.insere(12)

print(pilha.remove())
print(pilha.mostra_pilha())