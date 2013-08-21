
# `prettyplotlib.pcolormesh`: Improving heatmaps in `matplotlib`

## Both positive and negative values

The default `matplotlib` `pcolormesh` heatmaps use a rainbow colormap, which has
been known to mislead data visualization. Specifically, [*"the rainbow color map
is universally inferior to all other color maps"*](http://www.jwave.vt.edu/~rkri
z/Projects/create_color_table/color_07.pdf). Unfortunately, `matplotlib` took
its default colors from MATLAB, and there the default is also rainbow.

In[1]:

```
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1)

np.random.seed(10)

#ax.pcolor(np.random.randn((10,10)))
#ax.pcolor(np.random.randn(10), np.random.randn(10))
p = ax.pcolormesh(np.random.randn(10,10))
fig.colorbar(p)
fig.savefig('pcolormesh_matplotlib_default.png')
```



[!image]()


Using the same zero-centered randomly distributed gaussian distribution, we can
plot it using `prettplotlib` with a few modifications:

    ppl.pcolormesh(fig, ax, np.random.randn(10,10))

You'll notice that the "hot" (large, positive) color is still red, and the
"cold" (small, negative) color is still blue, but the in between colors are
gradations of red and blue, so it's easier to tell the difference between
values.

In[2]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.random.randn(10,10))
fig.savefig('pcolormesh_prettyplotlib_default.png')
```



[!image]()


You may have noticed similar changes as were made in `prettyplotlib.scatter`,
where axis lines were removed, and blacks were changed to almost black.

## Only positive (or negative) values

If your data is only positive (or negative), `matplotlib` does nothing to change
the color scale. It's still a rainbow, but look at the colorbar, the range is
different (0 to 1 instead of -2 to +2)

In[3]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np

fig, ax = plt.subplots(1)

np.random.seed(10)

p = ax.pcolormesh(np.random.uniform(size=(10,10)))
fig.colorbar(p)
fig.savefig('pcolormesh_matplotlib_positive_default.png')
```



[!image]()


If your data is only positive or negative, then `prettyplotlib` will auto-detect
this and use a single-color colormap. The default for positive data is the
`reds` colormap.

In[4]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.abs(np.random.randn(10,10)))
fig.savefig('pcolormesh_prettyplotlib_positive.png')
```



[!image]()


And the default for negative data is the `blues` colormap.

In[5]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, -np.abs(np.random.randn(10,10)))
fig.savefig('pcolormesh_prettyplotlib_negative.png')
```



[!image]()


Plus you can add $x$- and $y$-ticklabels directly!

Normally, when you add $x$- and $y$-ticklables on `pcolormesh` in `matplotlib`,
they're not centered on the blocks, and you have to do a lot of annoying work
just getting a label on each box. You have to specify the xticks explicitly,
since you want to label each box.

    xticks = range(10)
    yticks = range(10)

    xticklabels=string.uppercase[:10]
    yticklabels=string.lowercase[-10:]

    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)


In[6]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import string

fig, ax = plt.subplots(1)

np.random.seed(10)

p = ax.pcolormesh(np.abs(np.random.randn(10,10)))
fig.colorbar(p)

xticks = range(10)
yticks = range(10)

xticklabels=string.uppercase[:10]
yticklabels=string.lowercase[-10:]

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)


fig.savefig('pcolormesh_matplotlib_positive_labels.png')
```



[!image]()


But `prettyplotlib.pcolormesh` assumes that you want the `xticklabels` and
`yticklabels` on each block, and makes it easy to specify.

    ppl.pcolormesh(fig, ax, np.random.uniform(size=(10,10)),
                   xticklabels=string.uppercase[:10],
                   yticklabels=string.lowercase[-10:])

In[11]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
import numpy as np
import string

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.random.randn(10,10), 
               xticklabels=string.uppercase[:10], 
               yticklabels=string.lowercase[-10:])
fig.savefig('pcolormesh_prettyplotlib_labels.png')
```



[!image]()


Or pick your own colormap! The diverging colormap `PRGn` or Purple and Green is
pretty nice. I usually use this website to look up the colormaps: [Every
Colorbrewer Scale](http://bl.ocks.org/mbostock/5577023)

In[25]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
from prettyplotlib import brewer2mpl
import numpy as np
import string

green_purple = brewer2mpl.get_map('PRGn', 'diverging', 11).mpl_colormap

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.random.randn(10,10), 
               xticklabels=string.uppercase[:10], 
               yticklabels=string.lowercase[-10:],
               cmap=green_purple)
fig.savefig('pcolormesh_prettyplotlib_labels_other_cmap_diverging.png')
```



[!image]()


Or if you want your own colormap for positive-only data:

In[24]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
from prettyplotlib import brewer2mpl
import numpy as np
import string

red_purple = brewer2mpl.get_map('RdPu', 'Sequential', 9).mpl_colormap

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.abs(np.random.randn(10,10)),
               xticklabels=string.uppercase[:10], 
               yticklabels=string.lowercase[-10:],
               cmap=red_purple)
fig.savefig('pcolormesh_prettyplotlib_labels_other_cmap_sequential.png')
```



[!image]()


Plus, this will take the usual parameters of `pcolormesh` like if you want to
rescale your data to log-scale:

    from matplotlib.colors import LogNorm
    ...
    ppl.pcolormesh(..., norm=LogNorm(vmin=x.min().min(), vmax=x.max().max()))

In[23]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
from prettyplotlib import brewer2mpl
import numpy as np
import string
from matplotlib.colors import LogNorm

red_purple = brewer2mpl.get_map('RdPu', 'Sequential', 9).mpl_colormap

fig, ax = plt.subplots(1)

np.random.seed(10)

x = np.abs(np.random.randn(10,10))
ppl.pcolormesh(fig, ax, x,
               xticklabels=string.uppercase[:10], 
               yticklabels=string.lowercase[-10:],
               cmap=red_purple, 
               norm=LogNorm(vmin=x.min().min(), vmax=x.max().max()))
fig.savefig('pcolormesh_prettyplotlib_labels_lognorm.png')
```



[!image]()


And now you can easily make beautiful heatmaps!
