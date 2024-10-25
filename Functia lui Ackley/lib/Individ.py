from math import sqrt, cos

E = 2.718281828459045
PI = 3.141592653589793

# Recommended values. Source: https://www.sfu.ca/~ssurjano/ackley.html
A = 20
B = 0.2
C = 2 * PI

class Individ:
    def __init__(self, dimension, chromosome):
        self.dimension = dimension
        self.chromosome = chromosome
        self.fitness = None

    def calculate_fitness(self):
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

    def get_chromosome(self) -> list:
        return self.chromosome.copy()

    def get_fitness(self) -> int:
        return self.fitness

    def __exp(self, expression) -> float:
        return pow(E, expression)