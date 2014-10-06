#!/usr/bin/env python
from __future__ import absolute_import

import matplotlib as mpl
import brewer2mpl

from ._bar import bar
from ._barh import barh
from ._boxplot import boxplot
from ._beeswarm import beeswarm
from ._eventplot import eventplot
from ._hist import hist
from ._legend import legend
from ._plot import plot
from ._pcolormesh import pcolormesh
from ._scatter import scatter
from ._fill_between import fill_between
from ._fill_betweenx import fill_betweenx
from ._stackplot import stackplot
from .general import *

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

