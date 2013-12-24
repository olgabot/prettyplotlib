__author__ = 'olga'

from prettyplotlib.utils import maybe_get_ax, remove_chartjunk
from prettyplotlib.colors import set2, almost_black
import numpy as np
import collections

def barh(*args, **kwargs):
    """
    Creates a bar plot, with white outlines and a fill color that defaults to
     the first teal-ish green in ColorBrewer's Set2. Optionally accepts
     grid='y' or grid='x' to draw a white grid over the bars,
     to show the scale. Almost like "erasing" some of the plot,
     but it adds more information!

    Can also add an annotation of the width of the barplots directly onto
    the bars with the `annotate` parameter, which can either be True,
    which will annotate the values, or a list of strings, which will annotate
    with the supplied strings.

    @param ax: matplotlib.axes instance
    @param top: Vector of values of where to put the top side of the bar
    @param width: Vector of values of the bar widths
    @param ytickabels: Vector of labels of the bar widths
    @param kwargs: Any additional arguments to matplotlib.bar()
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

    top = args[0]
    width = args[1]

    # Label each individual bar, if xticklabels is provided
    ytickabels = kwargs.pop('yticklabels', None)
    # left+0.4 is the center of the bar
    yticks = np.array(top) + middle

    # Whether or not to annotate each bar with the width value
    annotate = kwargs.pop('annotate', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    rectangles = ax.barh(*args, **kwargs)

    # add whitespace padding on left
    ymin, ymax = ax.get_ylim()
    ymin -= 0.2
    ax.set_ylim(ymin, ymax)

    # If there are negative counts, remove the bottom axes
    # and add a line at y=0
    if any(w < 0 for w in width):
        axes_to_remove = ['top', 'right', 'bottom']
        ax.vlines(x=0, ymin=ymin, ymax=ymax,
                  linewidths=0.75)
       #ax.hlines(y=0, xmin=xmin, xmax=xmax,
       #       linewidths=0.75)
    else:
        axes_to_remove = ['top', 'right']

    # Remove excess axes
    remove_chartjunk(ax, axes_to_remove, grid=grid)

    # Add the yticklabels if they are there
    if ytickabels is not None:
        ax.set_yticks(yticks)
        ax.set_yticklabels(ytickabels)

    if annotate or isinstance(annotate, collections.Iterable):
        annotate_xrange_factor = 0.050
        xmin, xmax = ax.get_xlim()
        xrange = xmax - xmin

        # Reset ymax and ymin so there's enough room to see the annotation of
        # the top-most
        if xmax > 0:
            xmax += xrange * 0.1
        if xmin < 0:
            xmin -= xrange * 0.1
        ax.set_xlim(xmin, xmax)
        xrange = xmax - xmin

        offset_ = xrange * annotate_xrange_factor
        if isinstance(annotate, collections.Iterable):
            annotations = map(str, annotate)
        else:
            annotations = ['%.3f' % w if type(w) is np.float_ else str(w)
                           for w in width]
        for x, w, annotation in zip(yticks, width, annotations):
            # Adjust the offset to account for negative bars
            offset = offset_ if w >= 0 else -1 * offset_
            verticalalignment = 'bottom' if w >= 0 else 'top'

            # Finally, add the text to the axes
            ax.annotate(annotation, (w + offset, x - offset),
                        verticalalignment=verticalalignment,
                        horizontalalignment='center',
                        color=almost_black)
    return ax