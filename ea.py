import random
import numpy as np

from Classes.Population import Population
from Classes.TournamentSelection import TournamentSelection
from Classes.Crossover import Crossover
from Classes.Mutation import Mutation


def create_distance_matrix(vertexes: list) -> np.ndarray:
    """
    Function to create distance matrix from XML data
    :param vertexes: list
    :return: ndarray
    """
    cities_matrix = []
    for index, vertex in enumerate(vertexes):
        city = list(map(lambda edge: float(edge['@cost']), vertex['edge']))
        city.insert(index, 0)
        cities_matrix.append(city)
    return np.array(cities_matrix)


def init_population(
        cities: np.ndarray,
        distance_matrix: np.ndarray,
        n_pop: int,
        seed: int
) -> Population:
    """
    Function to generate initial population
    :param cities: ndarray
    :param distance_matrix: ndarray
    :param n_pop: int
    :param seed: int
    :return: Population
    """
    # Set random seed
    np.random.seed(seed)
    return Population(
        np.array([np.random.permutation(cities) for _ in range(n_pop)]),
        distance_matrix
    )


def parent_selection(
        population: np.ndarray,
        distance_matrix: np.ndarray,
        tour_selection_size: int
) -> tuple[np.ndarray, np.ndarray]:
    """
    Function to generate parent solutions using tournament selection
    :param population: ndarray
    :param distance_matrix: ndarray
    :param tour_selection_size: int
    :return: parent1, parent2: tuple[ndarray, ndarray]
    """
    tour_selection = TournamentSelection(population, distance_matrix)
    parent1, parent2 = tour_selection.parents_selection(tour_selection_size)
    return parent1, parent2


def crossover(
        parent1: np.ndarray,
        parent2: np.ndarray,
        crossover_rate: float,
) -> Crossover:
    """
    Function to generate two child solutions using single-point crossover
    :param parent1: ndarray
    :param parent2: ndarray
    :param crossover_rate: float
    :return: child1, child2: tuple[ndarray, ndarray]
    """
    return Crossover(parent1, parent2, crossover_rate)


def mutation(
        child1: np.ndarray,
        child2: np.ndarray,
        mutation_rate: float,
) -> Mutation:
    """
    Function to perform swap mutation
    :param child1: ndarray
    :param child2: ndarray
    :param mutation_rate: float
    :return: mutated_child1, mutated_child2: tuple[ndarray, ndarray]
    """
    return Mutation(child1, child2, mutation_rate)
