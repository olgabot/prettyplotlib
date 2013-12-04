#!/usr/bin/env python

import collections

import matplotlib as mpl
import matplotlib.pyplot as plt
import brewer2mpl
import numpy as np

from _bar import bar
from _boxplot import boxplot
from _hist import hist
from _legend import legend
from _plot import plot
from _pcolormesh import pcolormesh
from _scatter import scatter
from _remove_chartjunk import remove_chartjunk


# Get Set2 from ColorBrewer, a set of colors deemed colorblind-safe and
# pleasant to look at by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. These colors look lovely together, and are less
# saturated than those colors in Set1. For more on ColorBrewer, see:
# - Flash-based interactive map:
#     http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
#     http://bl.ocks.org/mbostock/5577023
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Another ColorBrewer scale. This one has nice "traditional" colors like
# reds and blues
set1 = brewer2mpl.get_map('Set1', 'qualitative', 9).mpl_colors

# Set some commonly used colors
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

reds = mpl.cm.Reds
reds.set_bad('white')
reds.set_under('white')

blues_r = mpl.cm.Blues_r
blues_r.set_bad('white')
blues_r.set_under('white')

# Need to 'reverse' red to blue so that blue=cold=small numbers,
# and red=hot=large numbers with '_r' suffix
blue_red = brewer2mpl.get_map('RdBu', 'Diverging', 11,
                              reverse=True).mpl_colormap


# --- Set a bunch of matplotlib parameters --- #
#mpl.rcParams['axes.color_cycle'] = set2
#
## Default "patches" like scatterplots
#mpl.rcParams['patch.linewidth'] = 0.75     # edge width in points
#
## Default empty circle with a colored outline
#mpl.rcParams['patch.facecolor'] = 'none'
#mpl.rcParams['patch.edgecolor'] = almost_black
#
## Change the default axis colors from black to a slightly lighter black,
## and a little thinner (0.5 instead of 1)
#mpl.rcParams['axes.edgecolor'] = almost_black
#mpl.rcParams['axes.labelcolor'] = almost_black
#mpl.rcParams['axes.linewidth'] = 0.5
#
## Make the default grid be white so it "removes" lines rather than adds
#mpl.rcParams['grid.color'] = 'white'
#
## change the tick colors also to the almost black
#mpl.rcParams['ytick.color'] = almost_black
#mpl.rcParams['xtick.color'] = almost_black
#
## change the text colors also to the almost black
#mpl.rcParams['text.color'] = almost_black




def scatter_column(ax, x, **kwargs):
    """
    Creates a boxplot-like 'scatter column' which is like a boxplot, though
    it plots the values of
    """
    pass


def switch_axis_limits(ax, which_axis):
    '''
    Switch the axis limits of either x or y. Or both!
    '''
    for a in which_axis:
        assert a in ('x', 'y')
        ax_limits = ax.axis()
        if a == 'x':
            ax.set_xlim(ax_limits[1], ax_limits[0])
        else:
            ax.set_ylim(ax_limits[3], ax_limits[2])


def upside_down_hist(ax, x, **kwargs):
    hist(ax, x, **kwargs)

    # Turn the histogram upside-down by switching the y-axis limits
    switch_axis_limits(ax, 'y')
    remove_chartjunk(ax, ['bottom', 'right'], grid='y', ticklabels='x')


def sideways_hist(ax, y, **kwargs):
    hist(ax, y, orientation='horizontal', **kwargs)

    # Orient the histogram with `0` counts on the right and the max
    # counts on the left by switching the `x` axis limits
    switch_axis_limits(ax, 'x')
    remove_chartjunk(ax, ['left', 'top'], grid='x', ticklabels='y')

