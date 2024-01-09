import random
from collections import defaultdict
from game import Game, Move, Player

class QPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        #from_pos = (random.randint(0, 4), random.randint(0, 4))
        #move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        #return from_pos, move
        pass

class Environment:
    def __init__(self):
        self.game = Game()
        self.board = self.game._board  # Representing the Tic Tac Toe board
        self.current_player = 'X'  # Player 'X' starts the game
    
    def print_board(self):
        self.game.print()
    
    def available_moves(self, board = None):
        pass

    def make_move(self, position):
        pass
    
    def check_winner(self):
        pass
    
    def game_over(self):
        return self.check_winner() or ' ' not in self.board
    
    def reset(self):
        pass

class QLearningAgent:
    def __init__(self, epsilon, alpha=0.5, gamma=0.1):
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.q_table = defaultdict(float)  # Q-table to store state-action values
        self.env = None
    
    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)
    
    def update_q_value(self, state, action, reward, next_state, player):
        if player == 'X':
            old_value = self.get_q_value(state, action)
            l = [self.get_q_value(next_state, a) for a in self.env.available_moves(next_state)]
            if len(l) > 0:
                best_next_action = max([self.get_q_value(next_state, a) for a in self.env.available_moves(next_state)])
            else:
                best_next_action = 0
            new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * best_next_action)
            self.q_table[(state, action)] = new_value
        else:
            old_value = self.get_q_value(state, action)
            l = [self.get_q_value(next_state, a) for a in self.env.available_moves(next_state)]
            if len(l) > 0:
                best_next_action = min([self.get_q_value(next_state, a) for a in self.env.available_moves(next_state)])
            else:
                best_next_action = 0
            new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * best_next_action)
            self.q_table[(state, action)] = new_value

    def choose_action(self, state, available_moves,play_as = None, playing = False):
        if not playing: #training
            if random.uniform(0, 1) < self.epsilon.get():
                return random.choice(available_moves)
            else:
                return max(available_moves, key=lambda a: self.get_q_value(state, a))
        else:
            if play_as == 'X':
                return max(available_moves, key=lambda a: self.get_q_value(state, a))
            else:
                return min(available_moves, key=lambda a: self.get_q_value(state, a))