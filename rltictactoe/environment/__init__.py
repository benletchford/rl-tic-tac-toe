from gym.envs.registration import register
from environment import TicTacToeEnv


# register(
#     id='TicTacToe-v0',
#     entry_point='rltictactoe.environment.environment:TicTacToeEnv',
# )
#
#
# def predict_env_factory(board_state):
#     return TicTacToeEnv(predict_for=board_state)
