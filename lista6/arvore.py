class Arvore:
	def __init__(self, data):
		self.direita = None
		self.esquerda = None
		self.data = data
	

	def inserir_valor(self, data):
		if self.data:
			if data < self.data:
				if self.esquerda == None:
					self.esquerda = Arvore(data)
				else:
					self.esquerda.inserir_valor(data)
			elif data > self.data:
				if self.direita == None:
					self.direita = Arvore(data)
				else:
					self.direita.inserir_valor(data)
		else:
			self.data = data

	def altura(self):
		
		if self.direita and self.esquerda:
			return max(self.esquerda.altura(), self.direita.altura())
		elif self.direita:
			return 1 + self.direita.altura()
		elif self.esquerda:
			return 1 + self.esquerda.altura() 
		else:
			return 1

	
	def preordem(self):
		if self:
			print(str(self.data))
			if self.esquerda:
				self.esquerda.preordem()
			if self.direita:
				self.direita.preordem()

	def posordem(self):
		if self:
			if self.esquerda:
				self.esquerda.posordem()
			if self.direita:
				self.direita.posordem()
			print(str(self.data))

	def inorder(self):
		if self:
			if self.esquerda:
				self.esquerda.inorder()
			print(str(self.data))
			
			if self.direita:
				self.direita.inorder()

	def search(self, valor):
		if self.data == None or self.data == valor:
			return self.data
		elif self.data > valor:
			return self.esquerda.search(valor)
		else:
			return self.direita.search(valor)


	#def percurso(self):
	#	fila = []
	#	if self:
	#		if self.esquerda:
	#			fila.append(self.data)
	#			self.esquerda.percurso()
	#		if self.direita:
	#			fila.append(self.data)
	#			self.direita.percurso()
	#	while len(fila)>0:
	#		v = fila.pop(0)
	#		print(v)
	#		for k in [self.esquerda, self.direita]:
	#			if k != None:
	#				fila.append(k)

	#def pre(self):
		#pilha = []
		#if self:
		#	if self.esquerda:
		#		pilha.append(self.esquerda)
		#		self.esquerda.pre()
		#	if self.direita:
		#		pilha.append(self.direita)
		#		self.direita.pre()
		#return pilha
		#while pilha != []:
		#	top = pilha.pop()
		#	print(top)
		#	for i in [self.direita,self.esquerda]:
		#		if i != None:
		#			pilha.append(i)



arvore = Arvore(10)
arvore.inserir_valor(5)
arvore.inserir_valor(15)
arvore.inserir_valor(7)
arvore.inserir_valor(18)
arvore.inserir_valor(25)
print("Altura arvore: ")
print(arvore.altura())
print("Preordem: ")
arvore.preordem()
print("Posordem: ")
arvore.posordem()
print("Inorder: ")
arvore.inorder()
print("Busca: ")
print(arvore.search(18))
#print(arvore.percurso())
#print(arvore.pre())