__author__ = 'jan'

import matplotlib.pyplot as plt
from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib import colors as _colors
import numpy as np 
import matplotlib.mlab as mlab

def _beeswarm(ax, x, notch=0, sym='b+', vert=1, whis=1.5,
            positions=None, widths=None, patch_artist=False,
            bootstrap=None):
    """
    Call signature::

      beeswarm(x, notch=0, sym='+', vert=1, whis=1.5,
              positions=None, widths=None, patch_artist=False)

    Make a box and whisker plot for each column of *x* or each
    vector in sequence *x*.  The box extends from the lower to
    upper quartile values of the data, with a line at the median.
    The whiskers extend from the box to show the range of the
    data.  Flier points are those past the end of the whiskers.

    Function Arguments:

      *x* :
        Array or a sequence of vectors.

      *notch* : [ 0 (default) | 1]
        If 0, produce a rectangular box plot.
        If 1, produce a notched box plot

      *sym* :
        (default 'b+') is the default symbol for flier points.
        Enter an empty string ('') if you don't want to show fliers.

      *vert* : [1 (default) | 0]
        If 1, make the boxes vertical.
        If 0, make horizontal boxes. (Odd, but kept for compatibility
        with MATLAB boxplots)

      *whis* : (default 1.5)
        Defines the length of the whiskers as
        a function of the inner quartile range.  They extend to the
        most extreme data point within ( ``whis*(75%-25%)`` ) data range.

      *bootstrap* : [ *None* (default) | integer ]
        Specifies whether to bootstrap the confidence intervals
        around the median for notched boxplots. If *None*, no
        bootstrapping is performed, and notches are calculated
        using a Gaussian-based asymptotic approximation
        (see McGill, R., Tukey, J.W., and Larsen, W.A.,
        1978, and Kendall and Stuart, 1967). Otherwise, bootstrap
        specifies the number of times to bootstrap the median to
        determine its 95% confidence intervals. Values between 1000
        and 10000 are recommended.

      *positions* : (default 1,2,...,n)
        Sets the horizontal positions of
        the boxes. The ticks and limits are automatically set to match
        the positions.

      *widths* : [ scalar | array ]
        Either a scalar or a vector to set the width of each box.
        The default is 0.5, or ``0.15*(distance between extreme
        positions)`` if that is smaller.

      *patch_artist* : boolean
        If *False* (default), produce boxes with the
        :class:`~matplotlib.lines.Line2D` artist.
        If *True*, produce boxes with the
        :class:`~matplotlib.patches.Patch` artist.

    Returns a dictionary mapping each component of the boxplot
    to a list of the :class:`~matplotlib.lines.Line2D`
    instances created (unless *patch_artist* was *True*. See above.).

    **Example:**

    .. plot:: pyplots/boxplot_demo.py
    """
    if not ax._hold: ax.cla()
    holdStatus = ax._hold
    whiskers, caps, boxes, medians, fliers = [], [], [], [], []

    # convert x to a list of vectors
    if hasattr(x, 'shape'):
        if len(x.shape) == 1:
            if hasattr(x[0], 'shape'):
                x = list(x)
            else:
                x = [x,]
        elif len(x.shape) == 2:
            nr, nc = x.shape
            if nr == 1:
                x = [x]
            elif nc == 1:
                x = [x.ravel()]
            else:
                x = [x[:,i] for i in xrange(nc)]
        else:
            raise ValueError("input x can have no more than 2 dimensions")
    if not hasattr(x[0], '__len__'):
        x = [x]
    col = len(x)

    # get some plot info
    if positions is None:
        positions = range(1, col + 1)
    if widths is None:
        distance = max(positions) - min(positions)
        widths = min(0.15*max(distance,1.0), 0.5)
    if isinstance(widths, float) or isinstance(widths, int):
        widths = np.ones((col,), float) * widths

    # loop through columns, adding each to plot
    ax.hold(True)
    for i,pos in enumerate(positions):
        d = np.ravel(x[i])
        row = len(d)
        if row==0:
            # no data, skip this position
            continue
        # get median and quartiles
        q1, med, q3 = mlab.prctile(d,[25,50,75])
        # get high extreme
        iq = q3 - q1
        hi_val = q3 + whis*iq
        wisk_hi = np.compress( d <= hi_val , d )
        if len(wisk_hi) == 0:
            wisk_hi = q3
        else:
            wisk_hi = max(wisk_hi)
        # get low extreme
        lo_val = q1 - whis*iq
        wisk_lo = np.compress( d >= lo_val, d )
        if len(wisk_lo) == 0:
            wisk_lo = q1
        else:
            wisk_lo = min(wisk_lo)
        
        # get x locations for fliers, whisker, whisker cap and box sides
        box_x_min = pos - widths[i] * 0.5
        box_x_max = pos + widths[i] * 0.5
        
        # get fliers - if we are showing them
        flier = []
        flier_x = []
        if len(sym) != 0:
            flier = d
            flier_x = np.ones(flier.shape[0]) * pos              
            flier_x = np.linspace(box_x_min , box_x_max, flier.shape[0])
        
        wisk_x = np.ones(2) * pos

        cap_x_min = pos - widths[i] * 0.25
        cap_x_max = pos + widths[i] * 0.25
        cap_x = [cap_x_min, cap_x_max]

        # get y location for median
        med_y = [med, med]

        # calculate 'regular' plot
        if notch == 0:
            # make our box vectors
            box_x = [box_x_min, box_x_max, box_x_max, box_x_min, box_x_min ]
            box_y = [q1, q1, q3, q3, q1 ]
            # make our median line vectors
            med_x = [box_x_min, box_x_max]
        # calculate 'notch' plot
        else:
            if bootstrap is not None:
                # Do a bootstrap estimate of notch locations.
                def bootstrapMedian(data, N=5000):
                    # determine 95% confidence intervals of the median
                    M = len(data)
                    percentile = [2.5,97.5]
                    estimate = np.zeros(N)
                    for n in range(N):
                        bsIndex = np.random.random_integers(0,M-1,M)
                        bsData = data[bsIndex]
                        estimate[n] = mlab.prctile(bsData, 50)
                    CI = mlab.prctile(estimate, percentile)
                    return CI

                # get conf. intervals around median
                CI = bootstrapMedian(d, N=bootstrap)
                notch_max = CI[1]
                notch_min = CI[0]
            else:
                # Estimate notch locations using Gaussian-based
                # asymptotic approximation.
                #
                # For discussion: McGill, R., Tukey, J.W.,
                # and Larsen, W.A. (1978) "Variations of
                # Boxplots", The American Statistician, 32:12-16.
                notch_max = med + 1.57*iq/np.sqrt(row)
                notch_min = med - 1.57*iq/np.sqrt(row)
            # make our notched box vectors
            box_x = [box_x_min, box_x_max, box_x_max, cap_x_max, box_x_max,
                     box_x_max, box_x_min, box_x_min, cap_x_min, box_x_min,
                     box_x_min ]
            box_y = [q1, q1, notch_min, med, notch_max, q3, q3, notch_max,
                     med, notch_min, q1]
            # make our median line vectors
            med_x = [cap_x_min, cap_x_max]
            med_y = [med, med]

        def to_vc(xs,ys):
            # convert arguments to verts and codes
            verts = []
            #codes = []
            for xi,yi in zip(xs,ys):
                verts.append( (xi,yi) )
            verts.append( (0,0) ) # ignored
            codes = [mpath.Path.MOVETO] + \
                    [mpath.Path.LINETO]*(len(verts)-2) + \
                    [mpath.Path.CLOSEPOLY]
            return verts,codes

        def patch_list(xs,ys):
            verts,codes = to_vc(xs,ys)
            path = mpath.Path( verts, codes )
            patch = mpatches.PathPatch(path)
            ax.add_artist(patch)
            return [patch]

        # vertical or horizontal plot?
        if vert:
            def doplot(*args):
                return ax.plot(*args)
            def dopatch(xs,ys):
                return patch_list(xs,ys)
        else:
            def doplot(*args):
                shuffled = []
                for i in xrange(0, len(args), 3):
                    shuffled.extend([args[i+1], args[i], args[i+2]])
                return ax.plot(*shuffled)
            def dopatch(xs,ys):
                xs,ys = ys,xs # flip X, Y
                return patch_list(xs,ys)

        if patch_artist:
            median_color = 'k'
        else:
            median_color = 'r'

        #whiskers.extend(doplot(wisk_x, [q1, wisk_lo], 'b--',
        #                       wisk_x, [q3, wisk_hi], 'b--'))
        #caps.extend(doplot(cap_x, [wisk_hi, wisk_hi], 'k-',
        #                   cap_x, [wisk_lo, wisk_lo], 'k-'))
        #if patch_artist:
        #    boxes.extend(dopatch(box_x, box_y))
        #else:
        #    boxes.extend(doplot(box_x, box_y, 'b-'))
        medians.extend(doplot(med_x, med_y, median_color+'-'))
        fliers.extend(doplot(flier_x, flier, sym))

    # fix our axes/ticks up a little
    if 1 == vert:
        setticks, setlim = ax.set_xticks, ax.set_xlim
    else:
        setticks, setlim = ax.set_yticks, ax.set_ylim

    newlimits = min(positions)-0.5, max(positions)+0.5
    setlim(newlimits)
    setticks(positions)

    # reset hold status
    ax.hold(holdStatus)

    return dict(whiskers=whiskers, caps=caps, boxes=boxes,
                medians=medians, fliers=fliers)



def beeswarm(*args, **kwargs):
    """
    Create a R-like beeswarm plot showing the mean and datapoints. 
    The difference from matplotlib is only the left axis line is
    shown, and ticklabels labeling each category of data can be added.

    @param ax:
    @param x:
    @param kwargs: Besides xticklabels, which is a prettyplotlib-specific
    argument which will label each individual beeswarm, many arguments for
    matplotlib.pyplot.boxplot will be accepted:
    http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.boxplot
    Additional arguments include:
    
       *median_color* : (default gray)
        The color of median lines   
    
       *median_width* : (default 2)
        Median line width

       *colors* : (default None)
        Colors to use when painting a dataseries, for example
        
          list1 = [1,2,3]
          list2 = [5,6,7]
          ppl.beeswarm([list1, list2], colors=["red", "blue"], xticklabels=["data1", "data2"])

    @return:
    """
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    # If no ticklabels are specified, don't draw any
    xticklabels = kwargs.pop('xticklabels', None)
    colors = kwargs.pop('colors', None)
    fontsize = kwargs.pop('fontsize', 10)
    
    gray = _colors.set1[8]
    red = _colors.set1[0]
    blue = kwargs.pop('color', _colors.set1[1])

    kwargs.setdefault('widths', 0.25)
    kwargs.setdefault('sym', "o")
    
    bp = _beeswarm(ax, *args, **kwargs)
    
    kwargs.setdefault("median_color", gray)
    kwargs.setdefault("median_linewidth", 2)
    
    
    if xticklabels:
        ax.xaxis.set_ticklabels(xticklabels, fontsize=fontsize)

    show_caps = kwargs.pop('show_caps', True)
    show_ticks = kwargs.pop('show_ticks', False)

    remove_chartjunk(ax, ['top', 'right', 'bottom'], show_ticks=show_ticks)
    linewidth = 0.75

    plt.setp(bp['boxes'], color=blue, linewidth=linewidth)
    plt.setp(bp['medians'], color=kwargs.pop("median_color"), linewidth=kwargs.pop("median_linewidth"))
    #plt.setp(bp['whiskers'], color=blue, linestyle='solid',
    #         linewidth=linewidth)
    for color, flier in zip(colors, bp['fliers']):
        plt.setp(flier, color=color)
    #if show_caps:
    #    plt.setp(bp['caps'], color=blue, linewidth=linewidth)
    #else:
    #    plt.setp(bp['caps'], color='none')
    ax.spines['left']._linewidth = 0.5
    return bp 

    
