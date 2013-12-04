__author__ = 'olga'

from prettyplotlib import blue_red, blues_r, reds, remove_chartjunk
import numpy as np

def pcolormesh(fig, ax, x, **kwargs):
    """
    Use for large datasets

    Non-traditional `pcolormesh` kwargs are:
    - xticklabels, which will put x tick labels exactly in the center of the
    heatmap block
    - yticklables, which will put y tick labels exactly aligned in the center
     of the heatmap block
     - xticklabels_rotation, which can be either 'horizontal' or 'vertical'
     depending on how you want the xticklabels rotated. The default is
     'horiztonal' but if you have xticklabels that are longer, you may want
     to do 'vertical' so they don't overlap
     - yticklabels_rotation, which can also be either 'horizontal' or
     'vertical'. The default is 'horizontal' and in most cases,
     that's what you'll want to stick with. But the option is there if you
     want.
    """
    # Deal with arguments in kwargs that should be there, or need to be taken
    #  out
    if 'vmax' not in kwargs:
        kwargs['vmax'] = x.max()
    if 'vmin' not in kwargs:
        kwargs['vmin'] = x.min()

    # If we have both negative and positive values, use a divergent colormap
    if 'cmap' not in kwargs:
        if kwargs['vmax'] > 0 and kwargs['vmin'] < 0:
            kwargs['cmap'] = blue_red
        elif kwargs['vmax'] <= 0:
                kwargs['cmap'] = blues_r
        elif kwargs['vmax'] > 0:
            kwargs['cmap'] = reds

    if 'xticklabels' in kwargs:
        xticklabels = kwargs['xticklabels']
        kwargs.pop('xticklabels')
    else:
        xticklabels = None
    if 'yticklabels' in kwargs:
        yticklabels = kwargs['yticklabels']
        kwargs.pop('yticklabels')
    else:
        yticklabels = None

    if 'xticklabels_rotation' in kwargs:
        xticklabels_rotation = kwargs['xticklabels_rotation']
        kwargs.pop('xticklabels_rotation')
    else:
        xticklabels_rotation = 'horizontal'
    if 'yticklabels_rotation' in kwargs:
        yticklabels_rotation = kwargs['yticklabels_rotation']
        kwargs.pop('yticklabels_rotation')
    else:
        yticklabels_rotation = 'horizontal'

    ax_colorbar = kwargs.pop('ax_colorbar', None)
    orientation_colorbar = kwargs.pop('orientation_colorbar', 'vertical')

    p = ax.pcolormesh(x, **kwargs)
    ax.set_ylim(0, x.shape[0])

    # Get rid of ALL axes
    remove_chartjunk(ax, ['top', 'right', 'left', 'bottom'])

    if xticklabels:
        xticks = np.arange(0.5, x.shape[1] + 0.5)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, rotation=xticklabels_rotation)
    if yticklabels:
        yticks = np.arange(0.5, x.shape[0] + 0.5)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels, rotation=yticklabels_rotation)

    # Show the scale of the colorbar
    fig.colorbar(p, cax=ax_colorbar, use_gridspec=True,
                 orientation=orientation_colorbar)
    return p
