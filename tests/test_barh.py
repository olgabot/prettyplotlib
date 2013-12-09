__author__ = 'jan'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import os
import string
import six

if six.PY3:
    UPPERCASE_CHARS = string.ascii_uppercase
else:
    UPPERCASE_CHARS = string.uppercase


@image_comparison(baseline_images=['bar'], extensions=['png'])
def test_bar():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.barh(ax, np.arange(10), np.abs(np.random.randn(10)))
    # fig.savefig('%s/baseline_images/test_barh/bar.png' %
    #             os.path.dirname(os.path.abspath(__file__)))

@image_comparison(baseline_images=['bar_grid'], extensions=['png'])
def test_bar_grid():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.barh(ax, np.arange(10), np.abs(np.random.randn(10)), grid='x')
    # fig.savefig('%s/baseline_images/test_barh/bar_grid.png' %
    #              os.path.dirname(os.path.abspath(__file__)))


@image_comparison(baseline_images=['bar_annotate'], extensions=['png'])
def test_bar_annotate():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.barh(ax, np.arange(10), np.abs(np.random.randn(10)), annotate=True)
    # fig.savefig('%s/baseline_images/test_barh/bar_annotate.png' %
    #             os.path.dirname(os.path.abspath(__file__)))

@image_comparison(baseline_images=['bar_annotate_user'], extensions=['png'])
def test_bar_annotate_user():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    ppl.barh(ax, np.arange(10), np.abs(np.random.randn(10)),
            annotate=range(10,20))
    # fig.savefig('%s/baseline_images/test_barh/bar_annotate_user.png' %
    #             os.path.dirname(os.path.abspath(__file__)))


@image_comparison(baseline_images=['bar_xticklabels'], extensions=['png'])
def test_bar_xticklabels():
    fig, ax = plt.subplots(1)
    np.random.seed(14)
    n = 10
    ppl.barh(ax, np.arange(n), np.abs(np.random.randn(n)),
            yticklabels=UPPERCASE_CHARS[:n])
    # fig.savefig('%s/baseline_images/test_barh/bar_xticklabels.png' %
    #              os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])

