import numpy as np
from utils import contains_duplicates, find_duplicate_indexes


class Crossover:
    def __init__(self, parent1, parent2, crossover_rate):
        self.parent1 = parent1
        self.parent2 = parent2
        self.crossover_rate = crossover_rate

    def single_point(self):
        """
        Method to generate 2 different children by single-point crossover
        :return: child1, child2: ndarray, ndarray
        """
        def fix_child(child, parent):
            """
            Method to fix children if there are duplicates
            :param child: ndarray
            :param parent: ndarray
            :return: child: ndarray
            """
            first_duplicate_ind, second_duplicate_ind = find_duplicate_indexes(child)
            city_to_swap = parent[second_duplicate_ind]
            child[first_duplicate_ind] = city_to_swap
            return child

        rng = np.random.default_rng()
        # Decide whether to perform crossover based on the crossover rate
        if rng.random() <= self.crossover_rate:
            crossover_point = rng.integers(1, len(self.parent1) - 1)

            child1 = np.append(self.parent1[:crossover_point], self.parent2[crossover_point:])
            child2 = np.append(self.parent2[:crossover_point], self.parent1[crossover_point:])

            if contains_duplicates(child1) and contains_duplicates(child2):
                fixed_child1 = fix_child(child1, self.parent1)
                fixed_child2 = fix_child(child2, self.parent2)

                return fixed_child1, fixed_child2

            return child1, child2
        else:
            # If crossover is not performed, children are copies of the parents
            return self.parent1.copy(), self.parent2.copy()

    def multi_points(self, num_points):
        """
        Method to generate 2 different children by multi-point crossover.
        :param num_points: Number of crossover points.
        :return: child1, child2: ndarray, ndarray
        """

        def fix_child(child, parent):
            """
            Method to fix children if there are duplicates.
            :param child: ndarray
            :param parent: ndarray
            :return: child: ndarray
            """
            duplicate_indices = find_duplicate_indexes(child)
            for i in duplicate_indices:
                missing_values = list(set(parent) - set(child))
                if missing_values:
                    # Choose a random missing value to replace the duplicate
                    replacement_value = np.random.choice(missing_values)
                    child[i] = replacement_value
                else:
                    # Handle case where no missing values are left
                    # This might need more sophisticated handling based on your problem specifics
                    break
            return child

        rng = np.random.default_rng()
        # Decide whether to perform crossover based on the crossover rate
        if rng.random() <= self.crossover_rate:
            # Randomly select unique crossover points
            crossover_points = sorted(rng.choice(len(self.parent1) - 2, size=num_points, replace=False) + 1)

            # Initialize children as copies of parents
            child1, child2 = self.parent1.copy(), self.parent2.copy()

            # Alternate segments from each parent based on crossover points
            for i in range(num_points):
                if i % 2 != 0:
                    continue

                end_point = crossover_points[i + 1] if i + 1 < len(crossover_points) else len(self.parent1)
                (child1[crossover_points[i]:end_point]
                 , child2[crossover_points[i]:end_point]) = (child2[crossover_points[i]:end_point],
                                                             child1[crossover_points[i]:end_point])

            if contains_duplicates(child1) and contains_duplicates(child2):
                fixed_child1 = fix_child(child1, self.parent1)
                fixed_child2 = fix_child(child2, self.parent2)

                return fixed_child1, fixed_child2

            return child1, child2
        else:
            # If crossover is not performed, children are copies of the parents
            return self.parent1.copy(), self.parent2.copy()
