import numpy as np


class TicTacToe:

    def __init__(self):
        self.board_state = None

    def set_state(self, new_state):
        """ 2d array of cell positions of the board. 0 = cell not occupied,
            1 = cross occupies cell, 2 = nought occupies cell.
            Example: [
                [0, 0, 1],
                [0, 0, 2],
                [0, 0, 0]
            ] """

        new_state = np.array(new_state)

        assert new_state.shape == (len(new_state), len(new_state))

        self.board_state = new_state

        return self.board_state

    def is_finished(self):
        """ 0 = not finished, 1 = cross win, 2 = nought win, 3 = tie """

        # Are we tied?
        if self.board_state.flatten().tolist().count(0) == 0:
            return 3

        # Stolen: https://codereview.stackexchange.com/a/24775
        positions_groups = (
            [[(x, y) for y in range(self.get_board_size())] for x in range(self.get_board_size())] +  # horizontals
            [[(x, y) for x in range(self.get_board_size())] for y in range(self.get_board_size())] +  # verticals
            [[(d, d) for d in range(self.get_board_size())]] +  # diagonal from top-left to bottom-right
            [[(2-d, d) for d in range(self.get_board_size())]]  # diagonal from top-right to bottom-left
        )
        for positions in positions_groups:
            values = [self.board_state[x][y] for (x, y) in positions]
            if len(set(values)) == 1 and values[0]:
                return values[0]

        # Game isn't finished
        return 0

    def get_board_size(self):
        return len(self.board_state)

    def get_turn(self):
        """ Returns 1 for crosses turn, 2 for noughts turn """

        flattened_list = self.board_state.flatten().tolist()

        if flattened_list.count(1) > flattened_list.count(2):
            return 2
        else:
            return 1

    def make_move(self, x, y):
        """ Updates the state with the requested new occupied cell """

        # Sanity check
        assert x < self.get_board_size() and y < self.get_board_size()
        assert self.board_state[x][y] == 0
        assert self.is_finished() == 0

        new_state = self.board_state.copy()
        new_state[y][x] = self.get_turn()

        return self.set_state(new_state)
