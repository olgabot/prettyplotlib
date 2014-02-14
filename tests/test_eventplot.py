__author__ = 'jgosmann'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
import numpy as np


@image_comparison(baseline_images=['eventplot'], extensions=['png'])
def test_plot():
    # Set the random seed for consistency
    np.random.seed(12)

    alpha = 0.5
    events = np.random.rand(10)
    ppl.eventplot(events, alpha=alpha)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])
