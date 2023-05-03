import numpy as np


class BiasExample:
    def __init__(self, num_actions=10):
        self.num_actions = num_actions
        self.state = "A"

    def reset(self):
        self.state = "A"
        return self.state, {}

    def step(self, action):
        """
        When in state A, we assume that action 1 is 'right' and action 0 is 'left', and these are the only two actions available.
        When in state B, there are `num_actions` available actions, all with the same effect.
        """
        if self.state == "A" and action == 1:
            reward = 0
            terminated = True
            info = {'optimal': True}
        elif self.state == "A" and action == 0:
            self.state = "B"
            reward = 0
            terminated = False
            info = {'optimal': False}
        else:
            terminated = True
            info = {'optimal': False}
            reward = np.random.normal(-0.1, 1)
        return self.state, reward, terminated, False, info
