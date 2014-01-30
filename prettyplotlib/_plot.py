__author__ = 'olga'

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import pretty


@pretty
def plot(*args, **kwargs):
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    show_ticks = kwargs.pop('show_ticks', False)

    lines = ax.plot(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return lines
