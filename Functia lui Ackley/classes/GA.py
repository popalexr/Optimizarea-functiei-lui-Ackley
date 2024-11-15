import random
class GA:
    def __init__(self):
        pass
    
    def run(self):
        pass

    def selection(self, specimen_list: list) -> list:
        parents = []
        while len(specimen_list > 0):
            turnir = []

            # Select 4 specimens for the tournament
            for i in range(4):
                turnir.append(specimen_list.pop())
            
            # Sort the specimens by their fitness. The best one will be the first
            turnir.sort(key=lambda x: x.get_fitness())

            parents.append(turnir[0])

        return parents


    def crossover(self, parents: list) -> list: # Crossover function completed 
        parent1 = parents[0]
        parent2 = parents[1]
        if self.dimension > 1:
            cut = random.randint(1, self.size - 1) # Cutting point from 100% of the size of the specimen
            child1 = p1 * cut + p2 * (1 - cut) 
            child2 = p2 * cut + p1 * (1 - cut)
        else:
            cut = random.randint(1, self.size - 1)
            child1 = p1[:len*cut] + p2[len*cut:]
            child2 = p2[:len*cut] + p1[len*cut:]

    def mutation(self, child: list) -> list:
        pass

    def survival(self, specimen_list: list) -> list:
        pass