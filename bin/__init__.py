import sys
import os
from ale_py.env import gym as ale_gym

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Patch to allow rendering Atari games.
# The AtariEnv's render method expects the mode to be in self._render_mode
# (usually initialized with env.make) instead of taking mode as a param.
_original_atari_render = ale_gym.AtariEnv.render


def atari_render(self, mode='rgb_array'):
    original_render_mode = self._render_mode
    try:
        self._render_mode = mode
        return _original_atari_render(self)
    finally:
        self._render_mode = original_render_mode


ale_gym.AtariEnv.render = atari_render
