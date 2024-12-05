import os
import dotenv
import time
import json

from classes.GA import GA
from classes.Plot import Plot




if __name__ == "__main__":
    # Load the environment variables
    dotenv.load_dotenv()
    time_start = time.perf_counter()
    genetical_algorithm = GA(
        dimension=int(os.getenv('DIMENSION')),
        initial_population=int(os.getenv('INITIAL_POPULATION')),
        mutation_rate=float(os.getenv('MUTATION_RATE')),
    )

    genetical_algorithm.run()

    print(f"Best specimen: {genetical_algorithm.get_best_specimen().get_chromosome()} with fitness {genetical_algorithm.get_best_specimen().get_fitness()}")


    best_fitnesses = genetical_algorithm.get_best_fitnesses_list()


    performance_data = []
    for i in range(len(best_fitnesses)):
            performance_data.append({
        "generation": i + 1,  # Using i as the generation index
        "best_fitness": best_fitnesses[i],
        
    })

# Save to JSON
    with open("performance_data.json", mode="w") as file:
        json.dump(performance_data, file, indent=4)

    time_end = time.perf_counter()
    print(f"Elapsed time: {time_end - time_start} seconds")
    # Plot the best fitnesses for each generation
    plot = Plot(genetical_algorithm.get_best_fitnesses_list())
    plot.plot()