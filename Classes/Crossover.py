import numpy as np
from utils import contains_duplicates, find_duplicate_indexes


class Crossover:
    def __init__(self, parent1, parent2):
        self.parent1 = parent1
        self.parent2 = parent2

    @staticmethod
    def fix_child(child, parent):
        first_duplicate_ind, second_duplicate_ind = find_duplicate_indexes(child)
        city_to_swap = parent[second_duplicate_ind]
        child[first_duplicate_ind] = city_to_swap
        return child

    def single_point(self):
        """
        Method to generate 2 different children by single-point crossover
        :return: child1, child2: ndarray, ndarray
        """
        rng = np.random.default_rng()
        crossover_point = rng.integers(1, len(self.parent1) - 1)

        child1 = np.append(self.parent1[:crossover_point], self.parent2[crossover_point:])
        child2 = np.append(self.parent2[:crossover_point], self.parent1[crossover_point:])

        if contains_duplicates(child1) and contains_duplicates(child2):
            fixed_child1 = self.fix_child(child1, self.parent1)
            fixed_child2 = self.fix_child(child2, self.parent2)

            return fixed_child1, fixed_child2

        return child1, child2
