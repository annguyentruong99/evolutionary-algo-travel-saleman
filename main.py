import numpy as np

from utils import prompt_input, read_xml
from ea import create_distance_matrix, init_population

TERMINATION = 10000

"""
This is the main function to start and run the experiment
"""


def main():
    """
    _____________________
    Read and process the XML data
    _____________________
    """
    # Choose the city to run the experiment, choose between Brazil or Burma
    country_options = ['brazil', 'burma']
    country_input = prompt_input(country_options, 'Pick a country that you want to run the experiment on:\n')
    # read the data from the XML file associated with the country
    vertexes = read_xml(country_input)
    # Create the distance matrix (D)
    distance_matrix = create_distance_matrix(vertexes)
    cities = list(range(len(distance_matrix)))
    print('Successfully created distance matrix\n')
    print("   " + "      ".join(map(str, cities)))
    for row_label, row in zip(range(len(distance_matrix)), distance_matrix):
        print('%s [%s]' % (row_label, '  '.join('%03s' % i for i in row)))

    '''
    _____________________
    Population Initialization
    _____________________
    '''
    # Choose initial population
    n_pop = int(prompt_input(['10', '100', '1000'], 'Pick your initial population:\n'))
    seed = int(prompt_input(['15', '24', '2984'], 'Pick a random seed:\n'))

    pop = init_population(cities, distance_matrix, n_pop, seed)

    distances = np.asarray(
        [pop.fitness(chromosome) for chromosome in pop.population]
    )

    print(distances)


if __name__ == '__main__':
    main()
