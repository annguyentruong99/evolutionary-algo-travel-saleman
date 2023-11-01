import random
import numpy as np

from Classes.Population import Population
from Classes.TournamentSelection import TournamentSelection

"""
Function to create distance matrix from XML data

    :parameter vertexes (list): list of vertexes
    
    :return cities_matrix (Array): a numpy array of the distance matrix
"""


def create_distance_matrix(vertexes: list) -> object:
    cities_matrix = []
    for index, vertex in enumerate(vertexes):
        city = list(map(lambda edge: float(edge['@cost']), vertex['edge']))
        city.insert(index, 0)
        cities_matrix.append(city)
    return np.array(cities_matrix)


"""
Function to generate initial population

    :parameter cities -> list of cities name
    :parameter distance_matrix -> array of distance vectors
    :parameter n_pop -> number of initial population
    :parameter seed -> random seed
    
    :return Population
"""


def init_population(
        cities: object,
        distance_matrix: object,
        n_pop: int,
        seed: int
) -> Population:
    # Set random seed
    np.random.seed(seed)
    return Population(
        np.array([np.random.permutation(cities) for _ in range(n_pop)]),
        distance_matrix
    )


"""
Function to generate parent solutions using tournament selection

    :parameter population -> array of current population
    
    :return parent1, parent2 -> two selected parents from the selection pool
"""


def parent_selection(population, distance_matrix, tour_selection_size):
    tour_selection = TournamentSelection(population, distance_matrix)
    pool = tour_selection.selection_pool(tour_selection_size)
    parent = tour_selection.parents_selection(pool)
    return parent
