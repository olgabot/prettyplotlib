prettyplotlib
=============

Python matplotlib-enhancer library which painlessly creates beautiful
default ``matplotlib`` plots. Inspired by `Edward
Tufte <http://www.edwardtufte.com/tufte/>`__'s work on information
design and `Cynthia Brewer <http://www.personal.psu.edu/cab38/>`__'s
work on `color perception <http://colorbrewer2.org/>`__.

I truly believe that scientific progress is impeded when improper data
visualizations are used. I spent a lot of time tweaking my figures to
make them more understandable, and realized the scientific world could
be a better place if the default parameters for plotting libraries
followed recent advances in information design research. And thus
``prettyplotlib`` was born.

Requirements:

-  `matplotlib <http://matplotlib.org/>`__. Can be installed via
   ``pip install matplotlib`` or ``easy_install matplotlib``
-  `brewer2mpl <https://github.com/jiffyclub/brewer2mpl>`__. Can be
   installed via ``pip install brewer2mpl`` or
   ``easy_install brewer2mpl``

Comparison to ``matplotlib``
----------------------------
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/plot_matplotlib_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/plot_prettyplotlib_default.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#plot-lines-eg-time-series-with-a-legend"
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/scatter_matplotlib_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/scatter_prettyplotlib_default.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#scatter-points
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/bar_matplotlib_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/bar_prettyplotlib_default.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#bar
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/hist_matplotlib_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/hist_prettyplotlib_default.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#hist
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/hist_matplotlib_grid.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/hist_prettyplotlib_grid.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#back-to-matplotlib-style-scatterplots
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/boxplot_matplotlib_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/boxplot_prettyplotlib_default.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#boxplot
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/pcolormesh_matplotlib_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/pcolormesh_prettyplotlib_default.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#pcolormesh-heatmaps
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/pcolormesh_matplotlib_positive_default.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/pcolormesh_prettyplotlib_positive.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#pcolormesh-positive-only-data
   :width: 45%

.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/pcolormesh_matplotlib_negative_labels.png
:width: 45%
.. image:: https://raw.github.com/olgabot/prettyplotlib/master/ipython_notebooks/pcolormesh_prettyplotlib_negative_labels.png
:target: https://github.com/olgabot/prettyplotlib/wiki/exampleswith-code#pcolormesh-positive-only-data
   :width: 45%

Quotes
~~~~~~

*"Dis ain't no **ugly**\ plotlib"* - Anonymous

.. |Build Status| image:: https://travis-ci.org/olgabot/prettyplotlib.png?branch=master
:target: https://travis-ci.org/olgabot/prettyplotlib