__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
import numpy as np
import os


@image_comparison(baseline_images=['plot'], extensions=['png'])
def test_plot():
    # Set the random seed for consistency
    np.random.seed(12)

    # Show the whole color range
    for i in range(8):
        y = np.random.normal(size=1000).cumsum()
        x = np.arange(1000)

        # For now, you need to specify both x and y :(
        # Still figuring out how to specify just one
        ppl.plot(x, y, label=str(i))
    # fig.savefig('%s/baseline_images/test_plot/plot.png' %
    #             os.path.dirname(__file__))

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])