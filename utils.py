#Backend - function definitions
alphas = ["a", "b", "c", "d", "e", "f", "g", "h"]

class Piece:
    def __init__(self, pos, color, unit):
        x = alphas.index(pos[0])
        y = 8 - (int(pos[1]))
        self.position = [x, y]
        self.color = color
        self.unit = unit
        self.hasMoved = False
    
    def posToChess(self):
        string = ""
        string += alphas[self.position[0]]
        string += str(8 - self.position[1])
        return string
    
    def moveTo(self, x, y):
        self.position[0] = x
        self.position[1] = y
        self.hasMoved = True
    
    def moveToChess(self, pos, board):
        x = alphas.index(pos[0])
        y = 8 - (int(pos[1]))
        board[self.posToChess()] = None
        self.moveTo(x, y)
        
        board[self.posToChess()] = self

        if self.unit == "P" and (self.posToChess()[1] == 8 or self.posToChess()[1] == 0):
            self.unit == "Q"
    
    def isLegalMove(self, pos, board):
        #X, Y refers to the coordinates of the proposed position
        x = alphas.index(pos[0])
        y = (int(pos[1]))
        if self.unit == "R":
            if x != self.position[0] and y != 8 -self.position[1]:
                return False
            elif x == self.position[0] and y ==  8 - self.position[1]:
                return False
            elif (x >= 8 or x < 0) or (y >= 8 or y < 0):
                return False
            else:
                if x != self.position[0]:
                    if x < self.position[0]:
                        fine = True
                        for i in range(self.position[0], x):
                            j = alphas[i]
                            if type(board[j + str(8 - self.position[1])]) != None:
                                if board[j + str(8 - self.position[1])].color == self.color:
                                    fine = False
                                elif board[j + str(8 - self.position[1])] != board[pos]:
                                    fine = False
                        return fine
                    else:
                        fine = True
                        for i in range(x, self.position[0]):
                            j = alphas[i]
                            if type(board[j + str(8 - self.position[1])]) != None:
                                if board[j + str(8 - self.position[1])].color == self.color:
                                    fine = False
                                elif board[j + str(8 - self.position[1])] != board[pos]:
                                    fine = False
                        return fine
                if y != self.position[1]:
                    if y > 8- self.position[1]:
                        fine = True
                        for i in range(8 -self.position[1], y):
                            j = alphas[x]
                            if type(board[j + str(i)]) != None:
                                if board[j + str(i)].color == self.color:
                                    fine = False
                                elif board[j + str(i)] != board[pos]:
                                    fine = False
                        return fine
                    else:
                        fine = True
                        for i in range(y, self.position[1]):
                            j = alphas[x]
                            if type(board[j + str(i)]) != None:
                                if board[j + str(i)].color == self.color:
                                    fine = False
                                elif board[j + str(i)] != board[pos]:
                                    fine = False
                        return fine
        if self.unit == "B":
            if x == self.position[0] or y == 8 - self.position[1]:
                return False
            elif (x >= 8 or x < 0) or (y >= 8 or y < 0):
                return False
            elif abs(x - self.position[0]) != abs(y - (8-self.position[1])):
                return False
            else:
                fine = True
                
                
                if y > self.position[1]:
                    x = abs(x - self.position[0])
                    for i in range(8 - self.position[1], y):
                        j = alphas[8-i]
                        if isinstance(board[j + str(i)], Piece):
                            if board[j + str(i)].color == self.color and board[j + str(i)] != self:
                                
                                fine = False
                            elif board[j + str(i)] != board[pos]:
                                fine = False
                else:
                    x = abs(x - self.position[0])
                    for i in range(y, 8 - self.position[1]):
                        j = alphas[i]
                        if isinstance(board[j + str(i)], Piece):
                            if board[j + str(i)].color == self.color and board[j + str(i)] != self:
                                print(j, i)
                                fine = False
                            elif board[j + str(i)] != board[pos]:
                                fine = False
                return fine
        if self.unit == "N":
            if (x >= 8 or x < 0) or (y >= 8 or y < 0):
                return False
            elif abs(x - self.position[0]) > 2 or abs((8-y) - (self.position[1])) > 2:
                return False
            elif abs(x - self.position[0]) == 0 or abs((8-y) - (self.position[1])) == 0:
                return False
            elif (isinstance(board[pos], Piece) and board[pos].color != self.color) or board[pos] == None:
                if abs(x - self.position[0]) == 2 and abs((8-y) - (self.position[1])) == 1:
                    return True
                elif abs(x - self.position[0]) == 1 and abs((8-y) - (self.position[1])) == 2:
                    return True
                else:
                    return False
            else:
                return False
        if self.unit == "Q":
            if (x >= 8 or x < 0) and (y >= 8 or y < 0):
                return False
            elif x == self.position[0] and y == 8 - self.position[1]:
                return False
            elif x != self.position[0] and y != 8 -self.position[1]:
                
                if x == self.position[0] or y == 8 - self.position[1]:
                    
                    return False
                elif (x >= 8 or x < 0) or (y >= 8 or y < 0):
                    
                    return False
                elif abs(x - self.position[0]) != abs(y - (8-self.position[1])):
                    
                    return False
                else:
                    fine = True
                    
                    
                    if y > 8 - self.position[1]:
                        x = abs(x - self.position[0])
                        for i in range(self.position[1], y+ 1):
                            j = alphas[8-i]
                            if isinstance(board[j + str(i)], Piece):
                                if board[j + str(i)].color == self.color and board[j + str(i)] != self:
                                    fine = False
                                elif board[j + str(i)] != board[pos]:
                                    fine = False
                    else:
                        x = abs(x - self.position[0])
                        for i in range(y, self.position[1]):
                            j = alphas[i]
                            if isinstance(board[j + str(i)], Piece):
                                if board[j + str(i)].color == self.color and board[j + str(i)] != self:
                                    fine = False
                                elif board[j + str(i)] != board[pos]:
                                    fine = False
                    return fine
            elif x == self.position[0] or y == 8 - self.position[1]:
                if x != self.position[0]:
                    if x < self.position[0]:
                        fine = True
                        for i in range(self.position[0], x):
                            j = alphas[i]
                            if type(board[j + str(8 - self.position[1])]) != None:
                                if board[j + str(8 - self.position[1])].color == self.color and board[j + str(i)] != self:
                                    fine = False
                                elif board[j + str(8 - self.position[1])] != board[pos]:
                                    fine = False
                        return fine
                    else:
                        fine = True
                        for i in range(x, self.position[0]):
                            j = alphas[i]
                            if type(board[j + str(8 - self.position[1])]) != None:
                                if board[j + str(8 - self.position[1])].color == self.color and board[j + str(i)] != self:
                                    fine = False
                                elif board[j + str(8 - self.position[1])] != board[pos]:
                                    fine = False
                        return fine
                if y != 8 -self.position[1]:
                    if y > self.position[1]:
                        fine = True
                        for i in range(8 -self.position[1], y):
                            j = alphas[x]
                            if isinstance(board[j + str(i)], Piece) and board[j + str(i)] != self:
                                if board[j + str(i)].color == self.color:
                                    fine = False
                                elif board[j + str(i)] != board[pos]:
                                    fine = False
                        return fine
                    else:
                        fine = True
                        for i in range(y, self.position[1]):
                            j = alphas[x]
                            if isinstance(board[j + str(i)], Piece) and board[j + str(i)] != self:
                                if board[j + str(i)].color == self.color:
                                    fine = False
                                elif board[j + str(i)] != board[pos]:
                                    fine = False
                        return fine
            else:
                return False
        if self.unit == "K":
            if (x >= 8 or x < 0) or (y >= 8 or y < 0):
                return False
            elif abs(x - self.position[0]) > 1 or abs((8-y) - (self.position[1])) > 1:
                return False
            elif abs(x - self.position[0]) == 0 and abs((8-y) - (self.position[1])) == 0:
                return False
            elif (isinstance(board[pos], Piece) and board[pos].color != self.color) or board[pos] == None:
                return True
            else:
                return False
        if self.unit == "P":
            if self.color < 0 and y < (8 - self.position[1]):
                if (x >= 8 or x < 0) or (y >= 8 or y < 0):
                    return False
                elif not (abs((8-y) - self.position[1]) == 1 or abs((8-y) - self.position[1]) == 2):
                    return False
                elif isinstance(board[pos], Piece) and abs(x - self.position[0]) == 1 and board[pos].color != self.color:
                    return True
                elif isinstance(board[pos], Piece) and abs(x - self.position[0]) == 0:
                    return False
                elif abs(x - self.position[0]) != 0:
                    return False
                elif abs((8-y) - self.position[1]) == 2 and self.hasMoved:
                    return False
                elif abs((8-y) - self.position[1]) == 2 and (not self.hasMoved):
                    return True
                elif abs((8-y) - self.position[1]) == 1:
                    return True
                else:
                    return False
            if self.color > 0 and y > (8 - self.position[1]):
                if (x >= 8 or x < 0) or (y >= 8 or y < 0):
                    return False
                elif not (abs((8-y) - self.position[1]) == 1 or abs((8-y) - self.position[1]) == 2):
                    return False
                elif isinstance(board[pos], Piece) and abs(x - self.position[0]) == 1 and board[pos].color != self.color:
                    return True
                elif isinstance(board[pos], Piece) and abs(x - self.position[0]) == 1:
                    return False
                elif isinstance(board[pos], Piece) and abs(x - self.position[0]) == 0:
                    return False
                elif abs(x - self.position[0]) != 0:
                    return False
                elif abs((8-y) - self.position[1]) == 2 and self.hasMoved:
                    return False
                elif abs((8-y) - self.position[1]) == 2 and (not self.hasMoved):
                    return True
                elif abs((8-y) - self.position[1]) == 1:
                    return True
                else:
                    return False

def makeLegalMove(piece, pos, board):
    if piece.isLegalMove(pos, board):
        prevPos = piece.posToChess()
        piece.moveToChess(pos, board)
        print(board[prevPos])
    else:
        print("ILLEGAL MOVE!!!")

board = {
    "a8": Piece("a8", -1, "R"),
    "b8": Piece("b8", -1, "N"),
    "c8": Piece("c8", -1, "B"),
    "d8": Piece("d8", -1, "Q"),
    "e8": Piece("e8", -1, "K"),
    "f8": Piece("f8", -1, "B"),
    "g8": Piece("g8", -1, "N"),
    "h8": Piece("h8", -1, "R"),

    "a7": Piece("a7", -1, "P"),
    "b7": Piece("b7", -1, "P"),
    "c7": Piece("c7", -1, "P"),
    "d7": Piece("d7", -1, "P"),
    "e7": Piece("e7", -1, "P"),
    "f7": Piece("f7", -1, "P"),
    "g7": Piece("g7", -1, "P"),
    "h7": Piece("h7", -1, "P"),

    "a6": None,
    "b6": None,
    "c6": None,
    "d6": None,
    "e6": None,
    "f6": None,
    "g6": None,
    "h6": None,

    "a5": None,
    "b5": None,
    "c5": None,
    "d5": None,
    "e5": None,
    "f5": None,
    "g5": None,
    "h5": None,

    "a4": None,
    "b4": None,
    "c4": None,
    "d4": None,
    "e4": None,
    "f4": None,
    "g4": None,
    "h4": None,

    "a3": None,
    "b3": None,
    "c3": None,
    "d3": None,
    "e3": None,
    "f3": None,
    "g3": None,
    "h3": None,

    "a2": Piece("a2", 1, "P"),
    "b2": Piece("b2", 1, "P"),
    "c2": Piece("c2", 1, "P"),
    "d2": Piece("d2", 1, "P"),
    "e2": Piece("e2", 1, "P"),
    "f2": Piece("f2", 1, "P"),
    "g2": Piece("g2", 1, "P"),
    "h2": Piece("h2", 1, "P"),

    "a1": Piece("a1", 1, "R"),
    "b1": Piece("b1", 1, "N"),
    "c1": Piece("c1", 1, "B"),
    "d1": Piece("d1", 1, "Q"),
    "e1": Piece("e1", 1, "K"),
    "f1": Piece("f1", 1, "B"),
    "g1": Piece("g1", 1, "N"),
    "h1": Piece("h1", 1, "R")
}


turn = 0

while True:
    if turn == 0:
        print("White's piece to move:")
        piece = input(">")
        if piece == "STOP":
            break
        print("White's destination to move:")
        move = input(">")
        makeLegalMove(board[piece], move, board)
        turn = 1
    if turn == 1:
        print("Black's piece to move:")
        piece = input(">")
        print("Black's destination to move:")
        move = input(">")
        makeLegalMove(board[piece], move, board)
        turn = 0

for key, value in board.items():
    if isinstance(value, Piece):
        print(key, ' : ', value)
'''
queen = board["d1"]
#queen.moveToChess("d5", board)
board["e2"].moveToChess("e4", board)
print(queen.isLegalMove("e2", board))
'''
