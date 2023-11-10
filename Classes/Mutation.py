import numpy as np


class Mutation:
    def __init__(self, child1, child2, mutation_rate):
        self.child1 = child1
        self.child2 = child2
        self.mutation_rate = mutation_rate

    def swap_mutation(self):
        """
        Performs swap mutation on both children by swapping two randomly chosen elements in each child.
        :return: None
        """

        # Define a function for swapping two elements in an array
        def swap(arr):
            # Choose two distinct indices for swapping
            idx1, idx2 = np.random.choice(len(arr), size=2, replace=False)
            # Perform the swap
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        rng = np.random.default_rng()
        if rng.random() < self.mutation_rate:
            swap(self.child1)
        if rng.random() < self.mutation_rate:
            swap(self.child2)

        return self.child1, self.child2
