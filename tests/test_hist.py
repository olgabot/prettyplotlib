__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
import numpy as np

@image_comparison(baseline_images=['hist'], extensions=['png'])
def test_scatter():
    # Set the random seed for consistency
    np.random.seed(12)

    # Show some color range
    for i in range(2):
        x = np.random.randn(1000)
        ppl.hist(x)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])