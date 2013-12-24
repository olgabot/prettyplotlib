
# `prettyplotlib.scatter`: A motivating example

The default `matplotlib` color cycle is not pretty to look at ... It was taken
from MATLAB's color cycle.

Need to do the `matplotlib` example first because `prettyplotlib` changes the
default color cycle to a nicer one, from
[ColorBrewer](http://bl.ocks.org/mbostock/5577023)'s Set2. What's even worse is
that if you just do a `scatter` plot, then it doesn't cycle at all...

In[1]:

```
import matplotlib.pyplot as mpl_plt
# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    ax.scatter(x, y, label=str(i))
ax.legend()
    
ax.set_title('prettyplotlib `scatter` example\nshowing default matplotlib `scatter`')
fig.savefig('scatter_matplotlib_default.png')
```



[!image]()


## Before `prettyplotlib`: how to make nice plots

Now I'm going to take you through ALL the steps I used to take to make nice
looking plots.



First, change the colors with `brewer2mpl`:

    # Get "Set2" colors from ColorBrewer (all colorbrewer scales:
http://bl.ocks.org/mbostock/5577023)
    set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors
    ...
    color = set2[i]
    ax.scatter(x, y, label=str(i), facecolor=color)

In[2]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), color=color)
    
fig.savefig('scatter_matplotlib_improved_01_changed_colors.png')
```



[!image]()


This looks nice, almost like an impressionist painting, but it's still hard to
see overlaps here. So let's fill the symbols with `0.5` opacity using
`alpha=0.5`.

    ax.scatter(x, y, label=str(i), color=color, alpha=0.5)

In[3]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), color=color, alpha=0.5)
    
fig.savefig('scatter_matplotlib_improved_02_added_alpha.png')
```



[!image]()


This is still pretty lovely and impressionist-y but I still didn't like that it
was hard to see when the dots overlapped. So let's add a black outline, and
specify that `color` is just the `facecolor`:

    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black',
facecolor=color)

In[4]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black', facecolor=color)
    
fig.savefig('scatter_matplotlib_improved_03_added_outline.png')
```



[!image]()


Ack, but those lines are too thick ... let's think them down to `linewidth=0.15`

    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black',
facecolor=color, linewidth=0.15)

In[5]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black', facecolor=color, linewidth=0.15)
fig.savefig('scatter_matplotlib_improved_04_thinned_outline.png')
```



[!image]()


*Now* we're getting somewhere. This looks very lovely. Don't you want to just
cuddle up with that cute plot?

What are those top and right axes lines really doing for us? They're boxing the
data in, but we can do that with our eyes from the other axis lines. So let's
remove the top and right axis lines using `ax.spines`:

    # Remove top and right axes lines ("spines")
    spines_to_remove = ['top', 'right']
    for spine in spines_to_remove:
        ax.spines[spine].set_visible(False)

In[6]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black', facecolor=color, linewidth=0.15)

# Remove top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(False)
fig.savefig('scatter_matplotlib_improved_05_removed_top_right_spines.png')
```



[!image]()


Oops, but we still have the ticks on the top and right axes. We'll need to get
rid of them. Actually, why don't we just get rid of all ticks altogether? We can
tell by the position of the number where it indicates, so we don't need an
additional tick.

    # Get rid of ticks. The position of the numbers is informative enough of
    # the position of the value.
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

In[7]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black', facecolor=color, linewidth=0.15)

# Remove top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(False)

# Get rid of ticks. The position of the numbers is informative enough of
# the position of the value.
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
fig.savefig('scatter_matplotlib_improved_06_removed_ticks.png')
```



[!image]()


Ahh, much better. But we won't stop there. Now we'll tweak the remaining pieces
of the figure. For the rest of the spines, let's thin the line down to `0.5`
points instead of the default `1.0` points. Also, we'll change it from pure
black to a slightly lighter dark grey. Here they are side by side:

In[8]:

```
fig, axes = plt.subplots(2)
axes[0].set_axis_bgcolor('black')
axes[1].set_axis_bgcolor('#262626')
```



[!image]()


So not a *huge* difference, and the dark grey still looks pretty black, but it's
[a little more pleasant on the eyes](http://ianstormtaylor.com/design-tip-never-
use-black/) to use a dark grey instead of black. There's very few things in
nature that are truly black. Just look at shadows! They're just dark grey, or
blue, or red or purple. But I digress. Back to plotting libraries...

To change the $x$-axis and $y$-axis line colors, and the outlines of the scatter
sybmols from black to dark grey, we'll do:

    # For remaining spines, thin out their line and change the black to a
slightly off-black dark grey
    almost_black = '#262626'
    ...
        ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor='black',
facecolor=color, linewidth=0.15)`
    ...
    spines_to_keep = ['bottom', 'left']
    for spine in spines_to_keep:
        ax.spines[spine].set_linewidth(0.5)
        ax.spines[spine].set_color(almost_black)

In[9]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

# Save a nice dark grey as a variable
almost_black = '#262626'

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor=almost_black, facecolor=color, linewidth=0.15)

# Remove top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(False)

# Get rid of ticks. The position of the numbers is informative enough of
# the position of the value.
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# For remaining spines, thin out their line and change the black to a slightly off-black dark grey
spines_to_keep = ['bottom', 'left']
for spine in spines_to_keep:
    ax.spines[spine].set_linewidth(0.5)
    ax.spines[spine].set_color(almost_black)
fig.savefig('scatter_matplotlib_improved_07_axis_black_to_almost_black.png')
```



[!image]()


This is nice. But if you look closely, the tick labels are still black :(  We
have to change them separately, using

    # Change the labels to the off-black
    ax.xaxis.label.set_color(almost_black)
    ax.yaxis.label.set_color(almost_black)

And while we're at it, let's add a title and make it dark grey too.

    # Change the axis title to off-black
    ax.title.set_color(almost_black)

    ax.set_title('prettyplotlib `scatter` example\nshowing improved matplotlib
`scatter`')

In[10]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

# Save a nice dark grey as a variable
almost_black = '#262626'

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor=almost_black, facecolor=color, linewidth=0.15)

# Remove top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(False)

# Get rid of ticks. The position of the numbers is informative enough of
# the position of the value.
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# For remaining spines, thin out their line and change the black to a slightly off-black dark grey
spines_to_keep = ['bottom', 'left']
for spine in spines_to_keep:
    ax.spines[spine].set_linewidth(0.5)
    ax.spines[spine].set_color(almost_black)

# Change the labels to the off-black
ax.xaxis.label.set_color(almost_black)
ax.yaxis.label.set_color(almost_black)

# Change the axis title to off-black
ax.title.set_color(almost_black)

ax.set_title('prettyplotlib `scatter` example\nshowing improved matplotlib `scatter`')
fig.savefig('scatter_matplotlib_improved_08_labels_black_to_almost_black.png')
```



[!image]()


If you remember in the original example, we also had an axis legend, using

    ax.legend()

In[11]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

# Save a nice dark grey as a variable
almost_black = '#262626'

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor=almost_black, facecolor=color, linewidth=0.15)

# Remove top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(False)

# Get rid of ticks. The position of the numbers is informative enough of
# the position of the value.
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# For remaining spines, thin out their line and change the black to a slightly off-black dark grey
almost_black = '#262626'
spines_to_keep = ['bottom', 'left']
for spine in spines_to_keep:
    ax.spines[spine].set_linewidth(0.5)
    ax.spines[spine].set_color(almost_black)

# Change the labels to the off-black
ax.xaxis.label.set_color(almost_black)
ax.yaxis.label.set_color(almost_black)

# Change the axis title to off-black
ax.title.set_color(almost_black)

ax.legend()
    
ax.set_title('prettyplotlib `scatter` example\nshowing improved matplotlib `scatter`')
fig.savefig('scatter_matplotlib_improved_09_ugly_legend.png')
```



[!image]()


There are many things I don't like about this legend.

1. First of all, why does it have such a thick border line? What does that
really add to our interpretation of the legend? The black line is so thick that
it distracts from what we're trying to portray - which label goes with which
color.
2. Why does it show three points? Does this legend think I'm dumb and can't
figure out which symbol goes with which label after one iteration, so it does it
three times?
3. Finally, the legend labels are pure black. Maybe you notice it too, after
comparing to $x$-axis and $y$-axis lines and labels.

We'll accomplish these three things using this code:

    # Remove the line around the legend box, and instead fill it with a light
grey
    # Also only use one point for the scatterplot legend because the user will
    # get the idea after just one, they don't need three.
    light_grey = np.array([float(248)/float(255)]*3)
    legend = ax.legend(frameon=True, scatterpoints=1, fontcolor=almost_black)
    rect = legend.get_frame()
    rect.set_facecolor(light_grey)
    rect.set_linewidth(0.0)

    # Change the legend label colors to almost black, too
    texts = legend.texts
    for t in texts:
        t.set_color(almost_black)

In[12]:

```
import matplotlib.pyplot as mpl_plt
import brewer2mpl

# Get "Set2" colors from ColorBrewer (all colorbrewer scales: http://bl.ocks.org/mbostock/5577023)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# Set the random seed for consistency
np.random.seed(12)

# Save a nice dark grey as a variable
almost_black = '#262626'

fig, ax = mpl_plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    color = set2[i]
    ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor=almost_black, facecolor=color, linewidth=0.15)

# Remove top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(False)

# Get rid of ticks. The position of the numbers is informative enough of
# the position of the value.
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# For remaining spines, thin out their line and change the black to a slightly off-black dark grey
almost_black = '#262626'
spines_to_keep = ['bottom', 'left']
for spine in spines_to_keep:
    ax.spines[spine].set_linewidth(0.5)
    ax.spines[spine].set_color(almost_black)

# Change the labels to the off-black
ax.xaxis.label.set_color(almost_black)
ax.yaxis.label.set_color(almost_black)

# Change the axis title to off-black
ax.title.set_color(almost_black)

# Remove the line around the legend box, and instead fill it with a light grey
# Also only use one point for the scatterplot legend because the user will 
# get the idea after just one, they don't need three.
light_grey = np.array([float(248)/float(255)]*3)
legend = ax.legend(frameon=True, scatterpoints=1)
rect = legend.get_frame()
rect.set_facecolor(light_grey)
rect.set_linewidth(0.0)

# Change the legend label colors to almost black, too
texts = legend.texts
for t in texts:
    t.set_color(almost_black)

    
ax.set_title('prettyplotlib `scatter` example\nshowing improved matplotlib `scatter`')
fig.savefig('scatter_matplotlib_improved_10_pretty_legend.png')
```



[!image]()


Aaaaaaaaaaand I got tired of doing all those steps, EVERY time. So I wrote
[`prettyplotlib`](http://github.com/olgabot/prettyplotlib). Here's an
illustratitive example of how awesome `prettyplotlib` is, and how it will save
all the time you spent agonizing over making your `matplotlib` plots beautiful.

In[13]:

```
import prettyplotlib as ppl

# This is "import matplotlib.pyplot as plt" from the prettyplotlib library
from prettyplotlib import plt

# This is "import matplotlib as mpl" from the prettyplotlib library
from prettyplotlib import mpl

# Set the random seed for consistency
np.random.seed(12)

fig, ax = plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    ppl.scatter(ax, x, y, label=str(i))
    
ppl.legend(ax)
    
ax.set_title('prettyplotlib `scatter` example\nshowing default color cycle and scatter params')
fig.savefig('scatter_prettyplotlib_default.png')
```



[!image]()


The only commands that were different from the very first example with
matplotlib are:

    ppl.scatter(ax, x, y, label=str(i), facecolor='none')

instead of:

    ax.scatter(x, y, label=str(i))

And a different legend command:

    ppl.legend(ax)

instead of:

    ax.legend()

If you ***really*** want to get the original matplotlib style back in
prettyplotlib, you can do:

In[2]:

```
import prettyplotlib as ppl
from prettyplotlib import plt
from prettyplotlib import mpl
from prettyplotlib import brewer2mpl

# Set the random seed for consistency
np.random.seed(12)

fig, ax = plt.subplots(1)

#mpl.rcParams['axis.color_cycle'] = ['blue']

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    ax.scatter(x, y, label=str(i), facecolor='blue', edgecolor='black', linewidth=1)
    
# Get back the top and right axes lines ("spines")
spines_to_remove = ['top', 'right']
for spine in spines_to_remove:
    ax.spines[spine].set_visible(True)
    
# Get back the ticks. The position of the numbers is informative enough of
# the position of the value.
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')

# For all the spines, make their line thicker and return them to be black
all_spines = ['top', 'left', 'bottom', 'right']
for spine in all_spines:
    ax.spines[spine].set_linewidth(1.0)
    ax.spines[spine].set_color('black')

# Change the labels back to black
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')

# Change the axis title also back to black
ax.title.set_color('black')

# Remove the line around the legend box, and instead fill it with a light grey
# Also only use one point for the scatterplot legend because the user will 
# get the idea after just one, they don't need three.
ax.legend()
    
ax.set_title('prettyplotlib `scatter` example\nrevert everything back to default matplotlib parameters')
fig.savefig('scatter_prettyplotlib_back_to_matplotlib_default.png')
```



[!image]()



[!image]()


Notice that the default calls of `ax.scatter` and `ax.legend` do the usual
thing. This is important, because for `prettyplotlib` to work, you'll need to
use a syntax that's different from the usual `matplotlib` one:  `ppl.scatter(ax,
x, y...)` instead of `ax.scatter(x, y, ...)`


## That's all, folks!

That's my introduction to `prettyplotlib` and why you need it. There are similar
examples for the other functions, but this one for `ppl.scatter` is the most
extensive.
