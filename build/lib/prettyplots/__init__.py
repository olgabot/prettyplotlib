#!/usr/bin/env python

import matplotlib as mpl

def ax_prettify(ax, spines_to_remove, grid=None, remove_ticklabels=None):
    '''
    Removes "chartjunk", such as extra lines of axes and tick marks.

    If grid="y" or "x", will add a white grid at the "y" or "x" axes, 
    respectively

    If remove_ticklabels="y" or "x", will remove ticklabels from that axis
    '''
    # --- Added this line --- #
    for spine in spines_to_remove:
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
            for p in pos.difference(spines_to_remove):
                axis.set_ticks_position(p)
#                axis.set_tick_params(which='both', p)
        else:
            axis.set_ticks_position('none')

    if grid is not None:
        assert grid in ('x', 'y')
        ax.grid(axis=grid, color='white', linestyle='-')
        
    if remove_ticklabels is not None:
        assert remove_ticklabels in ('x', 'y')
        if remove_ticklabels == 'x':
            ax.set_xticklabels([])
        else:
            ax.set_yticklabels([])\


def hist(ax, x, **kwargs):
    ax.hist(x, edgecolor='white', **kwargs)
    
def upside_down_hist(ax, x, **kwargs):
    pretty_hist(ax, x, **kwargs)
    
    # Turn the histogram upside-down by switching the y-axis limits
    switch_axis_limits(ax, 'y')
    ax_prettify(ax, ['bottom', 'right'], grid='y', remove_ticklabels='x')

def sideways_hist(ax, y, **kwargs):
    pretty_hist(ax, y, orientation='horizontal', **kwargs)
    
    # Orient the histogram with `0` counts on the right and the max
    # counts on the left by switching the `x` axis limits
    switch_axis_limits(ax, 'x')
    ax_prettify(ax, ['left', 'top'], grid='x', remove_ticklabels='y')
