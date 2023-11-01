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
        self.best_sol = None

    def fitness(self, chromosome):
        """
        Method to calculate distance for each individual solution
        :param chromosome: ndarray
        :return: sum of the distance
        """
        return sum(
            [
                self.distance_matrix[chromosome[i], chromosome[i + 1]] for i in range(len(chromosome) - 1)
            ] + self.distance_matrix[chromosome[-1], chromosome[0]]
        )

    def evaluate(self):
        """
        Method to determine the best solution from the initial population
        :return: None
        """
        distances = np.array(
            [self.fitness(chromosome - 1) for chromosome in self.population]
        )
        self.score = np.min(distances)
        self.best_sol = self.population[distances.tolist().index(self.score)]

