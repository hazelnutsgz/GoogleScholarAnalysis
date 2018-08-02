import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import sys

def cdf_plot(data, name, number):
    ecdf = sm.distributions.ECDF(data)
    x = np.linspace(min(data), max(data), number)
    y = ecdf(x)

    #plt.step(x, y, label=name)
    plt.plot(x, y, label=name)

