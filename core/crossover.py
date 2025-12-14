import random

def arithmetic_crossover(parent1: tuple, parent2: tuple, crossover_rate: float) -> tuple:
    """
    Produce children from two parents using crossover.

    parent1, parent2: tuples of parameters
    return: two child tuples
    """

    crossover_probability = random.random()

    if crossover_probability < crossover_rate:
        mixing_ratio = random.random()

        child1, child2 = []

        for coefficient_parent1, coefficient_parent2 in zip(parent1, parent2):
            child1.append(mixing_ratio * coefficient_parent1 + (1 - mixing_ratio) * coefficient_parent2)
            child2.append(mixing_ratio * coefficient_parent2 + (1 - mixing_ratio) * coefficient_parent1)
        
        child1 = tuple(child1)
        child2 = tuple(child2)
        return child1, child2
    
    return parent1, parent2
