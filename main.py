#Computer Science Club Members code here - Time to write the AI!
import chess
from random import randint
import sys

board = chess.Board()
sim_board = chess.Board()
color = True

while True:
    select_color = input("What color am I playing? 1 for white, 2 for black. ")
    if select_color == "1":
        color = True
        break
    elif select_color == "2":
        color = False
        break
    else:
        print("Please input a valid response.")

while not board.is_game_over():
    if color == board.turn:
        #sets up simulated board
        sim_board = board.copy()
        legal_moves = list(sim_board.legal_moves)
        
        #variable initialization
        white_position = 0
        black_position = 0
        
        #determines current point totals for each side
        for piece in board.pieces(chess.PAWN, chess.WHITE):
            white_position += 10
        for piece in board.pieces(chess.KNIGHT, chess.WHITE):
            white_position += 30
        for piece in board.pieces(chess.BISHOP, chess.WHITE):
            white_position += 30
        for piece in board.pieces(chess.ROOK, chess.WHITE):
            white_position += 50
        for piece in board.pieces(chess.QUEEN, chess.WHITE):
            white_position += 90
        for piece in board.pieces(chess.KING, chess.WHITE):
            white_position += 900
        
        for piece in board.pieces(chess.PAWN, chess.BLACK):
            black_position += 10
        for piece in board.pieces(chess.KNIGHT, chess.BLACK):
            black_position += 30
        for piece in board.pieces(chess.BISHOP, chess.BLACK):
            black_position += 30
        for piece in board.pieces(chess.ROOK, chess.BLACK):
            black_position += 50
        for piece in board.pieces(chess.QUEEN, chess.BLACK):
            black_position += 90
        for piece in board.pieces(chess.KING, chess.BLACK):
            black_position += 900
        
        print("WP: " + str(white_position) + " BP: " + str(black_position)) #debug print statement

        #sets max difference to minimum so that the algo works
        max_diff = -9999999

        #gets current point difference to compare against later
        if color == chess.WHITE:
            current_diff = white_position - black_position
        else:
            current_diff = black_position - white_position
        
        #constants for current 'real' board position
        current_white = white_position
        current_black = black_position

        #simulates every legal move
        for sim_move in legal_moves:

            #resets point positions to where they are currently
            white_position = current_white
            black_position = current_black

            #adds points for checking
            if color == chess.WHITE:
                if sim_board.gives_check(sim_move):
                    white_position += 100
            else:
                if sim_board.gives_check(sim_move):
                    black_position += 100

            #calculates new board positions based on simulated move
            sim_board.push_uci(str(sim_move))
            for piece in sim_board.pieces(chess.PAWN, chess.WHITE):
                white_position += 10
            for piece in sim_board.pieces(chess.KNIGHT, chess.WHITE):
                white_position += 30
            for piece in sim_board.pieces(chess.BISHOP, chess.WHITE):
                white_position += 30
            for piece in sim_board.pieces(chess.ROOK, chess.WHITE):
                white_position += 50
            for piece in sim_board.pieces(chess.QUEEN, chess.WHITE):
                white_position += 90
            for piece in sim_board.pieces(chess.KING, chess.WHITE):
                white_position += 900
            
            for piece in sim_board.pieces(chess.PAWN, chess.BLACK):
                black_position += 10
            for piece in sim_board.pieces(chess.KNIGHT, chess.BLACK):
                black_position += 30
            for piece in sim_board.pieces(chess.BISHOP, chess.BLACK):
                black_position += 30
            for piece in sim_board.pieces(chess.ROOK, chess.BLACK):
                black_position += 50
            for piece in sim_board.pieces(chess.QUEEN, chess.BLACK):
                black_position += 90
            for piece in sim_board.pieces(chess.KING, chess.BLACK):
                black_position += 900
            
            #determines new difference in point totals
            if color == chess.WHITE:
                diff = white_position - black_position
            else:
                diff = black_position - white_position
            
            #sees if this is the best move so far
            if diff > max_diff:
                max_diff = diff
                move = sim_move
            
            #resets for next simulation
            sim_board.pop()
            
        #if we can't get a move that changes the point total, just do a random move
        legal_moves = list(board.legal_moves)
        if max_diff == current_diff:
            rand_val = randint(0, len(legal_moves) - 1)
            move = legal_moves[rand_val]

        #finalizes move
        print("My move in UCI notation: " + str(move))
        board.push_uci(str(move))

    else:
        while True:
            try:
                print("Please enter the opponent's move.")
                move = input(">")
                board.push_san(move)
                break
            except:
                if move == "goodbye":
                    sys.exit()
                print("Please enter a valid move in standard algebraic notation.")

