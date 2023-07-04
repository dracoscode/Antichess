import AntichessAI as anti
import chess as Achess
from antichess import anti_legal_moves
import sys

class Main:

    def __init__(self, board=Achess.Board):
        self.board=board

    def playOppoMove(self):
        try:
            play = input()
            self.board.push_san(play)
        except:
            self.playOppoMove()

    def playMyMove(self, max_depth, side):
        AI = anti.Auto(self.board, max_depth, side)
        a = AI.AImove()
        print(a)
        self.board.push(a)
        

    def playGame(self):
        #for x in sys.argv:
            #print(x)
        side = sys.argv[1]
        #while(side!="black" and side!="white"):
            #side = input()
        #self.board.color = side
        max_depth=None
        while(isinstance(max_depth, int)==False):
            max_depth = 4
        if side=="white":
            while (self.board.is_checkmate()==False and len(anti_legal_moves(self.board)) != 0):
                if (self.board.is_fifty_moves()):
                    print('1/2-1/2')
                    break
                if (self.board.is_repetition(3)):
                    print('1/2-1/2')
                    break
                self.playMyMove(max_depth, Achess.WHITE)
                if (self.board.is_checkmate()==False and len(anti_legal_moves(self.board)) != 0):
                    self.playOppoMove()
                    if (self.board.is_fifty_moves()):
                        print('1/2-1/2')
                        break
                    if (self.board.is_repetition(3)):
                        print('1/2-1/2')
                        break
            if (self.board.is_checkmate()):
                print(self.board.result())
            elif (len(anti_legal_moves(self.board)) == 0):
                print('1/2-1/2')  
        elif side=="black":
            while (self.board.is_checkmate()==False and len(anti_legal_moves(self.board)) != 0):
                self.playOppoMove()
                if (self.board.is_fifty_moves()):
                    print('1/2-1/2')
                    break
                if (self.board.is_repetition(3)):
                    print('1/2-1/2')
                    break

                if (self.board.is_checkmate()==False and len(anti_legal_moves(self.board)) != 0):
                    self.playMyMove(max_depth, Achess.BLACK)
                    if (self.board.is_fifty_moves()):
                        print('1/2-1/2')
                        break
                    if (self.board.is_repetition(3)):
                        print('1/2-1/2')
                        break
            if (self.board.is_checkmate()):
                print(self.board.result())
            elif (len(anti_legal_moves(self.board)) == 0):
                print('1/2-1/2')


newBoard= Achess.Board()
antichess = Main(newBoard)
start = antichess.playGame()
