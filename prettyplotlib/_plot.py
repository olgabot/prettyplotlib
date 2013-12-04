__author__ = 'olga'

from prettyplotlib import remove_chartjunk

def plot(ax, x, y, **kwargs):
    if 'color' in kwargs:
        color = kwargs['color']
        # Remove the other color argument so matplotlib doesn't complain
        kwargs.pop('color')
    else:
        # if no color is specified, cycle over the ones in this axis
        color_cycle = ax._get_lines.color_cycle
        color = next(color_cycle)
    if 'linewidth' not in kwargs:
        kwargs['linewidth'] = 0.75

    show_ticks = kwargs.pop('show_ticks', False)

    lines = ax.plot(x, y, color=color, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return lines
