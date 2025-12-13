# Connecting Everything Together

# The genetic algorithm loop

from typing import Callable

def genetic_algorithm(
    fitness_function: Callable,
    population_size: int,
    generations: int,
    bounds: tuple,
    mutation_rate: float,
    tournament_size: int
) -> tuple:
    """
    Run the genetic algorithm.

    fitness_function: callable that evaluates an individual
    population_size: number of individuals
    generations: number of generations to run
    bounds: (low, high) for gene values
    mutation_rate: mutation probability
    tournament_size: selection tournament size

    return: history and populations (empty for now)
    """
    pass
