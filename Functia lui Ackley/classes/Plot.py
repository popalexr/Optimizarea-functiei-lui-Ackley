import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self, values: list = []):
        self.values = values

        self.min_value = None
        self.min_index = None

        self.__calculate_min_value()
        

    def set_values(self, values: list):
        """
        Set the values list for the plot
        @param values: list of values
        """
        self.values = values

        self.__calculate_min_value()

    def plot(self):
        """
        Plot the values list
        """
        plt.plot(self.values)
        plt.plot(self.min_index, self.min_value, marker='o', markersize=10, markerfacecolor='red', label='Best Specimen')
        plt.ylabel('Fitness')
        plt.xlabel('Generation')
        plt.title('Best fitness for each generation')
        plt.show()

    def __calculate_min_value(self):
        """
        Calculate the minimum value from the values list
        """
        self.min_value = np.min(self.values)
        self.min_index = np.where(self.values == self.min_value)[0][0]