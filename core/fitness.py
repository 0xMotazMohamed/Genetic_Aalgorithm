def fitness_function(params: tuple) -> float:
    """
    Evaluate the fitness of an individual.

    params: a tuple of parameters (a, b, c)
    return: fitness value as float
    """
    a, b, c = params
    if a == 0:
        return -float('inf')
    vertex_x = -b / (2 * a)
    vertex_y = a * (vertex_x ** 2) + b * vertex_x + c
    y_left = a * (-10) ** 2 + b * (-10) + c
    y_right = a * (10) ** 2 + b * (10) + c
    vertex_deviation = abs(y_left - vertex_y) + abs(y_right - vertex_y)
    return -vertex_deviation
