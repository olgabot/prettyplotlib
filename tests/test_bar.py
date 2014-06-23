__author__ = 'olga'

import string

from matplotlib.testing.decorators import image_comparison
import numpy as np
import six

import prettyplotlib as ppl


if six.PY3:
    UPPERCASE_CHARS = string.ascii_uppercase
else:
    UPPERCASE_CHARS = string.uppercase


@image_comparison(baseline_images=['bar'], extensions=['png'])
def test_bar():
    np.random.seed(14)
    ppl.bar(np.arange(10), np.abs(np.random.randn(10)))
    # fig.savefig('%s/baseline_images/test_bar/bar.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['bar_grid'], extensions=['png'])
def test_bar_grid():
    np.random.seed(14)
    ppl.bar(np.arange(10), np.abs(np.random.randn(10)), grid='y')
    # fig.savefig('%s/baseline_images/test_bar/bar_grid.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['bar_annotate'], extensions=['png'])
def test_bar_annotate():
    np.random.seed(14)
    ppl.bar(np.arange(10), np.abs(np.random.randn(10)), annotate=True)
    # fig.savefig('%s/baseline_images/test_bar/bar_annotate.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['bar_annotate_user'], extensions=['png'])
def test_bar_annotate_user():
    np.random.seed(14)
    ppl.bar(np.arange(10), np.abs(np.random.randn(10)),
            annotate=range(10, 20))
    # fig.savefig('%s/baseline_images/test_bar/bar_annotate_user.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['bar_xticklabels'], extensions=['png'])
def test_bar_xticklabels():
    np.random.seed(14)
    n = 10
    ppl.bar(np.arange(n), np.abs(np.random.randn(n)),
            xticklabels=UPPERCASE_CHARS[:n])
    # fig.savefig('%s/baseline_images/test_bar/bar_xticklabels.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['bar_log'], extensions=['png'])
def test_bar_log():
    np.random.seed(14)
    x = np.arange(10)
    y = np.exp(np.random.random(10) * 5)
    ppl.bar(x, y)
    # fig.savefig('%s/baseline_images/test_bar/bar.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose

    nose.runmodule(argv=['-s', '--with-doctest'])
