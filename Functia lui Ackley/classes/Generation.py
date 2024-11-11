from classes.Specimen import Specimen

class Generation:
    def __init__(self):
        self._list = []

    def append(self, specimen: Specimen):
        self._list.append(specimen)

    def get_generation(self) -> list:
        return self._list.copy()