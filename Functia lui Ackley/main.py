from classes.GA import GA
from classes.Plot import Plot

if __name__ == "__main__":
    genetical_algorithm = GA(dimension=2, initial_population=555555, mutation_rate=0.25)

    genetical_algorithm.run()

    print(f"Best specimen: {genetical_algorithm.get_best_specimen().get_chromosome()} with fitness {genetical_algorithm.get_best_specimen().get_fitness()}")

    # Plot the best fitnesses for each generation
    plot = Plot(genetical_algorithm.get_best_fitnesses_list())
    plot.plot()