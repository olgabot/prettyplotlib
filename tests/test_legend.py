__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
import numpy as np
import os

# This is "import matplotlib.pyplot as plt" from the prettyplotlib library
from prettyplotlib import plt

@image_comparison(baseline_images=['legend'], extensions=['png'])
def test_legend():
    # Set the random seed for consistency
    np.random.seed(12)

    fig, ax = plt.subplots(1)

    # Show the whole color range
    for i in range(8):
        x = np.random.normal(loc=i, size=1000)
        y = np.random.normal(loc=i, size=1000)
        ppl.scatter(ax, x, y, label=str(i))
    ppl.legend(ax)
    # fig.savefig('%s/baseline_images/test_legend/legend.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])