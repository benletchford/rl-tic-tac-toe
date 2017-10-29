from gym.envs.registration import register


register(
    id='TicTacToe-v0',
    entry_point='environment:environment:Environment',
)
