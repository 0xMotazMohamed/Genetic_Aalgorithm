# load config
# choose experiment
# run algorithm
# get history
# visualize
# save results

import config.ga_config as config
from experiments.quadratic_u_shape import run_experiment

def main():
    best_solution = run_experiment(config)
    print("Best solution", best_solution)

if __name__ == "__main__":
    main()
