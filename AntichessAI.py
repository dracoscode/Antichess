import chess as Achess
import random as random
from antichess import anti_legal_moves
from copy import deepcopy

class Auto:

    def __init__(self, board, max_depth, side):
        self.board=board
        self.side=side
        self.max_depth=max_depth

    def AImove(self):
        #print(list(anti_legal_moves(self.board)))
        return self.AI(None, 1)



    '''
    Define the evaluation function by Piece-Square Tables. 
    Assign a bonus weight to each type of piece accoroding to its position on the board.
    '''
    def evaluate(self):
        score = 0
        bonus_pawn = [0,  0,  0,  0,  0,  0,  0,  0,
                     50, 50, 50, 50, 50, 50, 50, 50,
                     10, 10, 20, 30, 30, 20, 10, 10,
                      5,  5, 10, 25, 25, 10,  5,  5,
                      0,  0,  0, 20, 20,  0,  0,  0,
                      5, -5,-10,  0,  0,-10, -5,  5,
                      5, 10, 10,-20,-20, 10, 10,  5,
                      0,  0,  0,  0,  0,  0,  0,  0]
        bonus_knight = [-50,-40,-30,-30,-30,-30,-40,-50,
                        -40,-20,  0,  0,  0,  0,-20,-40,
                        -30,  0, 10, 15, 15, 10,  0,-30,
                        -30,  5, 15, 20, 20, 15,  5,-30,
                        -30,  0, 15, 20, 20, 15,  0,-30,
                        -30,  5, 10, 15, 15, 10,  5,-30,
                        -40,-20,  0,  5,  5,  0,-20,-40,
                        -50,-40,-30,-30,-30,-30,-40,-50]
        bonus_bishop = [-20,-10,-10,-10,-10,-10,-10,-20,
                        -10,  0,  0,  0,  0,  0,  0,-10,
                        -10,  0,  5, 10, 10,  5,  0,-10,
                        -10,  5,  5, 10, 10,  5,  5,-10,
                        -10,  0, 10, 10, 10, 10,  0,-10,
                        -10, 10, 10, 10, 10, 10, 10,-10,
                        -10,  5,  0,  0,  0,  0,  5,-10,
                        -20,-10,-10,-10,-10,-10,-10,-20]
        bonus_rook = [-20,-10,-10,-10,-10,-10,-10,-20,
                      -10,  0,  0,  0,  0,  0,  0,-10,
                      -10,  0,  5, 10, 10,  5,  0,-10,
                      -10,  5,  5, 10, 10,  5,  5,-10,
                      -10,  0, 10, 10, 10, 10,  0,-10,
                      -10, 10, 10, 10, 10, 10, 10,-10,
                      -10,  5,  0,  0,  0,  0,  5,-10,
                      -20,-10,-10,-10,-10,-10,-10,-20]
        bonus_queen = [-20,-10,-10, -5, -5,-10,-10,-20,
                       -10,  0,  0,  0,  0,  0,  0,-10,
                       -10,  0,  5,  5,  5,  5,  0,-10,
                        -5,  0,  5,  5,  5,  5,  0, -5,
                         0,  0,  5,  5,  5,  5,  0, -5,
                       -10,  5,  5,  5,  5,  5,  0,-10,
                       -10,  0,  5,  0,  0,  0,  0,-10,
                       -20,-10,-10, -5, -5,-10,-10,-20]
        bonus_king = [-30,-40,-40,-50,-50,-40,-40,-30,
                      -30,-40,-40,-50,-50,-40,-40,-30,
                      -30,-40,-40,-50,-50,-40,-40,-30,
                      -30,-40,-40,-50,-50,-40,-40,-30,
                      -20,-30,-30,-40,-40,-30,-30,-20,
                      -10,-20,-20,-20,-20,-20,-20,-10,
                       20, 20,  0,  0,  0,  0, 20, 20,
                       20, 30, 10,  0,  0, 10, 30, 20]
        inverse = [56, 57, 58, 59, 60, 61, 62, 63,
                   48, 49, 50, 51, 52, 53, 54, 55,
                   40, 41, 42, 43, 44, 45, 46, 47,
                   32, 33, 34, 35, 36, 37, 38, 39,
                   24, 25, 26, 27, 28, 29, 30, 31,
                   16, 17, 18, 19, 20, 21, 22, 23,
                    8, 9, 10, 11, 12, 13, 14, 15,
                    0, 1, 2, 3, 4, 5, 6, 7]
        for i in range(64):
            score+=self.pieceweight(Achess.SQUARES[i])
            if (self.board.color_at(Achess.SQUARES[i])==self.side):
                if(self.board.piece_type_at(Achess.SQUARES[i]) == Achess.PAWN):
                    score += bonus_pawn[i]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.ROOK):
                    score += bonus_rook[i]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.BISHOP):
                    score += bonus_bishop[i]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.KNIGHT):
                    score += bonus_knight[i]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.QUEEN):
                    score += bonus_queen[i]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.KING):
                    score += bonus_king[i]
            else:
                if(self.board.piece_type_at(Achess.SQUARES[i]) == Achess.PAWN):
                    score -= bonus_pawn[inverse[i]]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.ROOK):
                    score -= bonus_rook[inverse[i]]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.BISHOP):
                    score -= bonus_bishop[inverse[i]]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.KNIGHT):
                    score -= bonus_knight[inverse[i]]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.QUEEN):
                    score -= bonus_queen[inverse[i]]
                elif (self.board.piece_type_at(Achess.SQUARES[i]) == Achess.KING):
                    score -= bonus_king[inverse[i]]

        return score

    

    '''
    Assign a weight to each type of piece
    '''
    def pieceweight(self, square):
        pieceweight = 0
        if(self.board.piece_type_at(square) == Achess.PAWN):
            pieceweight = 100
        elif (self.board.piece_type_at(square) == Achess.ROOK):
            pieceweight = 500
        elif (self.board.piece_type_at(square) == Achess.BISHOP):
            pieceweight = 330
        elif (self.board.piece_type_at(square) == Achess.KNIGHT):
            pieceweight = 320
        elif (self.board.piece_type_at(square) == Achess.QUEEN):
            pieceweight = 900
        elif (self.board.piece_type_at(square) == Achess.KING):
            pieceweight = 20000

        if (self.board.color_at(square)!=self.side):
            return -pieceweight
        else:
            return pieceweight

    

        
    def AI(self, action, depth):
        
        # Base case
        if ( depth == self.max_depth
        or len(anti_legal_moves(self.board)) == 0):
            return self.evaluate()
            
        all_moves = list(anti_legal_moves(self.board))
            
        curr_val = None
        best_move = None
        
        #odd depth for my turn, otherwise for opponent
        if(depth % 2 != 0):
            curr_val = float("-inf")
        else:
           curr_val = float("inf")
            
        for i in all_moves:
            temp = deepcopy(self)
            temp.board.push(i)
            value = temp.AI(curr_val, depth + 1) 

            #minmax algorithm:
            #maximize curr_val for my play
            if(value > curr_val and depth % 2 != 0):
                    #need to save move played by the engine
                if (depth == 1):
                    best_move=i
                curr_val = value
            #minimize curr_val for opponent's play
            elif(value < curr_val and depth % 2 == 0):
                curr_val = value

            #Alpha-beta prunning: 
            #if previous turn is mine
            if (action != None
            and value < action
            and depth % 2 == 0):
                temp.board.pop()
                break
            #otherwise
            elif (action != None 
            and value > action 
            and depth % 2 != 0):
                temp.board.pop()
                break
                

        if (depth>1):
                #return value of a move in the tree
            return curr_val
        else:
                #return the move (only on first move)
            return best_move



  



            
            


        


        



            






        
        




        




    
    
