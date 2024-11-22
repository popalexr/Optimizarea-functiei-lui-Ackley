import random

from classes.Specimen import Specimen
from classes.Generation import Generation

MIN = -32.768 # Function domain. Source: https://www.sfu.ca/~ssurjano/ackley.html
MAX = 32.768

# Mutation limit interval
MUTATION_MIN = -0.5
MUTATION_MAX = 0.5

class GA:
    def __init__(self, dimension, initial_population, mutation_rate):
        self.dimension = dimension
        self.initial_population = initial_population
        self.mutation_rate = mutation_rate
        self.best_specimen = None
        self.generation_number = 0
        
        self.current_generation = self.__generate_population() # Generate the initial population
        
    def run(self):
        """
        Run the genetic algorithm for Ackley function.
        """
        # Before starting generating the next generations, apply survival operator on the initial population to get the best specimen
        self.survival(self.current_generation)        

        while self.current_generation.get_length() >= 4: # Apply the genetic algorithm until there are less than 4 specimens in the generation
            # Select the list of parents
            parents = self.selection(self.current_generation.get_generation())

            children_generation = Generation()

            # If the number of parents is odd, remove the worst parent
            if len(parents) % 2 != 0:
                worst_parent = self.__get_worst_specimen(parents)
                parents.remove(worst_parent)

            # Apply crossover on the selected parents
            for i in range(0, len(parents), 2):
                children = self.crossover(parents[i:i+2])

                children_generation.append(children[0])
                children_generation.append(children[1])

            # Apply mutation to the children
            children_generation = self.mutation(children_generation)

            self.generation_number += 1

            # Apply survival operator on the children
            self.survival(children_generation)
        
    def selection(self, specimen_list: list) -> list:
        """
        Tournament selection method.
        @param specimen_list: list of specimens
        @return: list of parents
        """
        parents = []

        while len(specimen_list) > 0:
            turnir = [] # List of specimens for the tournament

            # Select 2 specimens for the tournament
            for _ in range(2):
                turnir.append(specimen_list.pop())
            
            # Sort the specimens by their fitness. The best one will be the first
            turnir.sort(key=lambda x: x.get_fitness())

            parents.append(turnir[0]) # Add the best specimen from tournament to the parents list

        return parents

    def crossover(self, parents: list['Specimen']) -> list['Specimen']:
        """
        Generate children by applying crossover on the parents.
        @param parents: list of parents (2 parents)
        @return: list of children (2 children)
        """

        parent1 = parents[0].get_chromosome()
        parent2 = parents[1].get_chromosome()

        child1, child2 = [], []

        if self.dimension == 1:
            # For a 1D chromosome, generate a random cut point between 0.01 and 0.99
            cut = random.uniform(0.01, 0.99)
            
            # Calculate the children using a weighted average based on the cut value
            child1 = [parent1[0] * cut + parent2[0] * (1 - cut)] 
            child2 = [parent2[0] * cut + parent1[0] * (1 - cut)]
        else:
            # For higher dimensions, use an integer cut point within the chromosome length
            cut = random.randint(1, self.dimension - 1)
            
            # Do crossover by splitting the chromosomes at the cut point and swapping parts
            child1 = parent1[:cut] + parent2[cut:]
            child2 = parent2[:cut] + parent1[cut:]
        
        return [Specimen(self.dimension, child1), Specimen(self.dimension, child2)]

    def mutation(self, children: Generation) -> Generation:
        """
        Apply mutation to the children generation.

        @param children: Generation object containing the children list
        @return: Generation object containing the mutated children list
        """

        children_generation = children.get_generation() # Get the children list from the Generation object

        for child in children_generation:
            mutation = random.uniform(MUTATION_MIN, MUTATION_MAX) # Generate a random mutation value

            # Apply the mutation if necessary
            chromosome = [x + mutation if random.uniform(0, 100) < self.mutation_rate * 100 else x for x in child.get_chromosome()]

            # Update the chromosome of the child
            child.set_chromosome(chromosome.copy())
        
        return Generation(children_generation.copy())


    def survival(self, children_generation: Generation):
        """
        Survival operation consists in:
        - Checking if the generation length is even. If not, remove the worst specimen.
        - Replacing the current generation with the children generation.

        Also, the best specimen is saved.
        @param children_generation: Generation object containing the children list
        """

        # Check if the generation length is even
        if children_generation.get_length() % 2 != 0:
            # Get the worst specimen from the children generation
            worst_specimen = self.__get_worst_specimen(children_generation.get_generation())

            # Remove the worst specimen from the children generation
            children_generation.remove(worst_specimen)

        # Replace the current generation with the children generation
        self.current_generation = children_generation

        # Get the best specimen from the current generation
        best_specimen = min(self.current_generation.get_generation(), key=lambda x: x.get_fitness())

        # Check if the best specimen is better than the current best specimen
        if self.best_specimen is None or best_specimen.get_fitness() < self.best_specimen.get_fitness():
            self.best_specimen = best_specimen

            print(f"[Generation {self.generation_number}] New best specimen: {self.best_specimen.get_chromosome()} with fitness: {self.best_specimen.get_fitness()}")
    
    def get_best_specimen(self) -> Specimen:
        """
        Get the best specimen.
        @return: Specimen object representing the best specimen or None if the best specimen was not found
        """
        return self.best_specimen

    def __generate_population(self) -> Generation:
        """
        Generate the initial population.
        @return: Generation object containing the initial population
        """

        generation = Generation()

        for _ in range(self.initial_population):
            chromosome = self.__generate_chromosomes() # Generate a random chromosome
            specimen = Specimen(self.dimension, chromosome) # Create a specimen with the generated chromosome

            generation.append(specimen) # Add the specimen to the generation

        return generation
    
    def __generate_chromosomes(self) -> list: # Generate a random chromosome
        """
        Generate a random chromosome.
        @return: list of random numbers representing the vector (x1, x2, ..., xn) of the Ackley function
        """
        chromosome = []

        for _ in range(self.dimension):
            chromosome.append(random.uniform(MIN, MAX)) # Generate a random number between MIN and MAX
        
        return chromosome

    def __get_worst_specimen(self, specimen_list: list['Specimen']) -> Specimen:
        """
        Get the worst specimen from a list of specimens.
        @param specimen_list: list of Specimen objects
        @return: Specimen object representing the worst specimen
        """
        return max(specimen_list, key=lambda x: x.get_fitness())