__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import numpy as np
import prettyplotlib as ppl
import matplotlib.pyplot as plt
from prettyplotlib.utils import remove_chartjunk
from prettyplotlib.colors import set2
import os

@image_comparison(baseline_images=['remove_chartjunk'], extensions=['png'])
def test_remove_chartjunk():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ax.bar(np.arange(10), np.abs(np.random.randn(10)), color=set2[0],
           edgecolor='white')
    remove_chartjunk(ax, ['top', 'right'], grid='y', ticklabels='x')
    # fig.savefig('%s/baseline_images/test_remove_chartjunk/remove_chartjunk.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])