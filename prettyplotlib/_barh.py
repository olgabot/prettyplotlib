__author__ = 'olga'

from prettyplotlib.utils import maybe_get_ax, remove_chartjunk
from prettyplotlib.colors import set2, almost_black, getcolors
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

    Can support stacked bars with the value of each stack shown on the stack
    (Added by Salil Banerjee)

    @param ax: matplotlib.axes instance
    @param top: Vector of values of where to put the top side of the bar
    @param width: Vector of values of the bar widths
    @param ytickabels: Vector of labels of the bar widths
    @param kwargs: Any additional arguments to matplotlib.bar()
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    kwargs.setdefault('color', set2[0])
    kwargs.setdefault('edgecolor', 'white')
    middle = 0.4 if 'width' not in kwargs else kwargs['width']/2.0

    # Check if data contains stacks
    stacked = kwargs.pop('stacked',False)
    # Check if stack text should be included
    stack_text = kwargs.pop('stack_text',False)
    # Get legend if available
    legend = kwargs.pop('legend',False)

    top = args[0]
    width = np.array(args[1])

    # Label each individual bar, if xticklabels is provided
    ytickabels = kwargs.pop('yticklabels', None)
    # left+0.4 is the center of the bar
    yticks = np.array(top) + middle

    # Whether or not to annotate each bar with the width value
    annotate = kwargs.pop('annotate', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    cmap = kwargs.pop('cmap', False)
    if cmap:
        kwargs['edgecolor'] = almost_black
        if not stacked:
            kwargs['color'] = getcolors(cmap, width, 0)

    # Check if stacked and plot data accordingly
    if stacked:
        num_stacks, num_data = width.shape
        left = np.zeros(num_data)
        for i in np.arange(num_stacks):
            lst = list(args)
            lst[1] = width[i]
            args = tuple(lst)
            if cmap:
                kwargs['color'] = getcolors(cmap, width[i], i)
            else:
                kwargs['color'] = set2[i]
            kwargs['left'] = left
            rectangles = ax.barh(*args, **kwargs)
            left += width[i]
    else:
        rectangles = ax.barh(*args, **kwargs)

    # add legend
    if isinstance(legend, collections.Iterable):
        ax.legend(legend,loc='upper center',bbox_to_anchor=(0.5,1.11), ncol=5)

    # add whitespace padding on left
    ymin, ymax = ax.get_ylim()
    ymin -= 0.2
    if stacked:
        ymax = num_data
    ax.set_ylim(ymin, ymax)

    # If there are negative counts, remove the bottom axes
    # and add a line at y=0
    if any(w < 0 for w in width.tolist()):
        axes_to_remove = ['top', 'right', 'bottom']
        ax.vlines(x=0, ymin=ymin, ymax=ymax,
                  linewidths=0.75)
       #ax.hlines(y=0, xmin=xmin, xmax=xmax,
       #       linewidths=0.75)
    else:
        axes_to_remove = ['top', 'right']

    #Remove excess axes
    remove_chartjunk(ax, axes_to_remove, grid=grid)

    if stacked:
        data = width
        width = width.sum(axis=0)

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
        for y, w, annotation in zip(yticks, width, annotations):
            # Adjust the offset to account for negative bars
            offset = offset_ if w >= 0 else -1 * offset_
            # Finally, add the text to the axes
            ax.annotate(annotation, (w + offset, y),
                        verticalalignment='center',
                        horizontalalignment='center',
                        color=almost_black)

    # Text for each block of stack
    # This was partially inspired by the following article by Tableau software
    # http://www.tableausoftware.com/about/blog/2014/1/new-whitepaper-survey-data-less-ugly-more-understandable-27812
    if stack_text:
        left = np.zeros(num_data)
        max_w = max(width)
        for i in np.arange(num_stacks):
            for y, d, l in zip(yticks, data[i], left):
                if (d*100.0/max_w) > 2.0:
                    ax.text(l+d/2.0,y,d, ha='center', va='center', color=almost_black)
            left += data[i]

    return rectangles
