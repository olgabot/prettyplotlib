__author__ = 'jgosmann'

from matplotlib.cbook import iterable

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import set2


def eventplot(*args, **kwargs):
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    show_ticks = kwargs.pop('show_ticks', False)
    alpha = kwargs.pop('alpha', 1.0)

    if len(args) > 0:
        positions = args[0]
    else:
        positions = kwargs['positions']

    if any(iterable(p) for p in positions):
        size = len(positions)
    else:
        size = 1

    kwargs.setdefault('colors', [c + (alpha,) for c in set2[:size]])

    event_collections = ax.eventplot(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return event_collections
