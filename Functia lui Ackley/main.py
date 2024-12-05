import os
import dotenv

from classes.GA import GA
from classes.Plot import Plot

if __name__ == "__main__":
    # Load the environment variables
    dotenv.load_dotenv()

    genetical_algorithm = GA(
        dimension=int(os.getenv('DIMENSION')),
        initial_population=int(os.getenv('INITIAL_POPULATION')),
        mutation_rate=float(os.getenv('MUTATION_RATE')),
    )

    genetical_algorithm.run()

    print(f"Best specimen: {genetical_algorithm.get_best_specimen().get_chromosome()} with fitness {genetical_algorithm.get_best_specimen().get_fitness()}")

    # Plot the best fitnesses for each generation
    plot = Plot(genetical_algorithm.get_best_fitnesses_list())
    plot.plot()