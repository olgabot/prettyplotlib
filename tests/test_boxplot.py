__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
from matplotlib import pyplot as plt
import numpy as np
import prettyplotlib as ppl


@image_comparison(baseline_images=['boxplot'], extensions=['png'])
def test_boxplot():
    # Set the random seed for consistency
    np.random.seed(10)

    data = np.random.randn(8, 4)
    labels = ['A', 'B', 'C', 'D']

    fig, ax = plt.subplots()
    ppl.boxplot(ax, data, labels)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])
