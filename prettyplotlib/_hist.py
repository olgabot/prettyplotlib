__author__ = 'olga'

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax


def hist(*args, **kwargs):
    """
    Plots a histogram of the provided data. Can provide optional argument
    "grid='x'" or "grid='y'" to draw a white grid over the histogram. Almost like "erasing" some of the plot,
     but it adds more information!
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)

    color_cycle = ax._get_lines.color_cycle
    color = next(color_cycle)
    # Reassign the default colors to Set2 by Colorbrewer
    if 'color' not in kwargs:
        kwargs['color'] = color
    if 'facecolor' not in kwargs:
        kwargs['facecolor'] = color
    if 'edgecolor' not in kwargs:
        kwargs['edgecolor'] = 'white'
    show_ticks = kwargs.pop('show_ticks', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    # print 'hist kwargs', kwargs
    patches = ax.hist(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], grid=grid, show_ticks=show_ticks)
    return ax
