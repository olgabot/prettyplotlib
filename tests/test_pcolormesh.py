__author__ = 'olga'

from matplotlib.testing.decorators import image_comparison
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import os
import string
from prettyplotlib import brewer2mpl
from matplotlib.colors import LogNorm

import six

if six.PY3:
    LOWERCASE_CHARS = string.ascii_lowercase
    UPPERCASE_CHARS = string.ascii_uppercase
else:
    LOWERCASE_CHARS = LOWERCASE_CHARS
    UPPERCASE_CHARS = UPPERCASE_CHARS


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
                   xticklabels=UPPERCASE_CHARS[:10],
                   yticklabels=LOWERCASE_CHARS[-10:])
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh_labels.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['pcolormesh_positive'], extensions=['png'])
def test_pcolormesh_positive():
    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.uniform(size=(10, 10)),
                   xticklabels=UPPERCASE_CHARS[:10],
                   yticklabels=LOWERCASE_CHARS[-10:])
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh_positive.png' %
    #             os.path.dirname(__file__))

@image_comparison(baseline_images=['pcolormesh_negative'], extensions=['png'])
def test_pcolormesh_negative():
    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, -np.random.uniform(size=(10, 10)),
                   xticklabels=UPPERCASE_CHARS[:10],
                   yticklabels=LOWERCASE_CHARS[-10:])
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh_negative.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['pcolormesh_other_cmap'], extensions=['png'])
def test_pcolormesh_other_cmap():
    purple_green = brewer2mpl.get_map('PRGn', 'diverging', 11).mpl_colormap

    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.randn(10, 10), cmap=purple_green)
    # fig.savefig('%s/baseline_images/test_pcolormesh/pcolormesh_other_cmap.png' %
    #             os.path.dirname(__file__))


@image_comparison(baseline_images=['pcolormesh_positive_other_cmap'],
                  extensions=['png'])
def test_pcolormesh_positive_other_cmap():
    red_purple = brewer2mpl.get_map('RdPu', 'sequential', 8).mpl_colormap

    fig, ax = plt.subplots(1)

    np.random.seed(10)

    ppl.pcolormesh(fig, ax, np.random.uniform(size=(10, 10)),
                   xticklabels=UPPERCASE_CHARS[:10],
                   yticklabels=LOWERCASE_CHARS[-10:],
                   cmap=red_purple)
    # fig.savefig(
    #     '%s/baseline_images/test_pcolormesh/pcolormesh_positive_other_cmap.png' %
    #     os.path.dirname(__file__))

@image_comparison(baseline_images=['pcolormesh_lognorm'],
                  extensions=['png'])
def test_pcolormesh_lognorm():
    fig, ax = plt.subplots(1)

    np.random.seed(10)

    x = np.abs(np.random.randn(10, 10))
    ppl.pcolormesh(fig, ax, x,
                   norm=LogNorm(vmin=x.min().min(), vmax=x.max().max()))
    # fig.savefig('%s/baseline_images/test_pcolormesh/test_pcolormesh_lognorm.png' %
    #             os.path.dirname(__file__))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'])
