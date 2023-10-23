import numpy as np


class Population:
    def __init__(self, population, distance_matrix):
        """
        :type population: ndarray
        :type distance_matrix: ndarray
        """
        self.population = population
        self.distance_matrix = distance_matrix
        self.parents = []
        self.score = 0
        self.best = None

    def fitness(self, chromosome):
        return sum(
            [
                self.distance_matrix[chromosome[i], chromosome[i + 1]] for i in range(len(chromosome) - 1)
            ]
        )
