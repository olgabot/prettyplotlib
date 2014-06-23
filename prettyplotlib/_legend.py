__author__ = 'olga'

from prettyplotlib.colors import light_grey, almost_black
from prettyplotlib.utils import maybe_get_ax


def legend(*args, **kwargs):
    """

    @param args:
    @type args:
    @param kwargs: Any keyword arguments to matplotlib's plt.legend()
    Optional 'facecolor' keyword to change the facecolor of the legend
    @type kwargs:
    @return:
    @rtype:
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    facecolor = kwargs.pop('facecolor', light_grey)

    kwargs.setdefault('frameon', True)
    kwargs.setdefault('scatterpoints', True)

    legend = ax.legend(*args, **kwargs)
    try:
        rect = legend.get_frame()
        rect.set_facecolor(facecolor)
        rect.set_linewidth(0.0)

        # Change the label colors in the legend to almost black
        # Change the legend label colors to almost black, too
        texts = legend.texts
        for t in texts:
            t.set_color(almost_black)
    except AttributeError:
        # There are no labled objects
        pass
    return legend
