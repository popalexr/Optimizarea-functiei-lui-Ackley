from lib.Individ import Individ
import random

x = []

for i in range(10):
    x.append(Individ(2, [random.randint(-32, 32), random.randint(-32, 32)]))

    x[-1].calculate_fitness()

for i in x:
    print("-------------")
    print(f'Cromozomi: {i.get_chromosome()}')
    print(f'Fitness: {i.get_fitness()}')
    print("-------------")