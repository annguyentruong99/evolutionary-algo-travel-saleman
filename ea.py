import random
import numpy as np

from Classes.Population import Population

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
        cities: list,
        distance_matrix: object,
        n_pop: int,
        seed: int
) -> Population:
    np.random.seed(seed)
    return Population(
        np.asarray([np.random.permutation(cities) for _ in range(n_pop)]),
        distance_matrix
    )
