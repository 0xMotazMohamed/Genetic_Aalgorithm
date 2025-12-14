from core.crossover import arithmetic_crossover
from core.fitness import fitness_function
from core.mutation import mutate
from core.population import create_initial_population
from core.selection import tournament_selection

import pandas as pd

def genetic_algorithm(population_size,generations,lower_bound,upper_bound,mutation_rate,crossover_rate, tournament_size:int = 3):
    # History
    all_populations = []
    best_performance = []

    population = create_initial_population(population_size,lower_bound,upper_bound)

    # Iterating through Generation Starting with the first one
    for generation in range(generations):

        fitnesses = [fitness_function(ind) for ind in population]
        best_performance.append(max(fitnesses))

        population = tournament_selection(population,fitnesses,tournament_size)
        all_populations.append(population)

        selected_population = population
        if len(selected_population) % 2 != 0:
            selected_population = selected_population[:-1]

        next_population = []
        for ind in range(0 , len(selected_population) , 2):
            parent1 = population[ind]
            parent2 = population[ind+1]

            child1,child2 = arithmetic_crossover(parent1,parent2,crossover_rate)
            child1 = mutate(child1,mutation_rate,lower_bound, upper_bound)
            child2 = mutate(child2,mutation_rate,lower_bound, upper_bound)

            h1 , h2 = compare_fitnesses(parent1,parent2,child1,child2)
            next_population.append(h1)
            next_population.append(h2)


        if len(selected_population) != len(population):
            next_population.append(population[len(population)-1])

        population = next_population


    return  all_populations, best_performance


def compare_fitnesses(p1,p2,c1,c2):
    candidates = [(p1, fitness_function(p1)),(p2, fitness_function(p2)),
        (c1, fitness_function(c1)),(c2, fitness_function(c2))]

    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[0][0], candidates[1][0]

