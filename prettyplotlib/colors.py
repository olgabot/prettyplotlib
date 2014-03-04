from functools import wraps

import brewer2mpl
import numpy as np
import matplotlib as mpl
from matplotlib import cm



# Get Set2 from ColorBrewer, a set of colors deemed colorblind-safe and
# pleasant to look at by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. These colors look lovely together, and are less
# saturated than those colors in Set1. For more on ColorBrewer, see:
# - Flash-based interactive map:
#     http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
#     http://bl.ocks.org/mbostock/5577023

#class Common(object):
#    def __init__(self):
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Another ColorBrewer scale. This one has nice "traditional" colors like
# reds and blues
set1 = brewer2mpl.get_map('Set1', 'qualitative', 9).mpl_colors

# This decorator makes it possible to change the color cycle inside
# prettyplotlib  without affecting pyplot
def pretty(func):
    rcParams = {'axes.color_cycle': set2, 'lines.linewidth': .75}

    @wraps(func)
    def wrapper(*args, **kwargs):
        with mpl.rc_context(rc=rcParams):
            return func(*args, **kwargs)
    return wrapper

# Set some commonly used colors
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

reds = cm.Reds
reds.set_bad('white')
reds.set_under('white')

blues_r = cm.Blues_r
blues_r.set_bad('white')
blues_r.set_under('white')

# Need to 'reverse' red to blue so that blue=cold=small numbers,
# and red=hot=large numbers with '_r' suffix
blue_red = brewer2mpl.get_map('RdBu', 'Diverging', 11,
                              reverse=True).mpl_colormap
