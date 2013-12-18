__author__ = 'olga'

from prettyplotlib.colors import light_grey, almost_black


def legend(ax, facecolor=light_grey, **kwargs):
    legend = ax.legend(frameon=True, scatterpoints=1, **kwargs)
    rect = legend.get_frame()
    rect.set_facecolor(facecolor)
    rect.set_linewidth(0.0)

    # change the label colors in the legend to almost black
    # Change the legend label colors to almost black, too
    texts = legend.texts
    for t in texts:
        t.set_color(almost_black)
    return legend
