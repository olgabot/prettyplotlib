__author__ = 'olga'

from prettyplotlib import remove_chartjunk, almost_black

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
        kwargs['color'] = next(color_cycle)
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.5
    if 'linewidth' not in kwargs:
        kwargs['linewidth'] = 0.15

    show_ticks = kwargs.pop('show_ticks', False)

    scatterpoints = ax.scatter(x, y, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return scatterpoints
