__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
from matplotlib import pyplot as plt
import numpy as np
import prettyplotlib as ppl

@image_comparison(baseline_images=['scatter'], extensions=['png'])
def test_scatter():
    # Set the random seed for consistency
    np.random.seed(12)

    x = np.random.randn(1000)
    y = np.random.randn(1000)

    fig, ax = plt.subplots()
    ppl.scatter(ax, x, y)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])