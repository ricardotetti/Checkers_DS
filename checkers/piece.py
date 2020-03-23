class Piece:
    # Type pode ser: b -> peao preto, w -> peao branco, B -> rainha negra,
    # W -> Rainha branca
    def __init__(self, type, x, y):
        self._type = type
        self._position_x = x
        self._position_y = y
        self._deleted = False

    def getType(self):
        return self._type

    def getPos(self):
        return [self._position_x, self._position_y]

    def getCanCap(self):
        return self._canCap

    def deletaPeca(self):
        self._type = "removed"
        self._position_x = 0
        self._position_y = 0
        self._deleted = True


#--> Função Set para definir x e y da peça
#--> Recebe array com [x, y]
    def setPos(self, pos):
        self._position_x = pos[0]
        self._position_y = pos[1]

        if(self._type == "w" and self._position_y == 0):
            self.setQueen()
        elif(self._type == "b" and self._position_y == 7):
            self.setQueen()


#--> Função que procura no vetor das peças qual é o index da peça com as coordenadas x e y
#--> Retorno: -1 se não tiver a peça, -2 se der erro e o index se for encontrada a peça
    def procura_x_y(self, x, y, vec_pecas):
        if(x < 0 or y < 0 or x >= 8 if len(vec_pecas) == 24 else 10 or y >= 8 if len(vec_pecas) == 24 else 10):
            print("x ou y fora da range do tabuleiro")
            return -2

        for i in range(len(vec_pecas)):
            if(vec_pecas[i].getPos() == [x, y]):
                return i
        return -1

#--> A peça que convocar essa função é transformada em rainha
#--> Retorna True e transforma a peça em rainha quando dá certo e False se a peça já é rainha
    def setQueen(self):
        if(self._type == "b" or self._type == "w"):
            self._type = "B" if self._type == "b" else "W"
            return True
        else:
            print("Peça", self._type,"já é uma rainha")
            return False


#--> Se as peças forem do mesmo time retorna 1, se não retorna 0
    def mesmoTime(self, piece_to_compare):
        team1 = "pretas" if self._type.upper() == "B" else "brancas"
        team2 = "pretas" if piece_to_compare.getType().upper() == "B" else "brancas"
        if(team1 == team2):
            return True
        return False

#--> Função que retorna a coordenada do movimento desejado pela peça
#--> Recebe: dir_x:"left" ou "right", dir_y:"up" ou "down", vec_pecas é o array
#--> com todas as peças de board e vezes a quantidade de casas na direção desejada
#--> Retorna: quando certo retorna array com [x, y] da posição, se der erro retorna -1
    def _mov_futuro_peca(self, dir_x, dir_y, vec_pecas, vezes = 1):

        board_size = 8 if len(vec_pecas) == 24 else 10 # Determina o tamanho do tabuleiro para que não haja movimentos futuros saindo do tabuleiro

        if(dir_y == "up"):
            if(dir_x == "left" and self._position_x >= vezes and self._position_y >= vezes):
                return [self._position_x-vezes, self._position_y-vezes]
            elif(dir_x == "right" and self._position_y >= vezes and self._position_x+vezes < board_size):
                return [self._position_x+vezes, self._position_y-vezes]
            else:
                return -1
        else:
            if(dir_x == "right" and self._position_x+vezes < board_size and self._position_y+vezes < board_size):
                return [self._position_x+vezes, self._position_y+vezes]
            elif(dir_x == "left" and self._position_x >= vezes and self._position_y+vezes < board_size):
                return [self._position_x-vezes, self._position_y+vezes]
            else:
                return -1

# Função privada que ajuda a simplificar a função allMoves
# Retorno: vetor com o [x, y] da posição final da peça (após captura) ou -1 se não houver o que capturar
    def _queenMove(self, dir_x, dir_y, vec_pecas):

        can_capture = []
        can_move = []

        #Lógica que verifica até que ponto está com casas vazias
        i = 1
        while(True):
            mov_novo = self._mov_futuro_peca(dir_x, dir_y, vec_pecas, i) # Pega as coordenadas [x,y] da posição futura da peça
            if(mov_novo == -1):
                index = -1
                break
            index = self.procura_x_y(mov_novo[0], mov_novo[1], vec_pecas)
            if(index != -1):
                break
            else:
                can_move.append(mov_novo)
            i += 1

        if(index != -1 and self.mesmoTime(vec_pecas[index]) == False):
            i += 1
            filled_space = mov_novo
            mov_novo = self._mov_futuro_peca(dir_x, dir_y, vec_pecas, i)
            if(mov_novo != -1):
                index = self.procura_x_y(mov_novo[0], mov_novo[1], vec_pecas)
            while(index == -1 and mov_novo != -1):
                can_capture.append((filled_space, mov_novo))
                i += 1
                mov_novo = self._mov_futuro_peca(dir_x, dir_y, vec_pecas, i)
                if(mov_novo == -1):
                    break
                index = self.procura_x_y(mov_novo[0], mov_novo[1], vec_pecas)

        if(len(can_capture) == 0):
            return can_move

        self._canCap = True
        return can_capture

    def whereToMove(self, vec_pecas, turn):

        posicoes_permitidas = []
        vezes = 1

        dir_y = "up" if turn == "brancas" else "down"
        dir_x = "left"

        vec_pos = self._mov_futuro_peca(dir_x, dir_y, vec_pecas)

        if(vec_pos != -1):
            index = self.procura_x_y(vec_pos[0], vec_pos[1], vec_pecas)
            if(index == -1):
                posicoes_permitidas.append(vec_pos)

        dir_x = "right"

        vec_pos = self._mov_futuro_peca(dir_x, dir_y, vec_pecas)

        if(vec_pos != -1):
            index = self.procura_x_y(vec_pos[0], vec_pos[1], vec_pecas)
            if(index == -1):
                posicoes_permitidas.append(vec_pos)

        return posicoes_permitidas


#-> Verifica quais peças podem ser capturadas
#-> Entrada: Recebe de board o vetor com todas as peças, no caso (_peças)
#-> Saída: Retorna todas as peças que são possíveis serem capturadas pela peça
#-> que chamou a função, o retorno é um array de TUPLAS com dois vetores posição em cada tupla, o
#-> primeiro refere-se à peça que pode ser capturada o segundo o espaço para
#-> onde a peça pode parar após a captura, se não houverem peças para captura, return -1
    def allMoves(self, vec_pecas):
        can_capture = []
        can_move = []
        cont = 0

        if(self._type == "b" or self._type == "w"):
            filled_space = (self._mov_futuro_peca("left", "up", vec_pecas, 1),
                            self._mov_futuro_peca("right", "up", vec_pecas, 1),
                            self._mov_futuro_peca("right", "down", vec_pecas, 1),
                            self._mov_futuro_peca("left", "down", vec_pecas, 1))

            free_space = (self._mov_futuro_peca("left", "up", vec_pecas, 2),
                            self._mov_futuro_peca("right", "up", vec_pecas, 2),
                            self._mov_futuro_peca("right", "down", vec_pecas, 2),
                            self._mov_futuro_peca("left", "down", vec_pecas, 2))
            for i in range(len(filled_space)):
                for j in range(len(vec_pecas)):
                    notFree = False
                    if(vec_pecas[j].getPos() == filled_space[i] and self.mesmoTime(vec_pecas[j]) == False):
                        for k in range(len(vec_pecas)):
                            if(vec_pecas[k].getPos() == free_space[i] or free_space[i] == -1):
                                notFree = True
                        if(notFree != True):
                            can_capture.append((filled_space[i], free_space[i]))

            if(len(can_capture) == 0):
                possible_moves = self.whereToMove(vec_pecas, "brancas" if self._type.upper() == "W" else "pretas")
                for i in range(len(possible_moves)):
                    can_move.append(possible_moves[i])

        else:
            dir_x = "left"
            dir_y = "up"
            aux = self._queenMove(dir_x, dir_y, vec_pecas)

            try:
                nothing = aux[0][0][0]
                for i in range(len(aux)):
                    can_capture.append(aux[i])
            except Exception:
                for i in range(len(aux)):
                    can_move.append(aux[i])


            dir_x = "right"
            dir_y = "up"
            aux = self._queenMove(dir_x, dir_y, vec_pecas)

            try:
                nothing = aux[0][0][0]
                for i in range(len(aux)):
                    can_capture.append(aux[i])
            except Exception:
                for i in range(len(aux)):
                    can_move.append(aux[i])


            dir_x = "right"
            dir_y = "down"
            aux = self._queenMove(dir_x, dir_y, vec_pecas)

            try:
                nothing = aux[0][0][0]
                for i in range(len(aux)):
                    can_capture.append(aux[i])
            except Exception:
                for i in range(len(aux)):
                    can_move.append(aux[i])


            dir_x = "left"
            dir_y = "down"
            aux = self._queenMove(dir_x, dir_y, vec_pecas)

            try:
                nothing = aux[0][0][0]
                for i in range(len(aux)):
                    can_capture.append(aux[i])
            except Exception:
                for i in range(len(aux)):
                    can_move.append(aux[i])

        if(len(can_capture) == 0):
            return can_move

        self._canCap = True
        return can_capture
