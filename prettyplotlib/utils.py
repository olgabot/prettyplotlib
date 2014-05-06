__author__ = 'olga'

import matplotlib as mpl
import matplotlib.pyplot as plt


def remove_chartjunk(ax, spines, grid=None, ticklabels=None, show_ticks=False,
                     xkcd=False):
    '''
    Removes "chartjunk", such as extra lines of axes and tick marks.

    If grid="y" or "x", will add a white grid at the "y" or "x" axes,
    respectively

    If ticklabels="y" or "x", or ['x', 'y'] will remove ticklabels from that
    axis
    '''
    all_spines = ['top', 'bottom', 'right', 'left', 'polar']
    for spine in spines:
        # The try/except is for polar coordinates, which only have a 'polar'
        # spine and none of the others
        try:
            ax.spines[spine].set_visible(False)
        except KeyError:
            pass

    # For the remaining spines, make their line thinner and a slightly
    # off-black dark grey
    if not xkcd:
        for spine in set(all_spines).difference(set(spines)):
            # The try/except is for polar coordinates, which only have a
            # 'polar' spine and none of the others
            try:
                ax.spines[spine].set_linewidth(0.5)
            except KeyError:
                pass
                # ax.spines[spine].set_color(almost_black)
                # ax.spines[spine].set_tick_params(color=almost_black)
                # Check that the axes are not log-scale. If they are, leave
                # the ticks because otherwise people assume a linear scale.
    x_pos = set(['top', 'bottom'])
    y_pos = set(['left', 'right'])
    xy_pos = [x_pos, y_pos]
    xy_ax_names = ['xaxis', 'yaxis']

    for ax_name, pos in zip(xy_ax_names, xy_pos):
        axis = ax.__dict__[ax_name]
        # axis.set_tick_params(color=almost_black)
        #print 'axis.get_scale()', axis.get_scale()
        if show_ticks or axis.get_scale() == 'log':
            # if this spine is not in the list of spines to remove
            for p in pos.difference(spines):
                #print 'p', p
                axis.set_tick_params(direction='out')
                axis.set_ticks_position(p)
                #                axis.set_tick_params(which='both', p)
        else:
            axis.set_ticks_position('none')

    if grid is not None:
        for g in grid:
            assert g in ('x', 'y')
            ax.grid(axis=grid, color='white', linestyle='-', linewidth=0.5)

    if ticklabels is not None:
        if type(ticklabels) is str:
            assert ticklabels in set(('x', 'y'))
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


def maybe_get_ax(*args, **kwargs):
    """
    It used to be that the first argument of prettyplotlib had to be the 'ax'
    object, but that's not the case anymore.

    @param args:
    @type args:
    @param kwargs:
    @type kwargs:
    @return:
    @rtype:
    """

    if 'ax' in kwargs:
        ax = kwargs.pop('ax')
    elif len(args) == 0:
        fig = plt.gcf()
        ax = plt.gca()
    elif isinstance(args[0], mpl.axes.Axes):
        ax = args[0]
        args = args[1:]
    else:
        ax = plt.gca()
    return ax, args, dict(kwargs)


def maybe_get_fig_ax(*args, **kwargs):
    """
    It used to be that the first argument of prettyplotlib had to be the 'ax'
    object, but that's not the case anymore. This is specially made for
    pcolormesh.

    @param args:
    @type args:
    @param kwargs:
    @type kwargs:
    @return:
    @rtype:
    """
    if 'ax' in kwargs:
        ax = kwargs.pop('ax')
        if 'fig' in kwargs:
            fig = kwargs.pop('fig')
        else:
            fig = plt.gcf()
    elif len(args) == 0:
        fig = plt.gcf()
        ax = plt.gca()
    elif isinstance(args[0], mpl.figure.Figure) and \
            isinstance(args[1], mpl.axes.Axes):
        fig = args[0]
        ax = args[1]
        args = args[2:]
    else:
        fig, ax = plt.subplots(1)
    return fig, ax, args, dict(kwargs)


def maybe_get_linewidth(**kwargs):
    try:
        key = (set(["lw", "linewidth", 'linewidths']) & set(kwargs)).pop()
        lw = kwargs[key]
    except KeyError:
        lw = 0.15
    return lw
