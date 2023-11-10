import random
import numpy as np

from Classes.Population import Population
from Classes.TournamentSelection import TournamentSelection
from Classes.Crossover import Crossover
from Classes.Mutation import Mutation

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
) -> tuple[np.ndarray, np.ndarray]:
    tour_selection = TournamentSelection(population, distance_matrix)
    parent1, parent2 = tour_selection.parents_selection(tour_selection_size)
    return parent1, parent2


"""
Function to generate two child solutions using single-point crossover

    :parameter parent1 -> parent 1 array
    :parameter parent1 -> parent 1 array
    
    :return child1, child2 -> two children generated
"""


def single_point_crossover(
        parent1: np.ndarray,
        parent2: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    crossover = Crossover(parent1, parent2)

    child1, child2 = crossover.single_point()

    return child1, child2


def swap_mutation(child1: np.ndarray, child2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mutation = Mutation(child1, child2)
    mutated_child1, mutated_child2 = mutation.swap_mutation()
    return mutated_child1, mutated_child2