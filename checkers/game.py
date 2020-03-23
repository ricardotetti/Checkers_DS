from board import *
import random
import sys

class Jogada:

    def __init__(self):
        self._movs_captura = []
        self._movs_sem_captura = []

    def setCaptura(self, vetor):
        if(vetor[-1] == vetor[-2]):
            pass
        else:
            self._movs_captura.append(vetor)

    def setMovsNormal(self, vetor):
        if(vetor[-1] == vetor[-2]):
            pass
        else:
            self._movs_sem_captura.append(vetor)

    def getCaptura(self):
        return self._movs_captura

    def getSemCaptura(self):
        return self._movs_sem_captura

    def vetorMovimentos(self, index):
        if(len(self._movs_captura) > 0):
            return self._movs_captura
        else:
            return self._movs_sem_captura


class Jogo:
    def __init__(self):
        self.board = Board(8)
        self._turn = "brancas"
        self._contador_jogadas = 0
        self.acabou_de_capturar = False

    def troca_turno(self):
        self._turn = "brancas" if self._turn == "pretas" else "pretas"


    def fim_de_jogo(self):
        self.troca_turno()
        print("\n\n\n\n\nFim de jogo\n\n{} ganharam!\n\n\n\n".format(self._turn))
        print()
        sys.exit(0)

    def empate(self):
        print("\n\n\n\n\nFim de jogo\n\nEmpate!\n\n\n\n".format(self._turn))
        print()
        sys.exit(0)

    def printa_movs(self, movimentos):

        mov = [] #Vetor que armazena todas as jogadas
        for i in range(len(movimentos)):
            if(len(movimentos[i][1]) > 0):
                mov.append(movimentos[i])
        if(len(mov) == 0):
            self.fim_de_jogo()

        else:
            jogadas = Jogada()
            for i in range(len(mov)):
                index_peca = mov[i][0]
                try:
                    for j in range(len(mov[i][1])):
                        peca_ameacada_x = mov[i][1][j][0][0]
                        peca_ameacada_y = mov[i][1][j][0][1]
                        peca_ameacada_index = self.board._pecas[0].procura_x_y(peca_ameacada_x, peca_ameacada_y, self.board._pecas)
                        espaco_vago_x = mov[i][1][j][1][0]
                        espaco_vago_y = mov[i][1][j][1][1]
                        jogadas.setCaptura([index_peca, peca_ameacada_index, espaco_vago_x, espaco_vago_y])

                except TypeError:
                    for j in range(len(mov[i][1])):
                        espaco_vago_x = mov[i][1][j][0]
                        espaco_vago_y = mov[i][1][j][1]
                        jogadas.setMovsNormal([index_peca, espaco_vago_x, espaco_vago_y])

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n#-------------------------------------------------------------------#\n\n")
            print("\t\t\t\t\tTABULEIRO")
            print("\t\t\t\t** TURNO DAS {} **".format(self._turn.upper()))
            self.board.print_board()

            aux = jogadas.getCaptura()
            aux1 = jogadas.getSemCaptura()

            #--> Lógica utilizada para deixar o tabuleiro sempre no mesmo lugar no terminal
            n = (18 - len(aux)) if len(aux) > 0 else 18 - len(aux1)
            for i in range(n):
                print()

            print("Movimentos possíveis das peças {}:".format(self._turn))
            contador = 1


            if(len(aux) > 0):
                self._contador_jogadas = 0
                for i in range(len(aux)):
                    print("Jogada {}: Peça {} {} |---> [{},{}]".format(i+1, aux[i][0], self.board._pecas[aux[i][0]].getPos(), aux[i][2], aux[i][3]))

            elif(self.acabou_de_capturar == False):
                self._contador_jogadas += 1
                for i in range(len(aux1)):
                    print("Jogada {}: Peça {} {} |---> [{},{}]".format(i+1, aux1[i][0], self.board._pecas[aux1[i][0]].getPos(), aux1[i][1], aux1[i][2]))

            elif(len(aux1) == 0):
                self.fim_de_jogo()

            else:
                return -1

            return  aux if len(aux) > 0 else aux1


    def todosMovimentosTurno(self):
        movimentos = self.board.allMoves(self._turn)
        return movimentos

    def movimenta_peca(self, movimentos):
        movs = self.printa_movs(movimentos) #Recebe um vetor com todas as jogadas possíveis
        if(movs == -1):
            self.acabou_de_capturar = False
            self.troca_turno()
            return


        if(self._turn == "brancas"):
            while(True):
                i = int(input("Qual jogada deseja realizar: "))
                if(i > 0 and i <= len(movs)):
                    break
                else:
                    print("Comando não reconhecido, refaça outra jogada:")
        else:
            aux = len(movs)

            try:
                random.seed()
                i = random.randint(1, len(movs))
                print("Comando da máquina: ", i)
            except Exception:
                self.fim_de_jogo()

        i -= 1
        if(len(movs[0]) == 3):
            self.board._pecas[movs[i][0]].setPos([movs[i][1], movs[i][2]])
            self.acabou_de_capturar = False
            self.troca_turno()

        elif(len(movs[0]) == 4):
            self.board._pecas[movs[i][0]].setPos([movs[i][2], movs[i][3]])
            self.board._pecas[movs[i][1]].deletaPeca()
            self.acabou_de_capturar = True
            self.turno()
        else:
            self.fim_de_jogo()

    def turno(self):
        #--> Verifica todos os movimentos que as peças do turno podem fazer e salva em movimentos
        movimentos = self.todosMovimentosTurno()
        #--> Faz o movimento do jogo
        if(self.movimenta_peca(movimentos) == -1):
            return -1
        if(self._contador_jogadas == 20):
            self.empate()


#--> Faz toda a interação com o usuário
    def joga(self):
        #--> Loop infinito que acaba quando o jogo acaba
        while(True):
            if(self.turno() == -1):
                self.fim_de_jogo()
                break
