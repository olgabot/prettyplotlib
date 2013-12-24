__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
import numpy as np
import os


@image_comparison(baseline_images=['scatter'], extensions=['png'])
def test_scatter():
    # Set the random seed for consistency
    np.random.seed(12)

    # Show the whole color range
    for i in range(8):
        x = np.random.normal(loc=i, size=1000)
        y = np.random.normal(loc=i, size=1000)
        ppl.scatter(x, y, label=str(i))
    # fig.savefig('%s/baseline_images/test_scatter/scatter.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])