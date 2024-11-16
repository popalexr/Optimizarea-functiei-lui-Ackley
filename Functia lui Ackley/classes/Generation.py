from classes.Specimen import Specimen

class Generation:
    def __init__(self, generation: list['Specimen'] = []):
        self._list = generation.copy()

    def append(self, specimen: Specimen):
        self._list.append(specimen)

    def get_generation(self) -> list['Specimen']:
        return self._list.copy()

    def get_length(self) -> int:
        return len(self._list)
    
    def update_generation(self, specimen_list: list['Specimen']):
        self._list = specimen_list.copy()

    def remove(self, specimen: Specimen):
        self._list.remove(specimen)