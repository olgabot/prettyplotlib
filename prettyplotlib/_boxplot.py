__author__ = 'olga'

import matplotlib as mpl
import matplotlib.pyplot as plt
from prettyplotlib import remove_chartjunk


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
    if isinstance(args[0], mpl.axes.Axes):
        ax = args.pop(0)
    elif 'ax' in kwargs:
        ax = kwargs['ax']
    else:
        ax = plt.gca()
        # If no ticklabels are specified, don't draw any
    xticklabels = kwargs.pop('xticklabels', None)
    fontsize = kwargs.pop('fontsize', 10)

    if 'widths' not in kwargs:
        kwargs['widths'] = 0.15
    bp = ax.boxplot(*args, **kwargs)
    if xticklabels:
        ax.xaxis.set_ticklabels(xticklabels, fontsize=fontsize)

    show_caps = kwargs.pop('show_caps', True)
    show_ticks = kwargs.pop('show_ticks', False)

    remove_chartjunk(ax, ['top', 'right', 'bottom'], show_ticks=show_ticks)
    linewidth = 0.75

    plt.setp(bp['boxes'], color=set1[1], linewidth=linewidth)
    plt.setp(bp['medians'], color=set1[0])
    plt.setp(bp['whiskers'], color=set1[1], linestyle='solid',
             linewidth=linewidth)
    plt.setp(bp['fliers'], color=set1[1])
    if show_caps:
        plt.setp(bp['caps'], color=set1[1], linewidth=linewidth)
    else:
        plt.setp(bp['caps'], color='none')
    ax.spines['left']._linewidth = 0.5
    return bp, ax
