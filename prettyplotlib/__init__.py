#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt
import brewer2mpl
import numpy as np
import sys
import collections

# Get Set2 from ColorBrewer, a set of colors deemed colorblind-safe and
# pleasant to look at by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. These colors look lovely together, and are less
# saturated than those colors in Set1. For more on ColorBrewer, see:
# - Flash-based interactive map:
#     http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
#     http://bl.ocks.org/mbostock/5577023
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Another ColorBrewer scale. This one has nice "traditional" colors like
# reds and blues
set1 = brewer2mpl.get_map('Set1', 'qualitative', 9).mpl_colors
mpl.rcParams['axes.color_cycle'] = set2

# Set some commonly used colors
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

reds = mpl.cm.Reds
reds.set_bad('white')
reds.set_under('white')

blues_r = mpl.cm.Blues_r
blues_r.set_bad('white')
blues_r.set_under('white')

# Need to 'reverse' red to blue so that blue=cold=small numbers,
# and red=hot=large numbers with '_r' suffix
blue_red = brewer2mpl.get_map('RdBu', 'Diverging', 11,
                              reverse=True).mpl_colormap

# Default "patches" like scatterplots
mpl.rcParams['patch.linewidth'] = 0.75     # edge width in points

# Default empty circle with a colored outline
mpl.rcParams['patch.facecolor'] = 'none'
mpl.rcParams['patch.edgecolor'] = set2[0]

# Change the default axis colors from black to a slightly lighter black,
# and a little thinner (0.5 instead of 1)
mpl.rcParams['axes.edgecolor'] = almost_black
mpl.rcParams['axes.labelcolor'] = almost_black
mpl.rcParams['axes.linewidth'] = 0.5

# Make the default grid be white so it "removes" lines rather than adds
mpl.rcParams['grid.color'] = 'white'

# change the tick colors also to the almost black
mpl.rcParams['ytick.color'] = almost_black
mpl.rcParams['xtick.color'] = almost_black

# change the text colors also to the almost black
mpl.rcParams['text.color'] = almost_black



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

    # Label each individual bar, if xticklabels is provided
    xtickabels = kwargs.pop('xticklabels', None)
    # left+0.4 is the center of the bar
    xticks = np.array(left) + 0.4

    # Whether or not to annotate each bar with the height value
    annotate = kwargs.pop('annotate', False)

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

    ax.bar(left, height, **kwargs)

    # add whitespace padding on left
    xmin, xmax = ax.get_xlim()
    xmin -= 0.2
    ax.set_xlim(xmin, xmax)

    # If there are negative counts, remove the bottom axes
    # and add a line at y=0
    if sum(h < 0 for h in height) > 0:
        axes_to_remove = ['top', 'right', 'bottom']
        ax.hlines(y=0, xmin=xmin, xmax=xmax,
                  linewidths=0.75)
    else:
        axes_to_remove = ['top', 'right']

    # Remove excess axes
    remove_chartjunk(ax, axes_to_remove, grid=grid)

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
            ymax += yrange*0.1
        if ymin < 0:
            ymin -= yrange*0.1
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
            offset = offset_ if h >= 0 else -1*offset_
            verticalalignment = 'bottom' if h >= 0 else 'top'

            # Finally, add the text to the axes
            ax.annotate(annotation, (x, h + offset),
                        verticalalignment=verticalalignment,
                        horizontalalignment='center',
                        color=almost_black)


def boxplot(ax, x, **kwargs):
    # If no ticklabels are specified, don't draw any
    xticklabels = kwargs.pop('xticklabels', None)

    if 'widths' not in kwargs:
        kwargs['widths'] = 0.15
    bp = ax.boxplot(x, **kwargs)
    if xticklabels:
        ax.xaxis.set_ticklabels(xticklabels)

    remove_chartjunk(ax, ['top', 'right', 'bottom'])

    plt.setp(bp['boxes'], color=set1[1], linewidth=0.5)
    plt.setp(bp['medians'], color=set1[0])
    plt.setp(bp['whiskers'], color=set1[1], linestyle='solid', linewidth=0.5)
    plt.setp(bp['fliers'], color=set1[1])
    plt.setp(bp['caps'], color='none')
    ax.spines['left']._linewidth = 0.5


def hist(ax, x, **kwargs):
    """
    Plots a histogram of the provided data. Can provide optional argument
    "grid='x'" or "grid='y'" to draw a white grid over the histogram. Almost like "erasing" some of the plot,
     but it adds more information!
    """
    # Reassign the default colors to Set2 by Colorbrewer
    if 'color' not in kwargs:
        kwargs['color'] = set2[0]

    # If no grid specified, don't draw one.
    grid = kwargs.pop('grid', None)

        # print 'hist kwargs', kwargs
    ax.hist(x, edgecolor='white', **kwargs)
    remove_chartjunk(ax, ['top', 'right'], grid=grid)

def legend(ax, facecolor=light_grey, **kwargs):
    legend = ax.legend(frameon=True, scatterpoints=1, **kwargs)
    rect = legend.get_frame()
    rect.set_facecolor(facecolor)
    rect.set_linewidth(0.0)

    # change the label colors in the legend to almost black
    # Change the legend label colors to almost black, too
    texts = legend.texts
    for t in texts:
        t.set_color(almost_black)

        # import matplotlib.pyplot as plt
        # import prettyplotlib as ppl
        #
        # fig, ax = plt.subplots(1)
        # ppl.scatter(ax, x, y)

def plot(ax, x, y, **kwargs):
    if 'color' in kwargs:
        color = kwargs['color']
        # Remove the other color argument so matplotlib doesn't complain
        kwargs.pop('color')
    else:
        # if no color is specified, cycle over the ones in this axis
        color_cycle = ax._get_lines.color_cycle
        color = color_cycle.next()
    if 'linewidth' not in kwargs:
        kwargs['linewidth'] = 0.75

    ax.plot(x, y, color=color, **kwargs)
    remove_chartjunk(ax, ['top', 'right'])


def scatter(ax, x, y, **kwargs):
    """
    This will plot a scatterplot of x and y, iterating over the ColorBrewer
    "Set2" color cycle unless a color is specified. The symbols produced are
    empty circles, with the outline in the color specified by either 'color'
    or 'edgecolor'. If you want to fill the circle, specify 'facecolor'.
    """
    # Force 'color' to indicate the edge color, so the middle of the
    # scatter patches are empty. Can speficy
    if 'edgecolor' not in kwargs:
        kwargs['edgecolor'] = almost_black
    if 'color' not in kwargs:
        # Assume that color means the edge color. You can assign the
        color_cycle = ax._get_lines.color_cycle
        kwargs['color'] = color_cycle.next()
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.5
    if 'linewidth' not in kwargs:
        kwargs['linewidth'] = 0.15

    ax.scatter(x, y, **kwargs)
    remove_chartjunk(ax, ['top', 'right'])






def switch_axis_limits(ax, which_axis=('x', 'y')):
    '''
    Switch the axis limits of either x or y
    '''
    assert which_axis in ('x', 'y')
    ax_limits = ax.axis()
    if which_axis == 'x':
        ax.set_xlim(ax_limits[1], ax_limits[0])
    else:
        ax.set_ylim(ax_limits[3], ax_limits[2])


def upside_down_hist(ax, x, **kwargs):
    hist(ax, x, **kwargs)

    # Turn the histogram upside-down by switching the y-axis limits
    switch_axis_limits(ax, 'y')
    remove_chartjunk(ax, ['bottom', 'right'], grid='y', ticklabels='x')


def sideways_hist(ax, y, **kwargs):
    hist(ax, y, orientation='horizontal', **kwargs)

    # Orient the histogram with `0` counts on the right and the max
    # counts on the left by switching the `x` axis limits
    switch_axis_limits(ax, 'x')
    remove_chartjunk(ax, ['left', 'top'], grid='x', ticklabels='y')

# TODO: Heatmap-style figures. Default colormap = Blues. Check if the data
# has both negative and positive values. If so, then use blue (negative)-red
# (positive) heatmap

def pcolormesh(fig, ax, x, **kwargs):
    """
    Use for large datasets

    Non-traditional `pcolormesh` kwargs are:
    - xticklabels, which will put x tick labels exactly in the center of the
    heatmap block
    - yticklables, which will put y tick labels exactly aligned in the center
     of the heatmap block
     - xticklabels_rotation, which can be either 'horizontal' or 'vertical'
     depending on how you want the xticklabels rotated. The default is
     'horiztonal' but if you have xticklabels that are longer, you may want
     to do 'vertical' so they don't overlap
     - yticklabels_rotation, which can also be either 'horizontal' or
     'vertical'. The default is 'horizontal' and in most cases,
     that's what you'll want to stick with. But the option is there if you
     want.
    """
    # Deal with arguments in kwargs that should be there, or need to be taken
    #  out
    if 'vmax' not in kwargs:
        kwargs['vmax'] = x.max()
    if 'vmin' not in kwargs:
        kwargs['vmin'] = x.min()

    # If we have both negative and positive values, use a divergent colormap
    if 'cmap' not in kwargs:
        if kwargs['vmax'] > 0 and kwargs['vmin'] < 0:
            kwargs['cmap'] = blue_red
        elif kwargs['vmax'] <= 0:
            kwargs['cmap'] = blues_r
        elif kwargs['vmax'] > 0:
            kwargs['cmap'] = reds

    if 'xticklabels' in kwargs:
        xticklabels = kwargs['xticklabels']
        kwargs.pop('xticklabels')
    else:
        xticklabels = None
    if 'yticklabels' in kwargs:
        yticklabels = kwargs['yticklabels']
        kwargs.pop('yticklabels')
    else:
        yticklabels = None

    if 'xticklabels_rotation' in kwargs:
        xticklabels_rotation = kwargs['xticklabels_rotation']
        kwargs.pop('xticklabels_rotation')
    else:
        xticklabels_rotation = 'horizontal'
    if 'yticklabels_rotation' in kwargs:
        yticklabels_rotation = kwargs['yticklabels_rotation']
        kwargs.pop('yticklabels_rotation')
    else:
        yticklabels_rotation = 'horizontal'
    p = ax.pcolormesh(x, **kwargs)
    ax.set_ylim(0, x.shape[0])

    # Get rid of ALL axes
    remove_chartjunk(ax, ['top', 'right', 'left', 'bottom'])

    if xticklabels:
        xticks = np.arange(0.5, x.shape[1] + 0.5)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, rotation=xticklabels_rotation)
    if yticklabels:
        yticks = np.arange(0.5, x.shape[0] + 0.5)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels, rotation=yticklabels_rotation)
        # Show the scale of the colorbar
    fig.colorbar(p)

def remove_chartjunk(ax, spines, grid=None, ticklabels=None):
    '''
    Removes "chartjunk", such as extra lines of axes and tick marks.

    If grid="y" or "x", will add a white grid at the "y" or "x" axes,
    respectively

    If ticklabels="y" or "x", or ['x', 'y'] will remove ticklabels from that
    axis
    '''
    all_spines = ['top', 'bottom', 'right', 'left']
    for spine in spines:
        ax.spines[spine].set_visible(False)

    # For the remaining spines, make their line thinner and a slightly
    # off-black dark grey
    for spine in all_spines:
        if spine not in spines:
            ax.spines[spine].set_linewidth(0.5)
            # ax.spines[spine].set_color(almost_black)
        #            ax.spines[spine].set_tick_params(color=almost_black)
        # Check that the axes are not log-scale. If they are, leave the ticks
    # because otherwise people assume a linear scale.
    x_pos = set(['top', 'bottom'])
    y_pos = set(['left', 'right'])
    xy_pos = [x_pos, y_pos]
    xy_ax_names = ['xaxis', 'yaxis']

    for ax_name, pos in zip(xy_ax_names, xy_pos):
        axis = ax.__dict__[ax_name]
        # axis.set_tick_params(color=almost_black)
        if type(axis.get_scale()) == 'log':
            # if this spine is not in the list of spines to remove
            for p in pos.difference(spines):
                axis.set_ticks_position(p)
            #                axis.set_tick_params(which='both', p)
        else:
            axis.set_ticks_position('none')

    if grid is not None:
        assert grid in ('x', 'y')
        ax.grid(axis=grid, color='white', linestyle='-', linewidth=0.5)

    if ticklabels is not None:
        if type(ticklabels) is str:
            assert ticklabels in set(('x'   , 'y'))
            if ticklabels == 'x':
                ax.set_xticklabels([])
            if ticklabels == 'y':
                ax.set_yticklabels([])
        else:
            assert set(ticklabels) | set(('x', 'y')) > 0
            if 'x' in ticklabels:
                ax.set_xticklabels([])
            elif 'y' in ticklabels:
                ax.set_yticklabels([])
