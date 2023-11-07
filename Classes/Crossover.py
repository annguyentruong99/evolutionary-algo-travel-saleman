import numpy as np


class Crossover:
    def __init__(self, parent1, parent2):
        self.parent1 = parent1
        self.parent2 = parent2

    def single_point(self):
        rng = np.random.default_rng()
        crossover_point = rng.integers(len(self.parent1))

        child1 = np.append(self.parent1[:crossover_point], self.parent2[crossover_point:])
        child2 = np.append(self.parent2[:crossover_point], self.parent1[crossover_point:])

        return child1, child2

    def multipoint(self):
        pass
