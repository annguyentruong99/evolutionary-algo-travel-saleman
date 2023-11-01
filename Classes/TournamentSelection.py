import numpy as np

from Classes.Population import Population


class TournamentSelection(Population):
    def __init__(self, population, distance_matrix):
        super().__init__(population, distance_matrix)
        self.population = population

    def selection_pool(self, tour_selection_size):
        """
        Method to generate tournament selections pool
        :param tour_selection_size: int
        :return: pool_selections: ndarray
        """
        rng = np.random.default_rng()
        pool_selections = np.array(
            [self.population[rng.integers(len(self.population))] for _ in range(tour_selection_size)]
        )
        return pool_selections

    def parents_selection(self, pool):
        """
        Method to select a best fit solution as a parent from a selection pool
        :param pool: ndarray
        :return: parent: ndarray
        """
        distances = np.array(
            [self.fitness(chromosome - 1) for chromosome in pool]
        )
        best_score = np.min(distances)
        parent = pool[distances.tolist().index(best_score)]
        return parent
