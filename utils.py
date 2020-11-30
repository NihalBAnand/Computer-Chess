#Backend - function definitions
alphas = ["a", "b", "c", "d", "e", "f", "g", "h"]

class Piece:
    def __init__(self, pos, color, unit):
        x = alphas.index(pos[0])
        y = 8 - (int(pos[1]))
        self.position = [x, y]
        self.color = color
        self.unit = unit
    
    def posToChess(self):
        string = ""
        string += alphas[self.position[0]]
        string += str(8 - self.position[1])
        return string
    
    def moveTo(self, x, y):
        self.position[0] = x
        self.position[1] = y
    
    def moveToChess(self, pos, board):
        x = alphas.index(pos[0])
        y = 8 - (int(pos[1]))
        board[self.posToChess()] = None
        self.moveTo(x, y)
        
        board[self.posToChess()] = self
    
    def isLegalMove(self, pos, board):
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
                        return fine
                    else:
                        fine = True
                        for i in range(x, self.position[0]):
                            j = alphas[i]
                            if type(board[j + str(8 - self.position[1])]) != None:
                                if board[j + str(8 - self.position[1])].color == self.color:
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
                        return fine
                    else:
                        fine = True
                        for i in range(y, self.position[1]):
                            j = alphas[x]
                            if type(board[j + str(i)]) != None:
                                if board[j + str(i)].color == self.color:
                                    fine = False
                        return fine



board = {
    "a8": Piece("a8", 0, "R"),
    "b8": Piece("b8", 0, "N"),
    "c8": Piece("c8", 0, "B"),
    "d8": Piece("d8", 0, "Q"),
    "e8": Piece("e8", 0, "K"),
    "f8": Piece("f8", 0, "B"),
    "g8": Piece("g8", 0, "N"),
    "h8": Piece("h8", 0, "R"),

    "a7": Piece("a7", 0, "P"),
    "b7": Piece("b7", 0, "P"),
    "c7": Piece("c7", 0, "P"),
    "d7": Piece("d7", 0, "P"),
    "e7": Piece("e7", 0, "P"),
    "f7": Piece("f7", 0, "P"),
    "g7": Piece("g7", 0, "P"),
    "h7": Piece("h7", 0, "P"),

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

rook = board["a8"]
rook.moveToChess("a6", board)
print(rook.isLegalMove("b7", board))







