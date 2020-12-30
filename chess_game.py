import chess
import sys
import chess.engine
from stockfish import Stockfish
import random 

class game:
    def __init__(self, human_players=[], bot_locale=None ):
        self.board = chess.Board()
        self.player_list = []
        self.suport_bot_play = False
        if human_players:
            for player in human_players:
                self.player_list.append(player)
        if bot_locale:
            self.suport_bot_play = True    
            self.bot = Stockfish() 
        
        order = random.randint(1,2)
        
    def get_move(self, dificulty=1):
        if self.suport_bot_play:
            self.bot.set_fen_position(self.board.fen())
            result = self.bot.get_best_move_time(time=100)
            return result
        
        return False

    def push_move(self, movestr):
        movesquares = movestr.split()
        if len(movesquares) == 1:
            self.board.push(chess.Move.from_uci(movesquares[0]))
            self.bot.set_fen_position( self.board.fen())
            
    
    def _push_move(self, origin_square, destination_square):
        start = chess.parse_square(origin_square)
        end = chess.parse_square(destination_square)
        pass

    def display_gameState(self):
        print (self.bot.get_board_visual())

    def is_valid(self, ucimove):
        candidate_move = chess.Move.from_uci(ucimove)
        if candidate_move in self.board.legal_moves:
            self.board.push(candidate_move)
            if not self.board.is_valid():
                self.board.pop()
                return False
            else:
                self.board.pop()
                return True
    
    
    def is_over(self):
        return self.board.is_game_over()
    def eval_gamestate(self):
        pass