#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt
import brewer2mpl

# Get Set2 from ColorBrewer, a set of colors deemed colorblind-safe and
# pleasant to look at by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. These colors look lovely together, and are less
# saturated than those colors in Set1. For more on ColorBrewer, see:
# - Flash-based interactive map:
#     http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
#     http://bl.ocks.org/mbostock/5577023
set2 = brewer2mpl.get_map('Set2', 'qualitative', 7).mpl_colors

# Another ColorBrewer scale. This one has nice "traditional" colors like
# reds and blues
set1 = brewer2mpl.get_map('Set1', 'qualitative', 7).mpl_colors


mpl.rcParams['axes.color_cycle'] = set2

def prettify(ax, remove_spines, grid=None, remove_ticklabels=None):
    '''
    Removes "chartjunk", such as extra lines of axes and tick marks.

    If grid="y" or "x", will add a white grid at the "y" or "x" axes, 
    respectively

    If remove_ticklabels="y" or "x", will remove ticklabels from that axis
    '''
    # --- Added this line --- #)
    for spine in remove_spines:
        ax.spines[spine].set_visible(False)
    # Check that the axes are not log-scale. If they are, leave the ticks
    # because otherwise people assume a linear scale.
    x_pos = set(['top', 'bottom'])
    y_pos = set(['left', 'right'])
    xy_pos = [x_pos, y_pos]
    xy_ax_names = ['xaxis', 'yaxis']

    for ax_name, pos in zip(xy_ax_names, xy_pos):
        axis = ax.__dict__[ax_name]
        if type(axis.get_scale()) == 'log':
            for p in pos.difference(remove_spines):
                axis.set_ticks_position(p)
#                axis.set_tick_params(which='both', p)
        else:
            axis.set_ticks_position('none')

    if grid is not None:
        assert grid in ('x', 'y')
        ax.grid(axis=grid, color='white', linestyle='-', linewidth=0.5)
        
    if remove_ticklabels is not None:
        assert set(remove_ticklabels) in set(('x', 'y'))
        if 'x' in remove_ticklabels:
            ax.set_xticklabels([])
        elif 'y' in remove_ticklabels:
            ax.set_yticklabels([])


def hist(ax, x, **kwargs):
# Reassign the default colors to Set2 by Colorbrewer
    ax.hist(x, edgecolor='white', **kwargs)


def scatter(ax, x, y, **kwargs):
    color = set2[0] if 'color' not in kwargs else kwargs['color']
    ax.scatter(x, y, edgecolor='black', linewidth=0.15, color=color, **kwargs)

def bar(ax, left, height, xticklabels, **kwargs):
    color = set2[0] if 'color' not in kwargs else kwargs['color']
    ax.bar(left, height, edgecolor='white', color=color, **kwargs)
    prettify(ax, ['top', 'right'])

def boxplot(ax, x, xticklabels, **kwargs):
    bp = ax.boxplot(x, widths=0.15)
    ax.xaxis.set_ticklabels(xticklabels)

    prettify(ax, ['top', 'right', 'bottom'])

    plt.setp(bp['boxes'], color=set1[1], linewidth=0.5)
    plt.setp(bp['medians'], color=set1[0])
    plt.setp(bp['whiskers'], color=set1[1], linestyle='solid', linewidth=0.5)
    plt.setp(bp['fliers'], color=set1[1])
    plt.setp(bp['caps'], color='none')
    ax.spines['left']._linewidth = 0.5

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
    prettify(ax, ['bottom', 'right'], grid='y', remove_ticklabels='x')

def sideways_hist(ax, y, **kwargs):
    hist(ax, y, orientation='horizontal', **kwargs)
    
    # Orient the histogram with `0` counts on the right and the max
    # counts on the left by switching the `x` axis limits
    switch_axis_limits(ax, 'x')
    prettify(ax, ['left', 'top'], grid='x', remove_ticklabels='y')


# import matplotlib.pyplot as plt
# import prettyplotlib as ppl
#
# fig, ax = plt.subplots(1)
# ppl.scatter(ax, x, y)