from piece import *
import numpy as np

class Board:
    # Inicializa uma matrix Size x Size com zeros.
    # Valores possíveis para cada ponto da matriz: 0 -> sem peça, 1 -> com um
    # peao preto, 2 -> com um peao branco, 3-> rainha preta, 4 -> rainha branca
    def __init__(self, size=8):
        self._pecas = []
        self._size = size

        for j in range(self._size):
            for i in range(self._size):
                if(((self._size - 2) / 2) > j):
                    if((i % 2) != (j % 2)):
                        aux = Piece('b', i, j)
                        self._pecas.append(aux)
                elif((self._size / 2) < j):
                    if((i % 2) != (j % 2)):
                        aux = Piece('w', i, j)
                        self._pecas.append(aux)


#Printa na tela a lista com as peças: "Tipo" "Pos x" "Pos y"
    def print_pecas(self):
        print("Quantidade de peças:", len(self._pecas))
        for i in range(len(self._pecas)):
            print(self._pecas[i]._type, "x:", self._pecas[i]._position_x, "y:", self._pecas[i]._position_y)
        print()


#Printa na tela o tabuleiro"
    def print_board(self):
        canvas = np.zeros((self._size,self._size), dtype = str)

        for i in range(len(self._pecas)):
            x, y = self._pecas[i].getPos()
            aux = self._pecas[i]._type
            canvas[x][y] = aux if aux != "removed" else ""


        print('\t\t\t\t   | 0 1 2 3 4 5 6 7\n\t\t\t\t --+----------------') if self._size == 8 else print('\t\t\t\t  | 0 1 2 3 4 5 6 7 8 9\n\t\t\t\t--+--------------------')
        for i in range(self._size):
            print("\t\t\t\t", i,'|',end=' ')
            for j in range(self._size):
                print("▧", end = " ") if canvas[j][i] == "" else print(canvas[j][i], end = " ")
            print()
        print("\n\n")

    def procura_x_y(self, x, y):
        aux = []
        cont = 0
        for i in range(len(self._pecas)):
            if([x, y] == self._pecas[i].getPos()):
                aux.append(self._pecas[i])
                cont += 1
        if(cont == 0):
            return -1
        else:
            return aux

# -> Vê todos os movimentos das peças brancas ou pretas ou todas
    def allMoves(self, turn = "All"):
        todosMovs = []
        for i in range((int(len(self._pecas)/2)) if turn.upper() == "BRANCAS" else 0, int(len(self._pecas)/2) if turn.upper() == "PRETAS" else len(self._pecas)):
            todosMovs.append([i, self._pecas[i].allMoves(self._pecas)])

        return todosMovs
