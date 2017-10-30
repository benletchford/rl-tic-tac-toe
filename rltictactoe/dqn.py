import sys
import os

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import Callback

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rltictactoe import environment
from rltictactoe.environment import TicTacToeEnv


def predict(board_state, model_path):
    env = TicTacToeEnv(predict_for=board_state)

    dqn = build_dqn(env)

    dqn.load_weights(model_path)

    dqn.test(env, nb_episodes=1, visualize=False, verbose=0)

    return dqn.recent_action


def build_dqn(env):
    nb_actions = env.action_space.n

    model = Sequential()
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(nb_actions, activation='linear'))

    memory = SequentialMemory(limit=5000000, window_length=1)
    policy = BoltzmannQPolicy()
    log_interval = 10000

    dqn = DQNAgent(
        model=model,
        nb_actions=nb_actions,
        memory=memory,
        nb_steps_warmup=1000,
        enable_dueling_network=False,
        target_model_update=1e-2,
        policy=policy
    )

    dqn.compile(Adam(lr=1e-5), metrics=['accuracy', 'mae'])

    return dqn
