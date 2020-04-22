import numpy as np


class Mastermind(object):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        self.colors = ['RED', 'GREEN', 'BLUE', 'CYAN', 'MAGENTA', 'YELLOW']
        self.tries = 0
        self.code = []
        for i in range(0, 4):
            self.code = np.random.choice(self.colors, 4)

    def check_input(self):
        pass

    def solve_mystery(self):
        return self.colors


