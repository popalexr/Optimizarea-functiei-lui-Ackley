from classes.Generation import Generation
from classes.Specimen import Specimen

def test_Generation():
    print("Testarea incepe")
    specimen1 = Specimen(dimension=2, chromosome=[1.0, 2.0])
    specimen2 = Specimen(dimension=2, chromosome=[3.0, 4.0])

    generation = Generation()
    generation.append(specimen1)
    generation.append(specimen2)

    assert generation.get_length() == 2, f"lungimea este de {generation.get_length()} care != 2"
    assert len(generation.get_generation()) == 2, f"lungimea este de {len(generation.get_generation())} care != 2"

    generation.remove(specimen1)
    assert generation.get_length() == 1
    print("A trecut testul")

test_Generation()
