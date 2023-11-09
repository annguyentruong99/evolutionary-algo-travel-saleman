import random
import numpy as np

from Classes.Population import Population
from Classes.TournamentSelection import TournamentSelection
from Classes.Crossover import Crossover

"""
Function to create distance matrix from XML data

    :parameter vertexes (list): list of vertexes
    
    :return cities_matrix (Array): a numpy array of the distance matrix
"""


def create_distance_matrix(vertexes: list) -> np.ndarray:
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
        cities: np.ndarray,
        distance_matrix: np.ndarray,
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
    
    :return parent -> selected parent from the selection pool
"""


def parent_selection(
        population: np.ndarray,
        distance_matrix: np.ndarray,
        tour_selection_size: int
) -> np.ndarray:
    tour_selection = TournamentSelection(population, distance_matrix)
    pool = tour_selection.selection_pool(tour_selection_size)
    parent = tour_selection.parents_selection(pool)
    return parent


"""
Function to generate two child solutions using single-point crossover

    :parameter parent1 -> parent 1 array
    :parameter parent1 -> parent 1 array
    
    :return child1, child2 -> two children generated
"""


def single_point_crossover(parent1: object, parent2: object) -> object:
    crossover = Crossover(parent1, parent2)

    child1, child2 = crossover.single_point()

    return child1, child2
