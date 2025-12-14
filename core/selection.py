import random

def tournament_selection(population: list, fitnesses: list, k: int) -> list:
    """
    Select individuals using tournament selection.

    population: list of individuals
    fitnesses: list of fitness values
    k: tournament size
    return: list of selected individuals
    """
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitnesses)), k)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)

    return selected
