import chess
import random 

class game:
    def __init__(self, human_players=1, ):
        if human_players >=1:
             self.player_list = []
             self.player_list.append(input("please enter your name:"))
        
        order = random.randint(1,2)
        pass
    def get_move(self):
        pass

    def eval_gamestate(self):
        pass