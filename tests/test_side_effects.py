__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
import numpy as np
import matplotlib.pyplot as plt

# Make sure that importing prettyplotlib has no side effects on the rcParams
# of matplotlib

@image_comparison(baseline_images=['side_effects'], extensions=['png'])
def test_side_effects():
    plt.plot((0,1), (0,1))
    # fig.savefig('%s/baseline_images/test_plot/plot.png' %
    #             os.path.dirname(__file__))

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])