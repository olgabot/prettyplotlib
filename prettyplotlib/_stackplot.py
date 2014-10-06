from prettyplotlib.utils import remove_chartjunk, maybe_get_ax, maybe_get_linewidth
from prettyplotlib.colors import almost_black, pretty

@pretty
def stackplot(*args, **kwargs):
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)

    lw = maybe_get_linewidth(**kwargs)
    kwargs['linewidths'] = lw

    kwargs.setdefault('edgecolor', almost_black)
    show_ticks = kwargs.pop('show_ticks', False)

    lines = ax.stackplot(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return lines 
