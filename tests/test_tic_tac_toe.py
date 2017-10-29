import pytest
import numpy as np

from .context import rltictactoe
from rltictactoe import TicTacToe


@pytest.mark.parametrize('params', [
    {
        'board_state': np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]),
        'turn': 1
    },
    {
        'board_state': np.array([
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]),
        'turn': 2
    },
    {
        'board_state': np.array([
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 2]
        ]),
        'turn': 1
    },
    {
        'board_state': np.array([
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 2]
        ]),
        'turn': 2
    }
])
def test_turn(params):
    tic_tac_toe = TicTacToe()

    tic_tac_toe.set_state(params['board_state'])
    assert tic_tac_toe.get_turn() == params['turn']


@pytest.mark.parametrize('params', [
    {
        'board_state': np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]),
        'move_x': 0,
        'move_y': 0,
        'new_board_state': np.array([
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
    },
    {
        'board_state': np.array([
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]),
        'move_x': 0,
        'move_y': 1,
        'new_board_state': np.array([
            [1, 0, 0],
            [2, 0, 0],
            [0, 0, 0]
        ])
    },
    {
        'board_state': np.array([
            [1, 0, 0],
            [2, 0, 0],
            [0, 0, 0]
        ]),
        'move_x': 1,
        'move_y': 1,
        'new_board_state': np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 0, 0]
        ])
    },
    {
        'board_state': np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 0, 0]
        ]),
        'move_x': 1,
        'move_y': 2,
        'new_board_state': np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 2, 0]
        ])
    },
    {
        'board_state': np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 2, 0]
        ]),
        'move_x': 2,
        'move_y': 2,
        'new_board_state': np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 2, 1]
        ])
    }
])
def test_move(params):
    tic_tac_toe = TicTacToe()

    tic_tac_toe.set_state(params['board_state'])

    np.testing.assert_array_equal(
        tic_tac_toe.make_move(params['move_x'], params['move_y']),
        params['new_board_state']
    )


@pytest.mark.parametrize('params', [
    {
        'board_state': np.array([
            [1, 2, 1],
            [2, 1, 2],
            [2, 1, 1]
        ]),
        'is_finished': 3
    },
    {
        'board_state': np.array([
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 2]
        ]),
        'is_finished': 0
    },
    {
        'board_state': np.array([
            [0, 1, 0],
            [0, 1, 2],
            [0, 1, 2]
        ]),
        'is_finished': 1
    },
    {
        'board_state': np.array([
            [0, 1, 2],
            [0, 1, 2],
            [1, 0, 2]
        ]),
        'is_finished': 2
    },
    {
        'board_state': np.array([
            [1, 1, 1],
            [2, 2, 0],
            [0, 0, 0]
        ]),
        'is_finished': 1
    },
    {
        'board_state': np.array([
            [1, 1, 0],
            [2, 2, 2],
            [0, 0, 1]
        ]),
        'is_finished': 2
    },
    {
        'board_state': np.array([
            [1, 2, 2],
            [0, 1, 0],
            [0, 0, 1]
        ]),
        'is_finished': 1
    },
    {
        'board_state': np.array([
            [1, 2, 2],
            [1, 2, 1],
            [2, 0, 1]
        ]),
        'is_finished': 2
    },
    {
        'board_state': np.array([
            [2, 2, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]),
        'is_finished': 1
    },
    {
        'board_state': np.array([
            [2, 2, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]),
        'is_finished': 1
    },
    {
        'board_state': np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 2, 1]
        ]),
        'is_finished': 1
    },
    {
        'board_state': np.array([
            [1, 1, 1, 1],
            [2, 0, 0, 0],
            [2, 0, 2, 0],
            [0, 0, 0, 0]
        ]),
        'is_finished': 1
    }
])
def test_is_finished(params):
    tic_tac_toe = TicTacToe()

    tic_tac_toe.set_state(params['board_state'])
    assert tic_tac_toe.is_finished() == params['is_finished']


@pytest.mark.parametrize('params', [
    {'position': 8, 'xy': (2, 2)},
    {'position': 0, 'xy': (0, 0)},
    {'position': 1, 'xy': (1, 0)},
    {'position': 2, 'xy': (2, 0)},
    {'position': 3, 'xy': (0, 1)},
    {'position': 4, 'xy': (1, 1)}
])
def test_position_translation(params):
    tic_tac_toe = TicTacToe()

    assert TicTacToe.translate_position_to_xy(params['position']) == params['xy']
