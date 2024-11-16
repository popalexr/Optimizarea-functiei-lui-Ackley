from math import sqrt, cos, e as E, pi as PI

# Recommended values. Source: https://www.sfu.ca/~ssurjano/ackley.html
A = 20
B = 0.2
C = 2 * PI

class Specimen:
    def __init__(self, dimension: int, chromosome: list):
        self.dimension = dimension
        self.chromosome = chromosome.copy()
        self.fitness = None
        self.__calculate_fitness()

    def get_chromosome(self) -> list:
        return self.chromosome.copy()
    
    def set_chromosome(self, chromosome: list):
        self.chromosome = chromosome.copy()
        self.__calculate_fitness()

    def get_fitness(self) -> float:
        return self.fitness

    def __calculate_fitness(self):
        """
        Fitness function is Ackley function.
        """

        expression_1 = self.__exp(
            -B * sqrt(1/self.dimension * sum([x**2 for x in self.chromosome]))
        )

        expression_2 = self.__exp(
            1/self.dimension * sum([cos(C * x) for x in self.chromosome])
        )

        self.fitness = -A * expression_1 - expression_2 + A + self.__exp(1)

    def __exp(self, expression) -> float:
        return pow(E, expression)