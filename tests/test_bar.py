__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import os

@image_comparison(baseline_images=['bar'], extensions=['png'])
def test_bar():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)))
    # fig.savefig('%s/baseline_images/test_bar/bar.png' %
    #             os.path.dirname(__file__))

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])