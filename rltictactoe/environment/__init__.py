from gym.envs.registration import register


register(
    id='TicTacToe-v0',
    entry_point='rltictactoe.environment.environment:TicTacToeEnv',
)
