from tictactoe import TicTacToe
import math
import random
import time

from tictactoe import TicTacToe


def minimax(board, depth, maximizing_player, ai_player):
    if ai_player == 'X':
        me = 'O'
    else:
        me = 'X'
    
    if board.current_winner == ai_player:
        if board.num_empty_squares() >= 3:
            return {'value': 5, 'position': None}
        return {'value': 1, 'position': None}
    elif board.current_winner is None and not board.empty_squares_available():
        return {'value': 0, 'position': None}
    elif board.current_winner == me:
        if board.num_empty_squares() >= 3:
            return {'value': -5, 'position': None}
        return {'value': -1, 'position': None}

    
    
    if maximizing_player:
        max_value = {'value': -math.inf, 'position': None}
        
        for move in board.available_moves():
            board.make_move(move, ai_player)
            comp = minimax(board, depth - 1, False, ai_player)['value']
            board.board[move] = ' '
            board.current_winner = None
            if comp > max_value['value']:
                max_value['value'] = comp
                max_value['position'] = move
        return max_value
             
    else:
        min_value = {'value': math.inf, 'position': None}
        
        for move in board.available_moves():
            board.make_move(move, me)
            comp = minimax(board, depth - 1, True, ai_player)['value']
            board.board[move] = ' '
            board.current_winner = None
            if comp < min_value['value']:
                min_value['value'] = comp
                min_value['position'] = move

        return min_value

def minimax_with_alpha_beta(board, depth, alpha, beta, maximizing_player, ai_player):
    if ai_player == 'X':
        me = 'O'
    else:
        me = 'X'
    
    if board.current_winner == ai_player:
        return {'value': 1, 'position': None}
    elif board.current_winner is None and not board.empty_squares_available():
        return {'value': 0, 'position': None}
    elif board.current_winner == me:
        return {'value': -1, 'position': None}
    
    if maximizing_player:
        max_value = {'value': -math.inf, 'position': None}
        
        for move in board.available_moves():
            board.make_move(move, ai_player)
            comp = minimax(board, depth - 1, False, ai_player)['value']
            board.board[move] = ' '
            board.current_winner = None
            if comp > max_value['value']:
                max_value['value'] = comp
                max_value['position'] = move
                
            alpha = max(alpha, comp)
            if beta <= alpha:
                break
        return max_value
             
    else:
        min_value = {'value': math.inf, 'position': None}
        
        for move in board.available_moves():
            board.make_move(move, me)
            comp = minimax(board, depth - 1, True, ai_player)['value']
            board.board[move] = ' '
            board.current_winner = None
            if comp < min_value['value']:
                min_value['value'] = comp
                min_value['position'] = move
            
            beta = min(beta, comp)
            if beta <= alpha:
                break

        return min_value

def play_game_human_moves_first():

    game = TicTacToe()
    print("\nInitial Board:")
    game.print_board()

    letter = 'X'  # Human player starts first.
    while game.empty_squares_available():
        if letter == 'O':  # AI's turn
            square = minimax_with_alpha_beta(game, len(game.available_moves()), -math.inf, math.inf, True, 'O')['position']
            if square is None:
                print("\nGame is a draw!")
                break
            game.make_move(square, letter)
            print(f"\nAI (O) chooses square {square + 1}")
        else:
            valid_square = False
            while not valid_square:
                square = input(f"\n{letter}'s turn. Input move (1-9): ")
                try:
                    square = int(square) - 1
                    if square not in game.available_moves():
                        raise ValueError
                    valid_square = True
                    game.make_move(square, letter)
                except ValueError:
                    print("\nInvalid square. Try again.")

        game.print_board()

        if game.current_winner:
            print(f"\n{letter} wins!")
            break

        letter = 'O' if letter == 'X' else 'X'  # Switch turns.
    else:
        print("\nIt's a draw!")

def play_game_ai_moves_first():

    game = TicTacToe()
    print("\nInitial Board:")
    game.print_board()

    first_move = True

    letter = 'O'  # AI player starts first.
    while game.empty_squares_available():
        if letter == 'O':  # AI's turn
            if first_move:
                square = random.randint(0, 8)
                first_move = False
            else:
                square = minimax_with_alpha_beta(game, len(game.available_moves()), -math.inf, math.inf, True, 'O')['position']
            if square is None:
                print("\nGame is a draw!")
                break
            game.make_move(square, letter)
            print(f"\nAI (O) chooses square {square + 1}")
        else:
            valid_square = False
            while not valid_square:
                square = input(f"\n{letter}'s turn. Input move (1-9): ")
                try:
                    square = int(square) - 1
                    if square not in game.available_moves():
                        raise ValueError
                    valid_square = True
                    game.make_move(square, letter)
                except ValueError:
                    print("\nInvalid square. Try again.")

        game.print_board()

        if game.current_winner:
            print(f"\n{letter} wins!")
            break

        letter = 'O' if letter == 'X' else 'X'  # Switch turns.
    else:
        print("\nIt's a draw!")

def play_game_human_vs_human():

    game = TicTacToe()
    print("\nInitial Board:")
    game.print_board()

    letter = 'O'  # Human (O) player starts first.
    while game.empty_squares_available():
        if letter == 'O':  # Human (O)'s turn
            valid_square = False
            while not valid_square:
                square = input(f"\n{letter}'s turn. Input move (1-9): ")
                try:
                    square = int(square) - 1
                    if square not in game.available_moves():
                        raise ValueError
                    valid_square = True
                    game.make_move(square, letter)
                except ValueError:
                    print("\nInvalid square. Try again.")

                if square is None:
                    print("\nGame is a draw!")
                    break
                game.make_move(square, letter)
                print(f"\nAI (O) chooses square {square + 1}")
        else:
            valid_square = False
            while not valid_square:
                square = input(f"\n{letter}'s turn. Input move (1-9): ")
                try:
                    square = int(square) - 1
                    if square not in game.available_moves():
                        raise ValueError
                    valid_square = True
                    game.make_move(square, letter)
                except ValueError:
                    print("\nInvalid square. Try again.")

        game.print_board()

        if game.current_winner:
            print(f"\n{letter} wins!")
            break

        letter = 'O' if letter == 'X' else 'X'  # Switch turns.
    else:
        print("\nIt's a draw!")

def play_game_ai_vs_ai():

    game = TicTacToe()
    print("\nInitial Board:")
    game.print_board()

    first_move = True

    letter = 'O'  # AI (O) player starts first.
    while game.empty_squares_available():
        if letter == 'O':  # AI (O)'s turn
            if first_move:
                square = random.randint(0, 8)
                first_move = False
            else:
                square = minimax_with_alpha_beta(game, len(game.available_moves()), -math.inf, math.inf, True, 'O')['position']
            if square is None:
                print("\nGame is a draw!")
                break
            game.make_move(square, letter)
            print(f"\nAI (O) chooses square {square + 1}")
            time.sleep(0.75)
        else:
            square = minimax_with_alpha_beta(game, len(game.available_moves()), -math.inf, math.inf, True, 'O')['position']
            if square is None:
                print("\nGame is a draw!")
                break
            game.make_move(square, letter)
            print(f"\nAI (X) chooses square {square + 1}")
            time.sleep(0.75)

        game.print_board()

        if game.current_winner:
            print(f"\n{letter} wins!")
            break

        letter = 'O' if letter == 'X' else 'X'  # Switch turns.
    else:
        print("\nIt's a draw!")


if __name__ == '__main__':

    print("""
Modes of play available:

    hh: Hooman vs. hooman
    ha: Hooman vs. AI
    ah: AI vs. Hooman - AI makes first move
    aa: AI vs. AI""")

    valid_move = False
    while not valid_move:
        mode = input("\nEnter preferred mode of play (e.g., aa): ")
        try:
            if mode not in ["hh", "ha", "ah", "aa"]:
                raise ValueError
            valid_move = True
            if mode == "hh":
                play_game_human_vs_human()
            elif mode == "ha":
                play_game_human_moves_first()
            elif mode == "ah":
                play_game_ai_moves_first()
            else:
                play_game_ai_vs_ai()
        except ValueError:
            print("\nInvalid option entered. Try again.")

