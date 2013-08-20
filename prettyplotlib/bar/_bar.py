__author__ = 'olga'

# Only export bar
__all__ = ['bar']

from prettyplotlib.common import *
from prettyplotlib import remove_chartjunk

def bar(ax, left, height, **kwargs):
    """
    Creates a bar plot, with white outlines and a fill color that defaults to
     the first teal-ish green in ColorBrewer's Set2. Optionally accepts
     grid='y' or grid='x' to draw a white grid over the bars,
     to show the scale. Almost like "erasing" some of the plot,
     but it adds more information!
    """
    if 'color' not in kwargs:
        kwargs['color'] = set2[0]
    if 'edgecolor' not in kwargs:
        kwargs['edgecolor'] = 'white'
    if 'grid' in kwargs:
        grid = kwargs['grid']
        kwargs.pop('grid')
    else:
        grid = None
    ax.bar(left, height, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], grid=grid)
