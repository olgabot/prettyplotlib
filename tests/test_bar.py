__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import os
import string

@image_comparison(baseline_images=['bar'], extensions=['png'])
def test_bar():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)))
    # fig.savefig('%s/baseline_images/test_bar/bar.png' %
    #             os.path.dirname(__file__))

@image_comparison(baseline_images=['bar_grid'], extensions=['png'])
def test_bar_grid():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)), grid='y')
    # fig.savefig('%s/baseline_images/test_bar/bar_grid.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['bar_annotate'], extensions=['png'])
def test_bar_annotate():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)), annotate=True)
    # fig.savefig('%s/baseline_images/test_bar/bar_annotate.png' %
    #             os.path.dirname(__file__))

@image_comparison(baseline_images=['bar_xticklabels'], extensions=['png'])
def test_bar_xticklabels():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    n = 10
    ppl.bar(ax, np.arange(n), np.abs(np.random.randn(n)),
            xticklabels=string.uppercase[:n])
    # fig.savefig('%s/baseline_images/test_bar/bar_xticklabels.png' %
    #             os.path.dirname(__file__))

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])