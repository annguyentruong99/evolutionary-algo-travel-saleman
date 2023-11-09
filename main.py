import numpy as np

from utils import prompt_input, read_xml, append_text
from ea import create_distance_matrix, init_population, parent_selection, single_point_crossover

TERMINATION = 10000

"""
This is the main function to start and run the experiment
"""


def main():

    """
    Input the parameter choices
    """
    experiment_number = int(input('What is the number of this experiment?\n'))
    param_group = int(input('Enter your parameters group number:\n'))
    # Choose the city to run the experiment, choose between brazil or burma
    country_options = ['brazil', 'burma']
    country_input = prompt_input(country_options, 'Pick a country that you want to run the experiment on:\n')
    # Choose initial population
    n_pop = int(input('Pick your initial population:\n'))
    seed = int(input('Pick a random seed:\n'))
    # Choose the tournament size
    tour_selection_size = int(input('Pick number of tournament pool selections:\n'))
    # Choose the type of crossover
    crossover_options = [
        'single-point',
        'multi-point',
    ]
    crossover = prompt_input(crossover_options, 'Choose the type of crossover you want to perform:\n')

    """
    _____________________
    Read and process the XML data
    _____________________
    """
    log_file_path = f'experiments/{country_input}/group_{param_group}/run_{experiment_number}.txt'
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
    # Initialize an array with random routes
    pop = init_population(cities, distance_matrix, n_pop, seed)
    # Evaluate the initial sample solutions to find the lowest sample solutions
    pop.evaluate()

    """
    _____________________
    Write the experiment specifications into a text file for reference
    _____________________
    """
    append_text(
        log_file_path,
        '***** Parameters: *****\n'
    )
    append_text(
        log_file_path,
        f'Dataset: {country_input}\n\
Number of initial population: {n_pop}\n\
Random Seed: {seed}\n\
Tournament Size: {tour_selection_size}\n\
Crossover: {crossover}\n'
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
    for row_label, row in zip(range(len(pop.population)), pop.population):
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

    """
    _____________________
    Fitness Evaluations
    _____________________
    """

    # Run 10000 fitness evaluations
    # for _ in range(TERMINATION):
    #     """
    #     _____________________
    #     Tournament Selection
    #     _____________________
    #     """
    #     parent1 = parent_selection(pop.population, distance_matrix, tour_selection_size)
    #     parent2 = parent_selection(pop.population, distance_matrix, tour_selection_size)
    #
    #     """
    #     _____________________
    #     Crossover
    #     _____________________
    #     """
    #     child1, child2 = single_point_crossover(parent1, parent2)
    #
    #     """
    #     _____________________
    #     Mutation
    #     _____________________
    #     """
    #
    #     """
    #     _____________________
    #     Replacement
    #     _____________________
    #     """
    #


if __name__ == '__main__':
    main()
