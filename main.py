import os
import time
from tqdm import tqdm
from prettytable import PrettyTable
from itertools import product
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

from utils import prompt_input, read_xml, append_text
from ea import (create_distance_matrix,
                init_population,
                parent_selection,
                crossover,
                mutation)

TERMINATION = 10000

"""
This is the main function to start and run the experiment
"""


def main():
    nums_init_pop = [50, 100, 200]
    tour_sizes = [2, 5, 7]
    crossover_points = [1, 2]
    crossover_rates = [0.6, 0.7, 0.8, 0.95]
    mutation_points = [1, 2]
    mutation_rates = [0.02, 0.05, 0.1]
    params = product(
        nums_init_pop,
        tour_sizes,
        crossover_points,
        crossover_rates,
        mutation_points,
        mutation_rates
    )

    # Choose the city to run the experiment, choose between brazil or burma
    country_options = ['brazil', 'burma']
    country_input = prompt_input(country_options, 'Pick a country that you want to run the experiment on:')
    """
    _____________________
    Read and process the XML data
    _____________________
    """
    # Read the data from the XML file associated with the country
    vertexes = read_xml(country_input)
    # Create the distance matrix (D)
    distance_matrix = create_distance_matrix(vertexes)
    cities = np.array(list(i + 1 for i in range(len(distance_matrix))))

    distance_matrix_table = PrettyTable([' '] + cities.tolist())
    for row_label, row in zip(range(len(distance_matrix)), distance_matrix):
        distance_matrix_table.add_row([row_label + 1] + list(row))
    append_text(
        f'experiments/{country_input}/distance matrix.txt',
        str(distance_matrix_table)
    )

    for param_group_num, params_group in enumerate(params):
        print(f'\nRUNNING GROUP {param_group_num + 1}\n')

        """
        Input the parameter choices
        """
        param_group = param_group_num + 1
        # Choose initial population
        n_pop = params_group[0]
        # Choose the tournament size
        tour_selection_size = params_group[1]
        # Choose the number of points for crossover
        num_points = params_group[2]
        # Choose the crossover rate
        crossover_rate = params_group[3]
        # Choose the number of points mutation
        num_swaps = params_group[4]
        # Choose the mutation rate
        mutation_rate = params_group[5]
        # Specify the number of trials for each experiment
        no_of_experiments = 10

        print('PARAMS\n')
        print(f'Dataset: {country_input}\n\
Number of initial population: {n_pop}\n\
Tournament Size: {tour_selection_size}\n\
Crossover Points: {num_points}\n\
Crossover Rate: {crossover_rate}\n\
Mutation Points: {num_swaps}\n\
Mutation Rate: {mutation_rate}\n')

        append_text(f'experiments/{country_input}/group_{param_group}/parameters.txt', f'Dataset: {country_input}\n\
Number of initial population: {n_pop}\n\
Tournament Size: {tour_selection_size}\n\
Crossover Points: {num_points}\n\
Crossover Rate: {crossover_rate}\n\
Mutation Points: {num_swaps}\n\
Mutation Rate: {mutation_rate}\n')

        data = {
            'Best Initial Distance': [],
            'Best Initial Solution': [],
            'Best Final Distance': [],
            'Best Final Solution': [],
            'Execution Time': [],
            'Mean': [],
            'Median': [],
            'Standard Deviation': []
        }

        for experiment in range(no_of_experiments):
            print('Running trial', experiment + 1)

            """
            _____________________
            Population Initialization
            _____________________
            """
            # Initialize an array with random routes
            seed = np.random.randint(1, 10000)
            pop = init_population(cities, distance_matrix, n_pop, seed)
            # Evaluate the initial sample solutions to find the lowest sample solutions
            pop.evaluate()
            data['Best Initial Distance'].append(pop.best_score)
            data['Best Initial Solution'].append(pop.best_sol)

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
                crossover_operator = crossover(parent1, parent2, crossover_rate)
                child1, child2 = crossover_operator.crossover(num_points)

                """
                _____________________
                Mutation
                _____________________
                """
                mutation_operator = mutation(child1, child2, mutation_rate)
                mutated_child1, mutated_child2 = mutation_operator.swap_mutation(num_swaps)

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

            # Record the end time of the experiment
            end_time = time.time()

            execution_time = end_time - start_time

            """
            _____________________
            Plot the convergence curve and save to a png file
            _____________________
            """
            graph_file_path = f'experiments/{country_input}/group_{param_group}/convergence_curve_{experiment + 1}.png'

            directory = os.path.dirname(graph_file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            plt.plot(best_scores)
            plt.title('Convergence Curve')
            plt.xlabel('Iteration')
            plt.ylabel('Best Total Distance')
            plt.savefig(graph_file_path)  # This saves the figure as an image file
            plt.close()

            data['Best Final Distance'].append(pop.best_score)
            data['Best Final Solution'].append(pop.best_sol)
            data['Execution Time'].append(execution_time)
            data['Mean'].append(np.mean(best_scores))
            data['Median'].append(np.median(best_scores))
            data['Standard Deviation'].append(np.std(best_scores))
        df = DataFrame(data, index=list(range(1, no_of_experiments + 1)))
        log_file_path = f'experiments/{country_input}/group_{param_group}/trials_log.csv'
        df.to_csv(log_file_path)


if __name__ == '__main__':
    main()
