__author__ = 'olga'

from matplotlib.cbook import iterable

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import pretty


@pretty
def hist(*args, **kwargs):
    """
    Plots a histogram of the provided data. Can provide optional argument
    "grid='x'" or "grid='y'" to draw a white grid over the histogram. Almost like "erasing" some of the plot,
     but it adds more information!
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)

    color_cycle = ax._get_lines.color_cycle
    # Reassign the default colors to Set2 by Colorbrewer
    if iterable(args[0]):
        if isinstance(args[0], list):
            ncolors = len(args[0])
        else:
            if len(args[0].shape) == 2:
                ncolors = args[0].shape[1]
            else:
                ncolors = 1
        kwargs.setdefault('color', [next(color_cycle) for _ in range(ncolors)])
    else:
        kwargs.setdefault('color', next(color_cycle))
    kwargs.setdefault('edgecolor', 'white')
    show_ticks = kwargs.pop('show_ticks', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    # print 'hist kwargs', kwargs
    patches = ax.hist(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], grid=grid, show_ticks=show_ticks)
    return patches
