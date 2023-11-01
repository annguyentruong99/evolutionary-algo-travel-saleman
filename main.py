import numpy as np

from utils import prompt_input, read_xml, append_text
from ea import create_distance_matrix, init_population, parent_selection

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
    log_file_path = 'experiments/{}/run_1'.format(country_input)
    # Read the data from the XML file associated with the country
    vertexes = read_xml(country_input)
    # Create the distance matrix (D)
    distance_matrix = create_distance_matrix(vertexes)
    cities = np.array(list(i + 1 for i in range(len(distance_matrix))))

    """
    _____________________
    Population Initialization
    _____________________
    """
    # Choose initial population
    n_pop = int(prompt_input(['50', '100', '200'], 'Pick your initial population:\n'))
    seed = int(prompt_input(['15', '24', '2984'], 'Pick a random seed:\n'))
    # Initialize an array with random routes
    pop = init_population(cities, distance_matrix, n_pop, seed)
    # Evaluate the initial sample solutions to find the lowest sample solutions
    pop.evaluate()

    """
    _____________________
    Fitness Evaluations
    _____________________
    """
    tour_selection_size = int(prompt_input(['4', '6', '10'], 'Pick number of tournament pool selections:\n'))
    n_fitness_eval = 0

    while n_fitness_eval <= TERMINATION:
        """
        _____________________
        Tournament Selection
        _____________________
        """
        parent1 = parent_selection(pop.population, distance_matrix, tour_selection_size)
        parent2 = parent_selection(pop.population, distance_matrix, tour_selection_size)

        """
        _____________________
        Single-point Crossover
        _____________________
        """

        """
        _____________________
        Swap Mutation
        _____________________
        """

        """
        _____________________
        Replacement
        _____________________
        """

    """
    _____________________
    Write the data into experiment text file
    _____________________
    """
    append_text(
        log_file_path,
        '***** Parameters: *****\n'
    )
    append_text(
        log_file_path,
        'Dataset: {}\n \
        Number of initial population: {}\n \
        Random Seed: {}\n \ '.format(
            country_input.capitalize(),
            n_pop,
            seed
        )
    )
    append_text(
        log_file_path,
        '***** Distance matrix: *****\n'
    )
    append_text(
        log_file_path,
        "   " + "      ".join(map(str, cities))
    )
    for row_label, row in zip(range(len(distance_matrix)), distance_matrix):
        append_text(
            log_file_path,
            '%s  [%s]' % (row_label + 1, '  '.join('%03s' % i for i in row))
        )
    append_text(
        log_file_path,
        '\n***** Initial Population: *****\n'
    )
    for row_label, row in zip(range(len(pop.solutions_sample)), pop.solutions_sample):
        append_text(
            log_file_path,
            '%s [%s]' % (row_label + 1, '  '.join('%03s' % i for i in row))
        )
    append_text(
        log_file_path,
        '\n***** Initial Best Solution: {} *****'.format(pop.best_sol)
    )
    append_text(
        log_file_path,
        '***** Initial Shortest Total Distance: {} *****'.format(pop.score)
    )


if __name__ == '__main__':
    main()
