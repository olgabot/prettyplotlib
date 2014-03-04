__author__ = 'olga'

import numpy as np

from prettyplotlib.colors import blue_red, blues_r, reds
from prettyplotlib.utils import remove_chartjunk, maybe_get_fig_ax

def pcolormesh(*args, **kwargs):
    """
    Use for large datasets

    Non-traditional `pcolormesh` kwargs are:
    - xticklabels, which will put x tick labels exactly in the center of the
    heatmap block
    - yticklables, which will put y tick labels exactly aligned in the center
     of the heatmap block
     - xticklabels_rotation, which can be either 'horizontal' or 'vertical'
     depending on how you want the xticklabels rotated. The default is
     'horizontal', but if you have xticklabels that are longer, you may want
     to do 'vertical' so they don't overlap.
     - yticklabels_rotation, which can also be either 'horizontal' or
     'vertical'. The default is 'horizontal' and in most cases,
     that's what you'll want to stick with. But the option is there if you
     want.
    - center_value, which will be the centered value for a divergent
    colormap, for example if you have data above and below zero, but you want
    the white part of the colormap to be equal to 10 rather than 0,
    then specify 'center_value=10'.
    """
    # Deal with arguments in kwargs that should be there, or need to be taken
    #  out
    fig, ax, args, kwargs = maybe_get_fig_ax(*args, **kwargs)

    x = args[0]

    kwargs.setdefault('vmax', x.max())
    kwargs.setdefault('vmin', x.min())

    center_value = kwargs.pop('center_value', 0)

    # If
    divergent_data = False
    if kwargs['vmax'] > 0 and kwargs['vmin'] < 0:
        divergent_data = True
        kwargs['vmax'] += center_value
        kwargs['vmin'] += center_value

    # If we have both negative and positive values, use a divergent colormap
    if 'cmap' not in kwargs:
        # Check if this is divergent
        if divergent_data:
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

    p = ax.pcolormesh(*args, **kwargs)
    ax.set_ylim(0, x.shape[0])

    # Get rid of ALL axes
    remove_chartjunk(ax, ['top', 'right', 'left', 'bottom'])

    if xticklabels is not None and any(xticklabels):
        xticks = np.arange(0.5, x.shape[1] + 0.5)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, rotation=xticklabels_rotation)
    if yticklabels is not None and any(yticklabels):
        yticks = np.arange(0.5, x.shape[0] + 0.5)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels, rotation=yticklabels_rotation)

    # Show the scale of the colorbar
    fig.colorbar(p, cax=ax_colorbar, use_gridspec=True,
                 orientation=orientation_colorbar)
    return fig
