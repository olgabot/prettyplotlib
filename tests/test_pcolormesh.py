__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import os
import string
from prettyplotlib import brewer2mpl


@image_comparison(baseline_images=['pcolormesh'], extensions=['png'])
def test_pcolormesh():
    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.randn(10, 10))
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['pcolormesh_labels'], extensions=['png'])
def test_pcolormesh_labels():
    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.randn(10, 10),
                   xticklabels=string.uppercase[:10],
                   yticklabels=string.lowercase[-10:])
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh_labels.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['pcolormesh_positive'], extensions=['png'])
def test_pcolormesh_positive():
    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.uniform(size=(10, 10)),
                   xticklabels=string.uppercase[:10],
                   yticklabels=string.lowercase[-10:])
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh_positive.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['pcolormesh_positive_other_cmap'],
                  extensions=['png'])
def test_pcolormesh_positive_other_cmap():
    red_purple = brewer2mpl.get_map('RdPu', 'sequential', 8).mpl_colormap

    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.uniform(size=(10, 10)),
                   xticklabels=string.uppercase[:10],
                   yticklabels=string.lowercase[-10:],
                   cmap=red_purple)
    # fig.savefig(
    #     '%s/baseline_images/test_pcolormesh/pcolormesh_positive_other_cmap.png' %
    #     os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])