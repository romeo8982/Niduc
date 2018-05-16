import numpy as np
from matplotlib import pyplot as plt


class Histogram:

    def __init__(self, list_of_bits, histogram_label):
        plt.xlim([min(list_of_bits) - 5, max(list_of_bits) + 5])
        bins = np.arange(0, max(list_of_bits) + 1, 1)
        plt.hist(list_of_bits, bins=bins, alpha=0.5, log=True)
        plt.title('Histogram występowania ' + histogram_label)
        plt.xlabel('liczba ' + histogram_label + ' pod rząd')
        plt.ylabel('ilość wystąpień')
        plt.show()
