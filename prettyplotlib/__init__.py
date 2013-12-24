#!/usr/bin/env python


import brewer2mpl
import matplotlib as mpl

from _bar import bar
from _boxplot import boxplot
from _hist import hist
from _legend import legend
from _plot import plot
from _pcolormesh import pcolormesh
from _scatter import scatter

#from _remove_chartjunk import remove_chartjunk


rcParams = {'axes.color_cycle': brewer2mpl.get_map('Set2', 'Qualitative',
                                                   8).mpl_colors}
mpl.rcParams.update(rcParams)


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

