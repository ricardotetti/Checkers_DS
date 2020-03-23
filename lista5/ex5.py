class Diretores:
	def __init__(self):
		self.diretores = []
		self.filmes = []
		self.quantidade = []
	def insere_diretores(self, nome, numero):
		self.diretores.append(nome)
		self.diretores.append(numero)
		self.quantidade.append(numero)
	def insere_filmes(self, filme, ano, duracao):
		for i in self.quantidade:
			while (i >= 0):
				self.filmes.append(filme)
				self.filmes.append(ano)
				self.filmes.append(duracao)
				i -= 1
	def monstra_filmes(self):
		return self.filmes

	def mostra(self):
		return self.diretores

diretores = Diretores()
diretores.insere_diretores("ab", 1)
diretores.insere_diretores("bc", 1)

diretores.insere_filmes("nemo","2004","1h30min")
diretores.insere_filmes("hulk","2000","2h")


print(diretores.mostra())

print(diretores.monstra_filmes())