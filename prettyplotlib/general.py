import matplotlib.pyplot as plt
from functools import partial, update_wrapper

from prettyplotlib.colors import pretty


@partial(update_wrapper, wrapped=plt.subplots, assigned=["__doc__"])
@pretty
def subplots(*args, **kwargs):
    return plt.subplots(*args, **kwargs)


@partial(update_wrapper, wrapped=plt.subplot2grid, assigned=["__doc__"])
@pretty
def subplot2grid(*args, **kwargs):
    return plt.subplot2grid(*args, **kwargs)
