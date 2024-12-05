import unittest
import random
from classes.Specimen import Specimen
from classes.Generation import Generation
from classes.GA import GA



class TestGA(unittest.TestCase):


    def setUp(self):
        # Initialize parameters for the GA instance
        self.dimension = 2
        self.initial_population = 10
        self.mutation_rate = 0.25

        # Create a GA instance
        self.ga = GA(self.dimension, self.initial_population, self.mutation_rate)

    def testSelection(self):
        """
        Test the selection function to ensure it selects the best specimens in a tournament.
        """
        # Create a list of specimens with predefined fitness values
        specimen1 = Specimen(self.dimension, [0.1, 0.2])  # Fitness: 0.1
        specimen1.fitness = 0.1

        specimen2 = Specimen(self.dimension, [0.3, 0.4])  # Fitness: 0.3
        specimen2.fitness = 0.3

        specimen3 = Specimen(self.dimension, [0.5, 0.6])  # Fitness: 0.5
        specimen3.fitness = 0.5

        specimen4 = Specimen(self.dimension, [0.7, 0.8])  # Fitness: 0.7
        specimen4.fitness = 0.7

        specimen_list = [specimen1, specimen2, specimen3, specimen4]

        # Shuffle the specimens to simulate randomness in input
        random.shuffle(specimen_list)

        # Perform selection
        selected_parents = self.ga.selection(specimen_list.copy())

        # Check if the correct number of parents is selected
        self.assertEqual(
            len(selected_parents),
            len(specimen_list) // 2,
            "Selection did not return the correct number of parents."
        )

        


        # Ensure no specimen is repeated
        self.assertEqual(
            len(set(selected_parents)),
            len(selected_parents),
            "Selected parents contain duplicates."
        )

        self.assertIsInstance(selected_parents, list, "The return value is not a list")

    def testCrossoverResultSizeFor1D(self):
         
         self.dimension = 1

         parent1 = Specimen(self.dimension, [5.0])
         parent2 = Specimen(self.dimension, [3.0])

         parents = [parent1, parent2]

         children = self.ga.crossover(parents)

         self.assertEqual(len(children), 2, "Crossover did not produce 2 children")

         self.assertTrue( all(isinstance(child, Specimen) for child in children), "Children created are not Speciment instances")

    def test_crossover_result_size_for_N_dimension(self):
         
         self.dimension = 3

         parent1 = Specimen(self.dimension, [5.0, 0.4, 0.9])
         parent2 = Specimen(self.dimension, [3.0, 0.1, 0.6])

         parents = [parent1, parent2,]

         children = self.ga.crossover(parents)

         self.assertEqual(len(children), 2, "Crossover did not produce 2 children")

         self.assertTrue(all(isinstance(child, Specimen) for child in children), "Children created are not Speciment instances")


    def test_mutation_return_value(self):
        specimen = Specimen(self.dimension, [0.5, 0.4])
        generation = Generation([specimen])

        mutated_generation = self.ga.mutation(generation)

        self.assertIsInstance(mutated_generation, Generation, "Mutated generation is not a Generation instance")


    def test_survival_best_specimen_unchanged(self):
      
        
        initial_best_specimen = Specimen(self.dimension, [7.0, 8.0])
        initial_best_specimen.fitness = 0.2
        self.ga.best_specimen = initial_best_specimen

        
        specimen1 = Specimen(self.dimension, [1.0, 2.0])
        specimen1.fitness = 0.5

        specimen2 = Specimen(self.dimension, [3.0, 4.0])
        specimen2.fitness = 0.3

        
        children_generation = Generation([specimen1, specimen2])

        
        self.ga.survival(children_generation)

        
        self.assertEqual(self.ga.current_generation.get_generation(), [specimen1, specimen2], "Current generation was not replaced")

        
        self.assertEqual(self.ga.get_best_specimen(), initial_best_specimen, "Best specimen was changed")


    

       

        

    

    
   
