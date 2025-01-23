from flask import Flask, request, jsonify
from tictactoe import TicTacToe
from main import minimax_with_alpha_beta
import math

app = Flask(__name__)
games = {}


@app.route('/start', methods=['POST'])
def start_game():
    game_id = len(games) + 1
    games[game_id] = TicTacToe()
    return jsonify({'message:': "game started", 'game_id': game_id, 'board': games[game_id].board})

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    game_id = data['game_id']
    square = data['square']
    letter = data['letter']

    game = games.get(game_id)
    if not game:
        return jsonify({'error': 'Invalid game ID'}), 404

    if game.make_move(square, letter):
        winner = game.current_winner
        board = game.board
        if winner:
            return jsonify({'message': f'{letter} wins!', 'board': board})
        elif not game.empty_squares_available():
            return jsonify({'message': 'It\'s a draw!', 'board': board})
        else:
            return jsonify({'message': 'Move accepted', 'board': board})
    else:
        return jsonify({'error': 'Invalid move'}), 400

@app.route('/ai-move', methods=['POST'])
def ai_move():
    data = request.json
    game_id = data['game_id']
    ai_player = data.get('ai_player', 'O')

    game = games.get(game_id)
    if not game:
        return jsonify({'error': 'Invalid game ID'}), 404

    if not game.empty_squares_available():
        return jsonify({'message': 'No moves left', 'board': game.board})

    move = minimax_with_alpha_beta(game, len(game.available_moves()), -math.inf, math.inf, True, ai_player)['position']
    if move is not None:
        game.make_move(move, ai_player)
        winner = game.current_winner
        if winner:
            return jsonify({'message': f'{ai_player} wins!', 'board': game.board})
        elif not game.empty_squares_available():
            return jsonify({'message': 'It\'s a draw!', 'board': game.board})
        else:
            return jsonify({'message': 'AI move made', 'board': game.board})
    else:
        return jsonify({'message': 'Game over', 'board': game.board})

if __name__ == '__main__':
    app.run(debug=True)