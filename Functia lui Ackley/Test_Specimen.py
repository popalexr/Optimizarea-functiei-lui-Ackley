import unittest     # Unit testing
from math import isclose
from classes.Specimen import Specimen

from parameterized import parameterized  # Parameterized testing and random parameters
import random

from math import sqrt, cos, e as E, pi as PI # Math functions and constants
from classes.Specimen import A, B, C

import time # Time for performance testing


class TestSpecimenFitnessCalculation(unittest.TestCase):
    def setUp(self):
        self.dimension = 2
        self.chromosome = [0, 0]
        self.specimen = Specimen(self.dimension, self.chromosome)

    # Test pentru calculul fitness-ului
    @parameterized.expand([
        ([0, 0], 0.0),  # Ackley minimum
        ([1, 1], None),  # Exemplu non-minim cu valoare statică
        ([random.uniform(-32.768, 32.768), random.uniform(-32.768, 32.768)], None),  
        ([random.uniform(-32.768, 32.768), random.uniform(-32.768, 32.768)], None),  # Parametri random pentru 3 cazuri
        ([random.uniform(-32.768, 32.768), random.uniform(-32.768, 32.768)], None),  
    ])

    # Test pentru calculul fitness-ului
    def test_fitness_calculation(self, chromosome, expected_fitness):
        self.specimen.set_chromosome(chromosome)
        calculated_fitness = self.specimen.get_fitness()
        print(f"Calculated fitness for chromosome {chromosome}: {calculated_fitness}")
        if expected_fitness is not None:
            self.assertTrue(isclose(calculated_fitness, expected_fitness, abs_tol=1e-15))
        else:
            self.assertIsInstance(calculated_fitness, float)

    # Test pentru dimensiune invalidă
    def test_invalid_dimension(self): #(Fail)
        with self.assertRaises(ValueError):
            Specimen(0, [0])  # Dimensiunea nu poate fi zero
        with self.assertRaises(ValueError): #(Fail)
            Specimen(-1, [0])  # Dimensiunea nu poate fi negativă

    # Test pentru lungimea invalidă a cromozomului
    def test_invalid_chromosome_length(self): # (Fail)
        with self.assertRaises(ValueError):
            Specimen(2, [0])  # Lungimea cromozomului trebuie să corespundă dimensiunii

    # Test pentru obținerea cromozomului
    def test_get_chromosome(self): # (Pass)
        chromosome = [1, 2]
        self.specimen.set_chromosome(chromosome)
        returned_chromosome = self.specimen.get_chromosome()
        self.assertEqual(chromosome, returned_chromosome)
        self.assertIsNot(chromosome, returned_chromosome)  # Asigură-te că este o copie

    # Test pentru recalcularea fitness-ului la setarea cromozomului
    def test_set_chromosome_recalculates_fitness(self):
        chromosome = [1, 1]
        self.specimen.set_chromosome(chromosome)
        expected_fitness = -A * E ** (-B * sqrt(2)) - E ** (cos(C) + cos(C)) + A + E
        self.assertTrue(isclose(self.specimen.get_fitness(), expected_fitness, abs_tol=1e-10))

    @parameterized.expand([
    ([-32.768] * 2, None),  # Lower bound for each gene
    ([32.768] * 2, None),   # Upper bound for each gene
    ([0.1, 0.1], None),     # Small identical values
])
    def test_edge_case_chromosomes(self, chromosome, expected_fitness):
        self.specimen.set_chromosome(chromosome)
        calculated_fitness = self.specimen.get_fitness()
        self.assertIsInstance(calculated_fitness, float)

    # Testare pentru dimensiuni mai mari față de cele standard (2)
    def test_higher_dimensions(self):
        chromosome = [1] * 10  # Dimension = 10
        specimen = Specimen(10, chromosome)
        expected_fitness = -A * E ** (-B * sqrt(sum(x**2 for x in chromosome) / 10)) - E ** (sum(cos(C * x) for x in chromosome) / 10) + A + E
        self.assertTrue(isclose(specimen.get_fitness(), expected_fitness, abs_tol=1e-10))

    #  Testare pentru valori extrem de mari la cronozomi
    def test_large_values(self):
        chromosome = [1e6, -1e6]
        self.specimen.set_chromosome(chromosome)
        self.assertIsInstance(self.specimen.get_fitness(), float)

    # Testare pentru precizia fitness-ului (Pass)
    def test_fitness_precision(self):
        chromosome = [0.1, 0.2]
        self.specimen.set_chromosome(chromosome)
        fitness = self.specimen.get_fitness()
        self.assertTrue(isinstance(fitness, float))
        self.assertLess(abs(fitness - round(fitness, 15)), 1e-15)

    # Testare pentru performanță (Pass)
    def test_performance(self):
        num_specimens = 100000
        start_time = time.time()
        for _ in range(num_specimens):
            chromosome = [random.uniform(-32.768, 32.768) for _ in range(self.dimension)]
            self.specimen.set_chromosome(chromosome)
            _ = self.specimen.get_fitness()
        elapsed_time = time.time() - start_time
        self.assertLess(elapsed_time, 5)  # Verificare daca toate calculele se fac in mai putin de 5 secunde


if __name__ == '__main__':
    unittest.main()