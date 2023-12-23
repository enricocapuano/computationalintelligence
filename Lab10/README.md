# Lab 10 of Computational Intelligence

For this lab I collaborated with Minh Triet Ngo (s309062)

The class TicTacToe defines the functioning of the game itself, giving a good print of the playing table.
Moreover, it has methods to define a move and to check when the game is over and who is the winner. 

In the context of Reinforcement Learning, we implememted a Q-Learning agent, based on a Q table that gathers the Q values for all the moves that an agent may do.
The Q Agent is trained to choose the best move, according to this table. Depending on which player is playing (X or O), the Q Agent performs different actions: X gets positive reward, while O negative.

For each agent, the winning rate is computed as the number of winning games over the number of total games.

Moreover, we implemented the method "play_vs_agent" to play TicTacToe ourselves against an agent (that could be the trained one or the random one).
