# plotting_utils.py
"""
Utility functions for plotting
"""

import matplotlib.pyplot as plt
import seaborn as sns


def mf(dims=(6, 4)):
    """
    Quick function "make fig" to make a figure and
    return ax object with specified dimensions
    """
    _, ax = plt.subplots(figsize=dims)
    return ax
