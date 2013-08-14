__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np
import prettyplotlib as ppl
import os

@image_comparison(baseline_images=['remove_chartjunk'], extensions=['png'])
def test_remove_chartjunk():
    fig, ax = plt.subplots(1)
    ax.hist(np.random.randn(1000))
    ppl.remove_chartjunk(ax, ['top', 'right'], grid='y', ticklabels='x')
    # fig.savefig('%s/baseline_images/test_remove_chartjunk/remove_chartjunk.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])