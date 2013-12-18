prettyplotlib
=============

Python matplotlib-enhancer library which painlessly creates beautiful default `matplotlib`
 plots. Inspired by [Edward Tufte](http://www.edwardtufte.com/tufte/)'s work on information design and [Cynthia Brewer](http://www.personal.psu.edu/cab38/)'s work on [color perception](http://colorbrewer2.org/).

I truly believe that scientific progress is impeded when improper data visualizations are used. I spent a lot of time tweaking my figures to make them more understandable, and realized the scientific world could be a better place if the default parameters for plotting libraries followed recent advances in information design research. And thus `prettyplotlib` was born.

Requirements:

* [`matplotlib`](http://matplotlib.org/). Can be installed via `pip install matplotlib` or `easy_install matplotlib`
* [`brewer2mpl`](https://github.com/jiffyclub/brewer2mpl). Can be installed via `pip install brewer2mpl` or `easy_install brewer2mpl`

## Comparison to `matplotlib`

<table>
  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>plot</code><br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/plot_matplotlib_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>plot</code><br><a href=https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#plot-lines-eg-time-series-with-a-legend"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/plot_prettyplotlib_default.png" height="202"></a></td>
  </tr>  
  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>scatter</code><br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/scatter_matplotlib_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>scatter</code><br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#scatter-points"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/scatter_prettyplotlib_default.png" height="202"></a></td>
  </tr>
  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>bar</code><br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/bar_matplotlib_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>bar</code><br><a href=https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#bar><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/bar_prettyplotlib_default.png" height="202"></a></td>
  </tr>
  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>hist</code><br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/hist_matplotlib_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>hist</code><br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#hist"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/hist_prettyplotlib_default.png" height="202"></a></td>
</tr>
  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>hist</code><br>with grid<br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/hist_matplotlib_grid.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>hist</code><br>with grid<br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#back-to-matplotlib-style-scatterplots"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/hist_prettyplotlib_grid.png" height="202"></a></td>
</tr>
  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>boxplot</code><br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/boxplot_matplotlib_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>boxplot</code><br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#boxplot"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/boxplot_prettyplotlib_default.png" height="202"></a></td>
  </tr>  
<tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>pcolormesh</code><br>positive and negative data<br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/pcolormesh_matplotlib_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>pcolormesh</code><br>positive and negative data<br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#pcolormesh-heatmaps"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/pcolormesh_prettyplotlib_default.png" height="202"></a></td>
  </tr>
  </tr>  <tr height="207" valign="top">
    <td><code>matplotlib</code> default <code>pcolormesh</code><br>positive data only<br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/pcolormesh_matplotlib_positive_default.png" height="202"></td>
    <td><code>prettyplotlib</code> default <code>pcolormesh</code><br>positive data only<br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#pcolormesh-positive-only-data"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/pcolormesh_prettyplotlib_positive.png" height="202"></a></td>
  </tr>
  </tr>  <tr height="207" valign="top">
    <td><code>matplotlib pcolormesh</code><br> negative-valued data with labels<br><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/pcolormesh_matplotlib_negative_labels.png" height="202"></td>
    <td><code>prettyplotlib pcolormesh</code><br> negative-valued data with labels<br><a href="https://github.com/olgabot/prettyplotlib/wiki/Examples-with-code#pcolormesh-positive-only-data"><img src="https://raw.github.com/olgabot/prettyplotlib/master/examples/pcolormesh_prettyplotlib_negative_labels.png" height="202"></a></td>
  </tr>
</table>

### Quotes

_"Dis ain't no **ugly**plotlib"_ - Anonymous