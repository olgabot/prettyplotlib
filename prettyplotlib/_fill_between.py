from prettyplotlib.utils import remove_chartjunk, maybe_get_ax, maybe_get_linewidth
from prettyplotlib.colors import almost_black, pretty


@pretty
def fill_between(*args, **kwargs):
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)

    lw = maybe_get_linewidth(**kwargs)
    kwargs['linewidths'] = lw

    if 'color' not in kwargs:
        # if no color is specified, cycle over the ones in this axis
        color_cycle = ax._get_lines.color_cycle
        kwargs['color'] = next(color_cycle)
    kwargs.setdefault('edgecolor', almost_black)

    show_ticks = kwargs.pop('show_ticks', False)

    lines = ax.fill_between(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return lines 
