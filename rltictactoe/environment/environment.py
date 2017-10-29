import numpy as np

import gym
from gym.spaces import Discrete, Box

from rltictactoe import TicTacToe


class TicTacToeEnv(gym.Env):
    action_space = Discrete(3**2)

    def __init__(self, board_size=3):
        self.board_size = board_size

        self.observation_space = Box(
            low=np.array([0 for cell in range(self.board_size ** 2)]),
            high=np.array([2 for cell in range(self.board_size ** 2)])
        )

    def reset(self):
        self.tictactoe = TicTacToe()
        self.tictactoe.set_state([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
        move = self._get_random_move()

        self.tictactoe.make_move(move[0], move[1])

        return self.tictactoe.board_state.flatten()

    def step(self, action):
        translated_action = TicTacToe.translate_position_to_xy(action)

        try:
            self.tictactoe.make_move(translated_action[0], translated_action[1])

        except AssertionError:
            return self.tictactoe.board_state.flatten(), -1, True, {}

        reward = 0
        done = False
        winner = self.tictactoe.is_finished()
        if winner == 0:
            move = self._get_random_move()
            self.tictactoe.make_move(move[0], move[1])

            next_winner = self.tictactoe.is_finished()
            if next_winner == 1:
                reward = -1
                done = True
            elif next_winner == 3:
                reward = 0
                done = True

        elif winner == 2:
            reward = 1
            done = True

        elif winner == 3:
            reward = 0
            done = True

        return self.tictactoe.board_state.flatten(), reward, done, {}

    def _get_random_move(self):
        assert self.tictactoe.is_finished() == 0

        positions = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.tictactoe.board_state[y][x] == 0:
                    positions.append((x, y))

        return positions[np.random.choice(len(positions), 1)[0]]
