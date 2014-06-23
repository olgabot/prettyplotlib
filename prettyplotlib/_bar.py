import collections

import numpy as np

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import set2, almost_black, getcolors

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

    Can support stacked bars with the value of each stack shown on the stack
    (Added by Salil Banerjee)

    @param ax: matplotlib.axes instance
    @param left: Vector of values of where to put the left side of the bar
    @param height: Vector of values of the bar heights
    @param kwargs: Besides xticklabels, which is a prettyplotlib-specific
    argument, any additional arguments to matplotlib.bar(): http://matplotlib
    .org/api/axes_api.html#matplotlib.axes.Axes.bar is accepted.
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

    left = args[0]
    height = np.array(args[1])

    # Label each individual bar, if xticklabels is provided
    xtickabels = kwargs.pop('xticklabels', None)
    # left+0.4 is the center of the bar
    xticks = np.array(left) + middle

    # Whether or not to annotate each bar with the height value
    annotate = kwargs.pop('annotate', False)

    show_ticks = kwargs.pop('show_ticks', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    cmap = kwargs.pop('cmap', False)
    if cmap:
        kwargs['edgecolor'] = almost_black
        if not stacked:
            kwargs['color'] = getcolors(cmap, height, 0)

    # Check if stacked and plot data accordingly
    color = kwargs.get('color', None)
    if stacked:
        num_stacks, num_data = height.shape
        bottom = np.zeros(num_data)
        for i in np.arange(num_stacks):
            lst = list(args)
            lst[1] = height[i]
            args = tuple(lst)
            # make sure number of user specified colors equals to the stacks 
            if not color or len(color) != num_stacks:
                if cmap:
                    kwargs['color'] = getcolors(cmap, height[i], i)
                else:
                    kwargs['color'] = set2[i]
            else:
                kwargs['color'] = color[i]
            kwargs['bottom'] = bottom
            rectangles = ax.bar(*args, **kwargs)
            bottom += height[i]
    else:
        rectangles = ax.bar(*args, **kwargs)
   
    # add legend
    if isinstance(legend, collections.Iterable):
        ax.legend(legend,loc='upper center',bbox_to_anchor=(0.5,1.11), ncol=5)

    # add whitespace padding on left
    xmin, xmax = ax.get_xlim()
    xmin -= 0.2
    if stacked:
        xmax = num_data
    ax.set_xlim(xmin, xmax)

    # If the user is only plotting one bar, make it an iterable
    if not isinstance(height, collections.Iterable):
        height = [height]


    # If there are negative counts, remove the bottom axes
    # and add a line at y=0
    if any(h < 0 for h in height.tolist()):
        axes_to_remove = ['top', 'right', 'bottom']
        ax.hlines(y=0, xmin=xmin, xmax=xmax,
                      linewidths=0.75)
    else:
        axes_to_remove = ['top', 'right']

    # Remove excess axes
    remove_chartjunk(ax, axes_to_remove, grid=grid, show_ticks=show_ticks)

    if stacked:
        data = height
        height = height.sum(axis=0)

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

        if kwargs.get('log') == True:
            offset_ = np.log(yrange) * annotate_yrange_factor
        else:
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

    # Text for each block of stack
    # This was partially inspired by the following article by Tableau software
    # http://www.tableausoftware.com/about/blog/2014/1/new-whitepaper-survey-data-less-ugly-more-understandable-27812
    if stack_text:
        bottom = np.zeros(num_data)
        max_h = max(height)
        for i in np.arange(num_stacks):
            for x, d, b in zip(xticks, data[i], bottom):
                if (d*100.0/max_h) > 4.0:
                    ax.text(x,b+d/2.0,d, ha='center', va='center', color=almost_black)
            bottom += data[i]
    return rectangles
