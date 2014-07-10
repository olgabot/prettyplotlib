__author__ = 'jan'

from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np
import prettyplotlib as ppl
import os


@image_comparison(baseline_images=['beeswarm'], extensions=['png'])
def test_beeswarm():
    # Set the random seed for consistency
    np.random.seed(123)
    data1 = np.random.normal(loc=1, size=(6,6), scale=0.2)
    data2 = np.random.normal(size=(6,6), scale=0.2)
    
    fig, ax = plt.subplots()
    ppl.beeswarm([data1, data2], \
                 colors=[ppl.colors.set1[1], ppl.colors.set1[2]], \
                 xticklabels=["data1", "data2"])
    ax.set_ylabel("Mean")
    # fig.savefig('%s/baseline_images/test_boxplot/boxplot.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])
