__author__ = 'olga'

import matplotlib.pyplot as plt
from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib import colors

def boxplot(*args, **kwargs):
    """
    Create a box-and-whisker plot showing the mean, 25th percentile, and 75th
    percentile. The difference from matplotlib is only the left axis line is
    shown, and ticklabels labeling each category of data can be added.

    @param ax:
    @param x:
    @param kwargs: Besides xticklabels, which is a prettyplotlib-specific
    argument which will label each individual boxplot, any argument for
    matplotlib.pyplot.boxplot will be accepted:
    http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.boxplot
    @return:
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    # If no ticklabels are specified, don't draw any
    xticklabels = kwargs.pop('xticklabels', None)
    fontsize = kwargs.pop('fontsize', 10)

    kwargs.setdefault('widths', 0.15)

    bp = ax.boxplot(*args, **kwargs)

    if xticklabels:
        ax.xaxis.set_ticklabels(xticklabels, fontsize=fontsize)

    show_caps = kwargs.pop('show_caps', True)
    show_ticks = kwargs.pop('show_ticks', False)

    remove_chartjunk(ax, ['top', 'right', 'bottom'], show_ticks=show_ticks)
    linewidth = 0.75

    blue = colors.set1[1]
    red = colors.set1[0]
    plt.setp(bp['boxes'], color=blue, linewidth=linewidth)
    plt.setp(bp['medians'], color=red)
    plt.setp(bp['whiskers'], color=blue, linestyle='solid',
             linewidth=linewidth)
    plt.setp(bp['fliers'], color=blue)
    if show_caps:
        plt.setp(bp['caps'], color=blue, linewidth=linewidth)
    else:
        plt.setp(bp['caps'], color='none')
    ax.spines['left']._linewidth = 0.5
    return bp 
