import collections

import numpy as np

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import set2, almost_black


def bar(*args, **kwargs):
    """
    Creates a bar plot, with white outlines and a fill color that defaults to
     the first teal-ish green in ColorBrewer's Set2. Optionally accepts
     grid='y' or grid='x' to draw a white grid over the bars,
     to show the scale. Almost like "erasing" some of the plot,
     but it adds more information!

    Can also add an annotation of the height of the barplots directly onto
    the bars with the `annotate` parameter, which can either be True,
    which will annotate the values, or a list of strings, which will annotate
    with the supplied strings.

    @param ax: matplotlib.axes instance
    @param left: Vector of values of where to put the left side of the bar
    @param height: Vector of values of the bar heights
    @param kwargs: Besides xticklabels, which is a prettyplotlib-specific
    argument, any additional arguments to matplotlib.bar(): http://matplotlib
    .org/api/axes_api.html#matplotlib.axes.Axes.bar is accepted.
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    if 'color' not in kwargs:
        kwargs['color'] = set2[0]
    if 'edgecolor' not in kwargs:
        kwargs['edgecolor'] = 'white'
    if 'width' in kwargs:
        # Find the middle of the bar
        middle = kwargs['width']/2.0
    else:
        middle = 0.4

    left = args[0]
    height = args[1]

    # Label each individual bar, if xticklabels is provided
    xtickabels = kwargs.pop('xticklabels', None)
    # left+0.4 is the center of the bar
    xticks = np.array(left) + middle

    # Whether or not to annotate each bar with the height value
    annotate = kwargs.pop('annotate', False)

    show_ticks = kwargs.pop('show_ticks', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    rectangles = ax.bar(left, height, **kwargs)

    # add whitespace padding on left
    xmin, xmax = ax.get_xlim()
    xmin -= 0.2
    ax.set_xlim(xmin, xmax)

    # If the user is only plotting one bar, make it an iterable
    if not isinstance(height, collections.Iterable):
        height = [height]


    # If there are negative counts, remove the bottom axes
    # and add a line at y=0
    if any(h < 0 for h in height):
        axes_to_remove = ['top', 'right', 'bottom']
        ax.hlines(y=0, xmin=xmin, xmax=xmax,
                  linewidths=0.75)
    else:
        axes_to_remove = ['top', 'right']

    # Remove excess axes
    remove_chartjunk(ax, axes_to_remove, grid=grid, show_ticks=show_ticks)

    # Add the xticklabels if they are there
    if xtickabels is not None:
        ax.set_xticks(xticks)
        ax.set_xticklabels(xtickabels)

    if annotate or isinstance(annotate, collections.Iterable):
        annotate_yrange_factor = 0.025
        ymin, ymax = ax.get_ylim()
        yrange = ymax - ymin

        # Reset ymax and ymin so there's enough room to see the annotation of
        # the top-most
        if ymax > 0:
            ymax += yrange * 0.1
        if ymin < 0:
            ymin -= yrange * 0.1
        ax.set_ylim(ymin, ymax)
        yrange = ymax - ymin

        offset_ = yrange * annotate_yrange_factor
        if isinstance(annotate, collections.Iterable):
            annotations = map(str, annotate)
        else:
            annotations = ['%.3f' % h if type(h) is np.float_ else str(h)
                           for h in height]
        for x, h, annotation in zip(xticks, height, annotations):
            # Adjust the offset to account for negative bars
            offset = offset_ if h >= 0 else -1 * offset_
            verticalalignment = 'bottom' if h >= 0 else 'top'

            # Finally, add the text to the axes
            ax.annotate(annotation, (x, h + offset),
                        verticalalignment=verticalalignment,
                        horizontalalignment='center',
                        color=almost_black)
    return rectangles
