import chess
import sys
import chess_game
import chess.engine
from stockfish import Stockfish


    
num_players = input("how many players?"+ 
"(1 = human vs ai, 2 = human vs human, 0 = ai vs ai ) ")
human_players = list()
if int(num_players) < 2:
    path_to_bot = str(sys.argv)
for player in range(int(num_players)):
    human_players.append(input("please enter your name:"))
game = chess_game.game(bot_locale=True)
game.display_gameState()

bot_to_move = False
while not game.is_over():
    
    if human_players and not bot_to_move:
        user_move = input("please enter your move in uci form: eg e2e4\n")
        if user_move == "-q":
            break
        if game.is_valid(user_move):
            game.push_move(user_move)
            bot_to_move = True 
        else:
            print( 'Move not valid try again.')
            bot_to_move = False
    if int(num_players) <= 1:
        if bot_to_move:
            bot_move = game.get_move()
            if bot_move:
                game.board.push_san(bot_move)
                game.bot.set_fen_position(game.board.fen())
        if int(num_players) == 1:
            bot_to_move = False
    game.display_gameState()
print ("good game")
"""engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
print(board)
engine.quit()"""
#bob = cb.bot()
#bob.display()
    