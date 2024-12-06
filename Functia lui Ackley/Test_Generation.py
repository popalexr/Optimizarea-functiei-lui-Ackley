import unittest
from classes.Generation import Generation
from classes.Specimen import Specimen
 
class TestGeneration(unittest.TestCase):
 
    def test_generation(self):
        print("Running the Test")
 
        # Creating Specimen instances
        specimen1 = Specimen(dimension=2, chromosome=[1.0, 2.0])
        specimen2 = Specimen(dimension=2, chromosome=[3.0, 4.0])
 
        # Creating Generation instance
        generation = Generation()
 
        # Adding specimens to the generation
        generation.append(specimen1)
        generation.append(specimen2)
 
        # Check if the length of the generation is 2
        self.assertEqual(generation.get_length(), 2, f"lungimea este de {generation.get_length()} care != 2")
        self.assertEqual(len(generation.get_generation()), 2, f"lungimea este de {len(generation.get_generation())} care != 2")
 
        # Remove specimen1 and check that the length is now 1
        generation.remove(specimen1)
        self.assertEqual(generation.get_length(), 1)
 
        print("Passed the Test")
 
if __name__ == '__main__':
    unittest.main()