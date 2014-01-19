import matplotlib.pyplot as plt
from functools import wraps

from prettyplotlib.colors import pretty


@wraps(plt.subplots)
@pretty
def subplots(*args, **kwargs):
    return plt.subplots(*args, **kwargs)

@wraps(plt.subplot2grid)
@pretty
def subplot2grid(*args, **kwargs):
    return plt.subplot2grid(*args, **kwargs)
