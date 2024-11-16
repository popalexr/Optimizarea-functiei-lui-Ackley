from classes.GA import GA

if __name__ == "__main__":
    genetical_algorithm = GA(dimension=2, initial_population=5555, mutation_rate=0.25)

    genetical_algorithm.run()

    print(f"Best specimen: {genetical_algorithm.get_best_specimen().get_chromosome()} with fitness {genetical_algorithm.get_best_specimen().get_fitness()}")