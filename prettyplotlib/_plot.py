__author__ = 'olga'

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax


def plot(*args, **kwargs):
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    if 'color' not in kwargs:
        # if no color is specified, cycle over the ones in this axis
        color_cycle = ax._get_lines.color_cycle
        kwargs['color'] = next(color_cycle)
    if 'linewidth' not in kwargs:
        kwargs['linewidth'] = 0.75

    show_ticks = kwargs.pop('show_ticks', False)

    lines = ax.plot(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return lines
