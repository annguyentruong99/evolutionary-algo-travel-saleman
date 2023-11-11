import time
from tqdm import tqdm
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

from utils import prompt_input, prompt_multi_input, read_xml, append_text
from ea import create_distance_matrix, init_population, parent_selection, single_point_crossover, swap_mutation, multi_swap_mutation

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
    country_input = prompt_input(country_options, 'Pick a country that you want to run the experiment on:')
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
    crossover = prompt_input(crossover_options, 'Choose the type of crossover you want to perform:')
    # Choose the crossover rate
    crossover_rate = float(input('Specify a crossover rate:\n'))
    # Choose the type of mutation
    mutation_options = [
        'swap',
        'multi-swap'
    ]
    additional_input_prompts = {
        'multi-swap': 'Enter the number of swaps:\n'
    }
    mutation, num_swaps = prompt_multi_input(
        mutation_options,
        'Choose the type of mutation you want to perform:\n',
        additional_input_prompts
    )
    # Choose the mutation rate
    mutation_rate = float(input('Specify a mutation rate:\n'))

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
Crossover: {crossover}\n\
Crossover Rate: {crossover_rate}\n\
Mutation: {mutation}\n\
Mutation Rate: {mutation_rate}\n'
    )
    append_text(
        log_file_path,
        '***** Distance matrix: *****\n'
    )
    distance_matrix_table = PrettyTable([' '] + cities.tolist())
    for row_label, row in zip(range(len(distance_matrix)), distance_matrix):
        distance_matrix_table.add_row([row_label + 1] + list(row))
    append_text(
        log_file_path,
        str(distance_matrix_table)
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
        '***** Initial Shortest Total Distance: {} *****\n'.format(pop.best_score)
    )

    """
    _____________________
    Fitness Evaluations
    _____________________
    """
    # List of best score through iterations
    best_scores = []
    # Record the start time of the experiment
    start_time = time.time()
    # Run 10000 fitness evaluations
    for i in tqdm(range(TERMINATION), desc='Running GA', unit='iteration'):
        """
        _____________________
        Tournament Selection
        _____________________
        """
        parent1, parent2 = parent_selection(pop.population, distance_matrix, tour_selection_size)

        """
        _____________________
        Crossover
        _____________________
        """
        child1, child2 = single_point_crossover(parent1, parent2, crossover_rate)

        """
        _____________________
        Mutation
        _____________________
        """
        if mutation == 'swap':
            mutated_child1, mutated_child2 = swap_mutation(child1, child2, mutation_rate)

        if mutation == 'multi-swap':
            mutated_child1, mutated_child2 = multi_swap_mutation(child1, child2, mutation_rate, int(num_swaps))

        """
        _____________________
        Replacement
        _____________________
        """
        pop.replacement(mutated_child1)
        pop.replacement(mutated_child2)

        """
        _____________________
        Record the best score for each iteration
        _____________________
        """
        best_scores.append(pop.best_score)

        append_text(
            log_file_path,
            f'\n***** Iteration {i + 1} Best Solution: {pop.best_sol} *****'
        )
        append_text(
            log_file_path,
            f'***** Iteration {i + 1} Shortest Total Distance: {pop.best_score} *****\n'
        )
    # Record the end time of the experiment
    end_time = time.time()

    execution_time = end_time - start_time

    # Log the lowest total distance after terminated
    append_text(
        log_file_path,
        f'***** Best Solution After Iterations: {pop.best_sol} *****\n'
    )
    append_text(
        log_file_path,
        f'***** Shortest Total Distance After Iterations: {pop.best_score} *****\n'
    )

    append_text(
        log_file_path,
        '***** Execution Time: {} *****\n'.format(execution_time)
    )

    """
    _____________________
    Plot the convergence curve and save to a png file
    _____________________
    """
    graph_file_path = f'experiments/{country_input}/group_{param_group}/convergence_curve_{experiment_number}.png'

    plt.plot(best_scores)
    plt.title('Convergence Curve')
    plt.xlabel('Iteration')
    plt.ylabel('Best Total Distance')
    plt.savefig(graph_file_path)  # This saves the figure as an image file
    plt.close()


if __name__ == '__main__':
    main()
