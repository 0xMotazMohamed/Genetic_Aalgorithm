import random


def create_initial_population(size: int, low: float, high: float) -> list:
    """
    Create the initial population of individuals.

    size: population size
    low: lower bound of gene values
    high: upper bound of gene values
    return: list of individuals
    """

    population = []
    for _ in range(size):
        population.append((
            random.uniform(low, high),
            random.uniform(low, high),
            random.uniform(low, high)
            ))
    return population