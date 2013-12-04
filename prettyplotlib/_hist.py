__author__ = 'olga'

from prettyplotlib import remove_chartjunk

def hist(ax, x, **kwargs):
    """
    Plots a histogram of the provided data. Can provide optional argument
    "grid='x'" or "grid='y'" to draw a white grid over the histogram. Almost like "erasing" some of the plot,
     but it adds more information!
    """
    # Reassign the default colors to Set2 by Colorbrewer
    color_cycle = ax._get_lines.color_cycle
    color = kwargs.pop('color', next(color_cycle))
    facecolor = kwargs.pop('facecolor', color)
    show_ticks = kwargs.pop('show_ticks', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    # print 'hist kwargs', kwargs
    patches = ax.hist(x, edgecolor='white', facecolor=facecolor, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], grid=grid, show_ticks=show_ticks)
    return patches
