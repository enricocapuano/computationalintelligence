import numpy as np
import random

# Create the Tic Tac Toe environment
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing the Tic Tac Toe board
        self.current_player = 'X'  # Player 'X' starts the game
        self.winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
    
    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
        print('---------')
    
    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']
    
    def make_move(self, position):
        
        #print(position)
        self.board[position] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        for combo in self.winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and (self.board[combo[0]] != ' '):
                return self.board[combo[0]]
        return None
    
    def game_over(self):
        return self.check_winner() or ' ' not in self.board
    
    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

# Q-Learning agent to play Tic Tac Toe
class QLearningAgent:
    def __init__(self, epsilon=0.3, alpha=0.1, gamma=0.9):
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.q_table = {}  # Q-table to store state-action values
        
    
    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)
    
    def update_q_value(self, state, action, reward, next_state):
        old_value = self.get_q_value(state, action)
        #print(self.env.available_moves())
        best_next_action = max([self.get_q_value(next_state, a) for a in env.available_moves()])
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * best_next_action)
        self.q_table[(state, action)] = new_value
    
    def choose_action(self, state, available_moves):
        #print(available_moves)
        if random.uniform(0, 1) < self.epsilon:
            #print(random.choice(available_moves))
            #print("minore")
            return int(random.choice(available_moves))
        else:
            #print("maggiore")
            #print(max([self.get_q_value(state, a) for a in env.available_moves()]))
            return max(available_moves, key=lambda a: self.get_q_value(state, a))
            

# Training the agent
def train_agent(episodes):
    env = TicTacToe()
    agent = QLearningAgent()
    
    #agent.env = env
    
    for episode in range(episodes):
        env.reset()
        state = tuple(env.board)
        
        while not env.game_over():
            available_moves = env.available_moves()
            action = agent.choose_action(state, available_moves)
            #print(action)
            next_state = list(state)
            env.make_move(action)
            next_state = tuple(env.board)
            
            if env.check_winner() == 'X':
                reward = 1
            elif env.check_winner() == 'O':
                reward = -1
            else:
                reward = 0
            
            agent.update_q_value(state, action, reward, next_state)
            state = next_state
    
    return agent

# Playing against the trained agent
def play_vs_agent(agent):
    #env = TicTacToe()
    state = tuple(env.board)
    
    while not env.game_over():
        if env.current_player == 'X':
            env.print_board()
            print("Your turn! Choose a position (0-8):")
            while True:
                try:
                    user_move = int(input())
                    if user_move in env.available_moves():
                        break
                    else:
                        print("Invalid move! Choose an available position.")
                except ValueError:
                    print("Invalid input! Enter a number.")
            env.make_move(user_move)
        else:
            available_moves = env.available_moves()
            action = agent.choose_action(state, available_moves)
            env.make_move(action)
        
        state = tuple(env.board)
    
    env.print_board()
    winner = env.check_winner()
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")




if __name__ == "__main__":
    # Train the agent and play against it
    env = TicTacToe()
    trained_agent = train_agent(episodes=10000)
    play_vs_agent(trained_agent)