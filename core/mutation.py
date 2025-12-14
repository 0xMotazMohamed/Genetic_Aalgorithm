import random

def mutate(individual: tuple, mutation_rate: float, low: float, high: float) -> tuple:
    """
    Mutate an individual with given mutation rate and bounds.

    individual: tuple of parameters
    mutation_rate: probability of mutation per gene
    low, high: bounds for gene values
    return: mutated individual tuple
    """
    mutation_probability = random.random()

    if mutation_probability < mutation_rate:
        individual = list(individual)
        mutation_amount = random.uniform(-1, 1)
        for i in len(individual):
            individual[i] *= mutation_amount
            individual[i] = max(min(individual[i], high), low)
        individual = tuple(individual)
        return individual
    
    return individual
